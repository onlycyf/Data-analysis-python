import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

"""
统计出911数据中不同月份不同类型的电话的次数的变化情况
"""
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 150)
file_path = './youtube_video_data/911.csv'
df = pd.read_csv(file_path)

# 把时间字符串转换为时间类型
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

# 添加列，表示分类
temp_list = df["title"].str.split(": ").tolist()
cate_list = [i[0] for i in temp_list]
df["cate"] = pd.DataFrame(np.array(cate_list).reshape(df.shape[0], 1))
# 这里把设置索引放在下面是因为如果先设置索引，自己建立的cate的Dataframe和设置索引不一样，合并会出问题
df.set_index('timeStamp', inplace=True)

plt.figure(figsize=(20, 8), dpi=80)

# 分组
for group_name, group_data in df.groupby(by="cate"):
    # 对不同的分类都进行绘图

    count_by_mouth = group_data.resample("M").count()['title']
    _x = count_by_mouth.index
    _y = count_by_mouth.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)), _y, label=group_name)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()
