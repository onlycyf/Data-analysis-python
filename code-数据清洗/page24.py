from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

# 对于这一组电影数据，如果我们想知道runtime的分布情况，应该如何呈现数据

file_path = "./youtube_video_data/IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
print(df.head(1))
# print(df.info())
# 准备数据
runtime_data = df['Runtime (Minutes)'].values
# print(runtime_data)
max_runtime = runtime_data.max()
min_runtime = runtime_data.min()

print(max_runtime - min_runtime)

# 计算组数
num_bin = (max_runtime - min_runtime) // 5

# print(rating_data)

plt.figure(figsize=(15, 8), dpi=80)
plt.hist(runtime_data, num_bin)

plt.xticks(range(min_runtime, max_runtime + 5, 5))

plt.show()
