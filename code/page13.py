import numpy as np


# 将数值替换
t1 = np.arange(24).reshape(4,6)
print(t1)

# 将t1中小于10的元素替换成0
# t1[t1<10] = 0
# print(t1)

# bool索引
# print(t1<10)

# 将小于10的替换成10，大于18的替换成18，clip
# t1 = t1.clip(10, 18)
# print(t1)

# 将某个元素替换成nan，要先将元素类型变成float
t1 = t1.astype(float)
t1[2,4] = np.nan
print(t1)