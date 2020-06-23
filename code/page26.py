import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
# 解决终端输出有省略号的问题
# 设置显示的最大列、宽等参数，消掉打印不完全中间的省略号
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
# 统计电影的分类（一部电影可能有多个分类）
file_path = "./youtube_video_data/IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

temp_genre_list = df['Genre'].str.split(',').tolist()
genre_list = list(set([i for j in temp_genre_list for i in j]))

# 构造全为0的数组
zero_df = pd.DataFrame(np.zeros((df.shape[0], len(genre_list))), columns=genre_list)
# print(zero_df)

# 给每个电影出现分类的位置赋值为1
for i in range(df.shape[0]):
    zero_df.loc[i, temp_genre_list[i]] = 1

# print(zero_df)

# 统计每个类型的电影总和
genre_count = zero_df.sum(axis=0)

print(genre_count)

# 排序
genre_count = genre_count.sort_values()
_x = genre_count.index
_y = genre_count.values
print(_x)
print(_y)
# 画图
plt.figure(figsize=(15, 8), dpi=80)
plt.bar(_x, _y)
plt.show()
