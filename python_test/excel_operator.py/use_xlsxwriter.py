import xlsxwriter

CommonSheetNameList = [
    "第1筒次010段_12345",
    "第2筒次012段_12345",
    "第3筒次011段_01120",
]

ExcelPath = 'C:\\Users\\Admin\\Desktop\\tesss1\\simple.xlsx'

ProjectInfoDict = {
    "项目名称": "四川省广汉市中石油德页1井",
    "地理位置": "四川省广汉市",
    "井口名称(井号)": "0011",
    "取心筒次": "2021024",
    "岩心直径": 26,
    "其他": ""
}

RockInfoDict = {
    "岩心编号": "202410230851192",
    "岩心名称": "第一筒次010段",
    "岩心块号": "1-10",
    "序列名称": "cpmg_1",
    "测量长度(m)": "-",
    "测量顶深(m)":"-",
    "测量底深(m)":"-",
    "测量时间":"-",
    "数据名称":"-",
    "回波间隔":"-",
    "回波个数":"-",
    "TW":"-",
    "平均次数":"-",
    "其他":"-",
}

class ExcelWriter:

    def __init__(self, aFileName: str, aSheetName: str) -> None:
        self.myWorkbook = xlsxwriter.Workbook(aFileName, {"tmpdir": "C:\\Users\\Admin\\Desktop\\tesss1\\temp", 'strings_to_numbers': False})
        self.myWorksheet = self.myWorkbook.add_worksheet(aSheetName)
        self.myWorkbook.add_worksheet("TEST_1")
        self.myWorkbook.add_worksheet("TEST_2")
        self.myWorkbook.add_worksheet("TEST_3")
        self.initFormatSettings()

    def initFormatSettings(self) -> None:
        self.myTitleFormat = self.myWorkbook.add_format({'bold': True})
        self.myTitleFormat.set_font_size(20)
        self.myTitleFormat.set_align('left')

        self.myContentFormat = self.myWorkbook.add_format()
        self.myContentFormat.set_align('left')

        self.myNormalTitleFormat = self.myWorkbook.add_format({'bold': True})
        self.myNormalTitleFormat.set_align('left')

    def origanizedData(self):
        self.myWorksheet.set_column("A:B", 20) # 第1,2列宽度
        self.myWorksheet.set_column("C:N", 12)
        self.myWorksheet.merge_range(0,0,0,1,"项目数据信息表", self.myTitleFormat)
        currentRow = self.__addProjectInfoToSheet()
        self.__addRockInfoToSheet(currentRow+1)

    def close(self):
        self.myWorkbook.close()

    def __addProjectInfoToSheet(self):
        row = 1
        col = 0
        for key, value in ProjectInfoDict.items():
            self.myWorksheet.write(row, col, key, self.myContentFormat)
            self.myWorksheet.write(row, col+1, value, self.myContentFormat)
            row += 1
        return row

    def __addRockInfoToSheet(self, aRow):
        col = 0
        for keys in RockInfoDict.keys():
            self.myWorksheet.write(aRow, col, keys, self.myNormalTitleFormat)
            col += 1

        row = aRow + 1
        while row < 200:
            col = 0
            for values in RockInfoDict.values():
                self.myWorksheet.write(row, col, values, self.myContentFormat)
                col += 1
            row += 1

def main():
    excelWriter = ExcelWriter(ExcelPath, CommonSheetNameList[0])
    excelWriter.origanizedData()
    excelWriter.close()


if __name__ == '__main__':
    main()