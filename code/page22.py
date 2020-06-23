import pandas as pd
import numpy as np

df = pd.read_csv('./youtube_video_data/dogNames2.csv')

# print((df['Count_AnimalName'] > 800) & (df['Count_AnimalName'] < 1000))

t1 = pd.DataFrame(np.arange(12).reshape(3, 4).astype('float'), index=list('abc'), columns=list('wxyz'))
print(t1)
t1.loc['b', 'w'] = np.nan
t1.loc['c', 'w'] = np.nan
print(t1)
# 舍弃nan
print(t1.dropna(axis=0, how='any'))
# 填充nan
# print(t1.fillna(0))
print(t1.fillna(t1.mean()))
