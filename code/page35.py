import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", 1000)
pd.set_option("display.width", 150)

file_path = './PM2.5/BeijingPM20100101_20151231.csv'

df = pd.read_csv(file_path)

# 把分开的字符串通过periodIndex方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")
df["datetime"] = period

# datetime设置为索引
df.set_index("datetime", inplace=True)

# 对df进行降采样
df = df.resample("7D").mean()

# 处理缺失数据, 删除缺失数据
data = df["PM_US Post"]
data_China = df["PM_Dongsi"]

# 画图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_China = [i.strftime("%Y%m%d") for i in data_China.index]
_y = data.values
_y_China = data_China.values

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(range(len(_x)), _y, label="US_POST")
plt.plot(range(len(_x_China)), _y_China, label="CN_POST")

plt.xticks(range(0, len(_x), 10), list(_x)[::10], rotation=45)

plt.legend(loc="best")
plt.show()
