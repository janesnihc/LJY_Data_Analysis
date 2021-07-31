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
# 单独查看wangpeng的数据
print(df.loc[df["name"] == "wangpeng"])


# 数据透视表部分
# 查看每个人的得分（score）
print(df.groupby("name")["score"].sum())

