import pandas as pd
import numpy as np
from matplotlib import pyplot as plt, font_manager

# 解决终端输出有省略号的问题
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
# 统计电影的分类（一部电影可能有多个分类）
file_path = "./youtube_video_data/starbucks_store_worldwide.csv"
# 设置中文
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei.ttf")

df = pd.read_csv(file_path)
# 使用matplotlib呈现出中国每个城市的店铺数量
df = df[df['Country'] == 'CN']
# 准备数据
data_CN = df.groupby(by='City')['Brand'].count().sort_values(ascending=False)[:25]
print(data_CN)

_x = data_CN.index
_y = data_CN.values
plt.figure(figsize=(15, 12), dpi=80)

# plt.bar(_x, _y, width=0.3)
plt.barh(_x, _y, height=0.3)

plt.xticks(fontproperties=my_font)
plt.yticks(fontproperties=my_font)

plt.show()
