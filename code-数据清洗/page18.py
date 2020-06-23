import numpy as np
from matplotlib import pyplot as plt

# 加载国家数据
us_data = "./youtube_video_data/US_video_data_numbers.csv"
uk_data = "./youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
# uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)

# 取评论的数据
t_us_comment = us_data[:, -1]

# 选择比5000小的数据
t_us_comment = t_us_comment[t_us_comment <= 5000]
d = 50
bins_num = (t_us_comment.max() - t_us_comment.min()) // d

plt.figure(figsize=(15, 8), dpi=80)

plt.hist(t_us_comment, bins_num)

plt.show()
