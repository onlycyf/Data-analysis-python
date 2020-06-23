import pandas as pd
import numpy as np

# 解决终端输出有省略号的问题
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)

file_path = './youtube_video_data/starbucks_store_worldwide.csv'

df = pd.read_csv(file_path)
# print(df.info())
print(df.head(1))

grouped = df.groupby(by='Country')
print(grouped)

# DataFrameGroupBy
# 可以进行遍历
# for i in grouped:
#     print(i)
#     print('*'*100)
# 调用聚合方法
# country_count = grouped['Brand'].count()
# print(country_count['US'])
# print(country_count['CN'])

# 统计中国每个省份的店铺的数量
# China_data = df[df['Country'] == "CN"]
# grouped = China_data.groupby(by='State/Province').count()['Brand']
# print(grouped)

# 数据按照多个条件进行分组,返回Series
# grouped = df['Brand'].groupby(by=[df['Country'], df['State/Province']]).count()
# print(grouped)
# print(type(grouped))

# 数据按照多个条件进行分组,返回DataFrame
grouped1 = df[['Brand']].groupby(by=[df['Country'], df['State/Province']]).count()
grouped2 = df.groupby(by=[df['Country'], df['State/Province']])[['Brand']].count()
grouped3 = df.groupby(by=[df['Country'], df['State/Province']]).count()[['Brand']]

# print(grouped1)
# print(type(grouped1))
# print(grouped2)
# print(type(grouped2))
# print(grouped3)
# print(type(grouped3))

print(grouped1.index)



