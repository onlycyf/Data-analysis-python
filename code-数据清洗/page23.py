import pandas as pd
import numpy as np

file_path = "./youtube_video_data/IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)

print(df.head(1))

# 获取电影平均评分
print(df['Rating'].mean())

# 导演人数
# print(len(df['Director'].tolist()))
print(len(df['Director'].unique()))

# 获取演员的人数
temp_actors_list = df['Actors'].str.split(',').tolist()
actors_list = [i for j in temp_actors_list for i in j]
actors_nums = len(set(actors_list))
print(actors_nums)
