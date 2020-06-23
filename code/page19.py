import numpy as np
from matplotlib import pyplot as plt

# 加载国家数据
us_data = "./youtube_video_data/US_video_data_numbers.csv"
uk_data = "./youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
# us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)
# 第一次画完图后发现，数据在500000的地方数据很突兀
uk_data = uk_data[uk_data[:, 1] <= 500000]

# 取评论和喜欢的数据
t_uk_comment = uk_data[:, -1]
t_uk_like = uk_data[:, 1]
print(t_uk_like)
# 绘制散点图
plt.figure(figsize=(15, 8), dpi=80)

plt.scatter(t_uk_like, t_uk_comment)

plt.show()
