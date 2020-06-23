import numpy as np


# 创建一个全是0的数组
# t1 = np.zeros((2, 3))
# print(t1)

# 全是1
# t1 = np.ones((2, 3))
# print(t1)

# 对角线是1的
# t2 = np.eye(3)
# print(t2)

# 获取最大值和最小值,axis=0,表示列，1表示行
t3 = np.random.randint(0,20, size=(4, 5))
min_t3 = np.argmin(t3, axis=0)
max_t3 = np.argmax(t3, axis=1)
print(t3)
print(min_t3)
print(max_t3)