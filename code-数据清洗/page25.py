from matplotlib import pyplot as plt
import pandas as pd

# 对于这一组电影数据，如果我们想知道rating的分布情况，应该如何呈现数据
file_path = "./youtube_video_data/IMDB-Movie-Data.csv"

df = pd.read_csv(file_path)
print(df.head(1))
# print(df.info())
# 准备数据
rating_data = df['Rating'].values

max_rating = rating_data.max()
min_rating = rating_data.min()
print(max_rating, min_rating)

# 设置不等宽的组距， hist方法中取到的会是一个左闭右开的区间[1.9, 3.5)
num_bin_list = [1.9, 3.5]
i = 3.5
while i <= max_rating:
    i += 0.5
    num_bin_list.append(i)

# 设置图形大小
plt.figure(figsize=(15, 8), dpi=80)
plt.hist(rating_data, num_bin_list)

# xticks让之前的组距能够对应上
plt.xticks(num_bin_list)

plt.show()
