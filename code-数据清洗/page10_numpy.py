import numpy as np
import random

t1 = np.array([1, 2, 3, ])
print(t1)
print(type(t1))

t3 = np.arange(4, 10, 2)
print(t3)
print(type(t3))

print(t3.dtype)

# 手动指定元素类型dtype
t4 = np.array(range(1, 4), dtype=float)
print(t4)
print(t4.dtype)

t5 = np.array([1, 1, 1, 0, 0, 1], dtype=bool)
print(t5)

# 调整数据类型astype
t6 = t5.astype("i1")
print(t6)
print(t6.dtype)

# numpy中的小数
t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)

# 保留3位小数
t7 = np.round(t7, 3)
print("t7: {}".format(t7))
print("-----------------------------")

# shape显示数组结构
t8 = np.array([[1, 2, 3], [4, 5, 6]])
t9 = np.array([1, 2, 2, 3, 4])
print(t8)
print(t8.shape)
print(t9.shape)

# reshape改变数组结构
t10 = np.array([0, 1, 2, 3, 4, 5, 6, 7])
t11 = t10.reshape(2, 4)
print(t11)

# 变成一维数组flatten
t12 = t11.flatten()
print(t12)
t13 = np.random.randint(0,10,size=[3,3,2])
print(t13)
