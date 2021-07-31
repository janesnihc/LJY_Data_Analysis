import pandas as pd
import numpy as np

# 读取csv文件
df = pd.read_csv("test.csv")
# 查看数据表头
print(df.columns.tolist())
# 查看数据大小
print("行:", df.shape[0], "列:", df.shape[1])
# 查看数据前5行
print(df.head())

