# 轴axis
# numpy读数据
# np.loadtxt(fname, dtype=np.float, delimiter=None, skiprows=0,usecols=None, unpack=False)
import numpy as np


us_file_path = "./youtube_video_data/US_video_data_numbers.csv"
ug_file_path = './youtube_video_data/GB_video_data_numbers.csv'

t1 = np.loadtxt(us_file_path, delimiter=',', dtype='int', unpack=True)

print(t1)
print("*********************************")

t2 = np.random.randint(1,30, size=(3,5))
print(t2)
print(t2.swapaxes(1,0))