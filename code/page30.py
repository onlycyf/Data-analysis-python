import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
现在我们有全球排名靠前的10000本书的数据，那么请统计一下下面几个问题：
1.不同年份书的数量
2.不同年份书的平均评分情况
"""
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 150)

file_path = './youtube_video_data/books.csv'

df = pd.read_csv(file_path)

print(df.head(1))
# 去除original_publication_year列nan的行
book_years_notnan = df[pd.notnull(df['original_publication_year'])]
# 准备数据
book_years = book_years_notnan.groupby(by='original_publication_year').count()['title'].sort_values()
_x = book_years.index
_y = book_years.values
# 画图
plt.figure(figsize=(20, 8), dpi=80)
plt.subplot(1, 2, 1)
plt.bar(range(len(_x)), _y)
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)

# 不同年份书的平均评分情况
data1 = book_years_notnan['average_rating'].groupby(by=book_years_notnan['original_publication_year']).mean()

print(data1)

_x = data1.index
_y = data1.values
plt.subplot(1, 2, 2)
plt.plot(range(len(_x)), _y)
plt.xticks(list(range(len(_x)))[::10], _x[::10].astype(int), rotation=45)
plt.show()
