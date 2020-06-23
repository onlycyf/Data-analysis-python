import numpy as np

t1 = np.arange(12).reshape(2, 6)
t2 = np.arange(12, 24).reshape(2, 6)
print(t1)
print(t2)

# 竖直拼接
# t3 = np.vstack((t1, t2))
# print(t3)

# 水平拼接
# t4 = np.hstack((t1, t2))
# print(t4)

# 行列交换
t1[[0, 1], :] = t1[[1, 0], :]
print(t1)

t1[:, [0, 1]] = t1[:, [1, 0]]
print(t1)

