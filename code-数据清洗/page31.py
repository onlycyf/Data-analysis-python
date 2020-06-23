import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
现在我们有2015到2017年25万条911的紧急电话的数据，请统计出出这些数据中不同类型的紧急情况的次数，
如果我们还想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
"""
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 150)
file_path = './youtube_video_data/911.csv'
df = pd.read_csv(file_path)

# print(df.head(1))
# print(df.info())

# 不同类型的紧急情况的次数
# 获取分类
# print(df['title'].str.split(': '))
# temp_list = df['title'].str.split(': ').tolist()
# cate_list = list(set([i[0] for i in temp_list]))
# print(cate_list)

# 构造全为0的数组
# zeros_df = pd.DataFrame(np.zeros((df.shape[0], len(cate_list))), columns=cate_list)
# for cate in cate_list:
#     zeros_df[cate][df['title'].str.contains(cate)] = 1
# # print(zeros_df)
# sums = zeros_df.sum(axis=0)
# print(sums)

# 下面有另一种做法，通过在原数据上添加一列，在通过groupby求和
temp_list = df['title'].str.split(': ').tolist()
cate_list = [i[0] for i in temp_list]
df['cate'] = pd.DataFrame(np.array(cate_list).reshape(df.shape[0], 1))
print(df.head(10))
sums_data = df.groupby(by='cate').count()['title']
print(sums_data)
