# 将两个国家的数据放在一起分析，同时保留两国信息

import numpy as np

# 加载国家数据
us_data = "./youtube_video_data/US_video_data_numbers.csv"
uk_data = "./youtube_video_data/GB_video_data_numbers.csv"

# 加载国家数据
us_data = np.loadtxt(us_data, delimiter=",", dtype=int)
uk_data = np.loadtxt(uk_data, delimiter=",", dtype=int)
print(us_data.shape)

# 添加国家数据
# 构造全是0和全是1的列
zeros_data = np.zeros((us_data.shape[0], 1)).astype(int)
ones_data = np.ones((uk_data.shape[0], 1)).astype(int)

# 拼接国家数据
us_data = np.hstack((us_data, zeros_data))
uk_data = np.hstack((uk_data, ones_data))

final_data = np.vstack((us_data, uk_data))
print(final_data)
