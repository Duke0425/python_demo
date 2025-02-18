import sys, os
import pandas as pd
import math


def ReadData(filepath):
    pd.io.formats.excel.header_style = None

    data = pd.read_excel(filepath)

    return data.loc[:, ~data.columns.str.contains('Unnamed')]

def WriteData(data, filepath):
    writer = pd.ExcelWriter(filepath, engine='xlsxwriter')
    data.to_excel(writer, sheet_name='考勤表', index=False, startrow=0, header=False)
    workbook = writer.book
    worksheet = writer.sheets['考勤表']

    # Add a header format.
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'font_name' : '宋体',
        'font_size' : 12,
        'align' : 'center',
        'valign': 'vcenter',
        'bg_color': '#646a73',
        'font_color': '#ffffff',
        'border': 1
    })

    format = workbook.add_format({
        'text_wrap': True,
        'font_name' : '宋体',
        'font_size' : 12,
        'align' : 'center',
        'valign': 'vcenter',
        'border': 1
    })

    # Write the column headers with the defined format.
    for col_num, value in enumerate(data.columns.values):
        worksheet.write(0, col_num, value, header_format)

    for row, row_data in data.iterrows():
        if row == 0:
            continue

        for col, (name, col_data) in enumerate(row_data.iteritems()):
            worksheet.write(row, col, col_data, format)

    for i in range(len(data.index)):
        worksheet.set_column(i, i, 11)

    writer.save()

def ConvertToMinutes(t):
    return int(t[0]) * 60 + int(t[1])

def FormatTime(minutes):
    return '{}:{}'.format(minutes // 60, minutes - (minutes // 60) * 60)

def ComputeTime(time_str):
    times = time_str.split('\n')
    times = [ConvertToMinutes(t.split(':')) for t in times]

    point1_time = ConvertToMinutes([11, 45])
    point2_time = ConvertToMinutes([13, 00])

    early_time_begin = ConvertToMinutes([6, 30])
    early_time_end = ConvertToMinutes([8, 30])

    night_time_begin = ConvertToMinutes([20, 30])
    night_time_end = ConvertToMinutes([24, 00])

    early_minutes = 0
    total_minutes = 0
    night_minutes = 0

    for i in range(0, len(times) // 2):
        start_time = times[i * 2]
        end_time = times[i * 2 + 1]

        if start_time < early_time_end:
            early_minutes += (min(end_time, early_time_end) - max(start_time, early_time_begin))

        if end_time > night_time_begin:
            night_minutes += (min(end_time, night_time_end) - max(start_time, night_time_begin))

        minutes1 = 0
        minutes2 = 0

        if start_time <= point1_time:
            if end_time <= point1_time:
                minutes1 = end_time - start_time
            else:
                minutes1 = point1_time - start_time
        else:
            minutes1 = 0

        if end_time >= point2_time:
            temp_start_time = 0
            temp_end_time = end_time

            if start_time >= point2_time:
                temp_start_time = start_time
            else:
                temp_start_time = point2_time

            minutes2 = temp_end_time - temp_start_time
        else:
            minutes2 = 0

        total_minutes += (minutes1 + minutes2)

    return total_minutes, early_minutes, night_minutes

def SumAttendanceMinutes(data, need_minutes):
    minutes = []

    for people_index, row in data.iterrows():
        if people_index == 0:
            continue

        total_minutes = 0
        weekday_minutes = 0
        early_minutes = 0
        night_minutes = 0

        for index, value in row.iteritems():
            if index == '姓名' or index == '工号' or index == '部门':
                continue

            if value == '-':
                continue

            if not isinstance(value, str):
                print("{} {} {} (时间格式不是文本模式, 请调整该时间的格式)".format(row['姓名'], index.replace("\n", " "), value))
                continue

            day_minutes, day_early_minutes, day_night_minutes = ComputeTime(value)
            total_minutes += day_minutes

            if index.endswith("周六") or index.endswith("周日"):
                weekday_minutes += day_minutes
            else:
                early_minutes += day_early_minutes
                night_minutes += day_night_minutes

        real_minutes = 0

        if total_minutes <= need_minutes:
            real_minutes = total_minutes
        else:
            real_minutes = total_minutes + 0.25 * weekday_minutes + 0.25 * early_minutes
            if night_minutes >= 20 * 60:
                real_minutes += 0.25 * night_minutes

        minutes.append([math.ceil(total_minutes), math.ceil(real_minutes)])

    return minutes


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("""用法:
    attendance.exe raw_filename(考勤原始数据) standard_minutes(标准工作时间 分钟) result_filename(处理后的考勤数据)
                """)
        sys.exit(0)

    if len(sys.argv) == 3:
        raw_filepath = sys.argv[1]
        need_minutes = sys.argv[2]
        result_filepath = os.path.dirname(os.path.abspath(raw_filepath)) + '/processed_' + os.path.basename(raw_filepath)
    else:
        raw_filepath = sys.argv[1]
        need_minutes = sys.argv[2]
        result_filepath = sys.argv[3]

    if not os.path.exists(raw_filepath):
        print(os.path.abspath(raw_filepath), " 不存在.")
        sys.exit(0)

    data = ReadData(raw_filepath)

    minutes = SumAttendanceMinutes(data, int(need_minutes))
    total_minutes = [m[0] for m in minutes]
    jia_quan_minutes = [m[1] for m in minutes]
    total_minutes.insert(0, 0)
    jia_quan_minutes.insert(0, 0)

    data['总工时(HH:MM)'] = [FormatTime(m) for m in total_minutes]
    data['加权总工时(HH:MM)'] = [FormatTime(m) for m in jia_quan_minutes]

    WriteData(data, result_filepath)
