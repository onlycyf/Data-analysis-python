import numpy as np

us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
ug_file_path = './youtube_video_data/GB_video_data_numbers.csv'

t1 = np.loadtxt(us_file_path, delimiter=',', dtype='int')

# 取连续的多行，取出2-8行
print(t1[1:8])
print('*' * 100)

# 取不连续的多行，例如：取出第2,8,10行
# print(t1[[2, 8, 10]])
# print(t1[1, :])
# print(t1[2:, :])
# print('*' * 100)

# 取列
# print(t1[:, 0])
# print('*' * 100)

# 取连续的多列
# print(t1[:, 2:])
# print('*' * 100)

# 取不连续的多列
# print(t1[:, [0, 2]])
# print('*' * 100)

# 取多列多行
# 取出第2行3列
# print(t1[1, 2])
# 取出第3行到第5行，第2列到第4列的结果
a = t1[2:5, 1:4]
# print(a)

# 取多个不相邻的点
c = t1[[0,2], [0,1]]
print(c)
