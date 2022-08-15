
import psutil
import pandas as pd
import numpy as np

"""
查看内存使用百分比以及可用内存, 操作大文件时, 保证拥有的内存是dataframe的3到10倍
"""
memory = psutil.virtual_memory()
print(f" {'*' * 3} Memory used percentage - {memory.percent} \n {'*' * 4} Free Memory available - { round(memory.free / (1024.0 ** 3))} GB")

"""
    读取到CSV到内存中,查看内存的占用
"""

data = pd.read_csv("E:\\duke_summary_python\\resourse_files\\SMS-Data.csv")
print(f"***  Memory usage of file - {sum(data.memory_usage()) * 0.000001} MB for {len(data.index)} Rows")

# Limits of Integer Data Type
print(f" ** Output limits of Numpy Integer Data Types ")
print(f" ** limits of Numpy Integer - {np.iinfo(np.int8)}")
print(f" ** limits of Numpy Integer - {np.iinfo(np.int16)}")
print(f" ** limits of Numpy Integer - {np.iinfo(np.int64)}")

# Limits of Float Data Type
print(f" ** Output limits of Numpy Float Data Types ")
print(f" ** limits of Numpy Float - {np.finfo(np.float16)}")
print(f" ** limits of Numpy Float - {np.finfo(np.float64)}")

# Lets print the DataFrame  information
print(f" {data.info()}")
# lets summarize the data types and count of columns
print(f" ** Summarize the data types and count of columns \n{data.dtypes.value_counts()}")

unwanted_columns = ["phoneNumber", "id"]
data_columns = [columns for columns in list(pd.read_csv("E:\\duke_summary_python\\resourse_files\\SMS-Data.csv").columns) if columns not in unwanted_columns]

data_type_conversion_numeric = {
    "phoneNumber": "category",
    "id": "category",
    "updateAt":"category",
    "senderAddress": "category",
    "text": "category"
}
data_one = pd.read_csv("E:\\duke_summary_python\\resourse_files\\SMS-Data.csv", dtype=data_type_conversion_numeric, usecols=data_columns)
print(f"***  Memory usage of the file after dropping cols- {sum(data_one.memory_usage()) * 0.000001} MB for {len(data_one.index)} Rows")
