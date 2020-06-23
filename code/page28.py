import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

# 解决终端输出有省略号的问题
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
# 统计电影的分类（一部电影可能有多个分类）
file_path = "./youtube_video_data/starbucks_store_worldwide.csv"

# 使用matplotlib呈现出店铺总数排名前10的国家
df = pd.read_csv(file_path)

# 准备数据
data1 = df.groupby(by="Country").count()['Brand'].sort_values(ascending=False)[:10]
# print(data1)

_x = data1.index
_y = data1.values

plt.figure(figsize=(15, 8), dpi=80)
plt.bar(_x, _y)

plt.show()
