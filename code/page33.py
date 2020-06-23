import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
现在我们有2015到2017年25万条911的紧急电话的数据
如果我们想统计出不同月份不同类型紧急电话的次数的变化情况，应该怎么做呢？
"""
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 150)
file_path = './youtube_video_data/911.csv'
df = pd.read_csv(file_path)

df['timeStamp'] = pd.to_datetime(df['timeStamp'])
df.set_index('timeStamp', inplace=True)
print(df.head(10))

# 重采样resample，相当于分组
count_by_mouth = df.resample('M').count()['title']

_x = count_by_mouth.index
_x = [i.strftime('%Y%m%d') for i in _x]
_y = count_by_mouth.values

plt.figure(figsize=(20, 8), dpi=80)
plt.plot(range(len(_x)), _y)
plt.xticks(range(len(_x)), _x, rotation=45)

plt.show()
