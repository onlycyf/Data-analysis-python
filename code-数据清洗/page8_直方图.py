import random
from matplotlib import pyplot as plt

a = [random.randint(90, 150) for i in range(250)]

# 计算组数
d = 3  # 组距
num_bins = (max(a) - min(a)) // d

# 设置图纸大小
plt.figure(figsize=(15, 8), dpi=80)

# density=True 表示使用频数分布图
plt.hist(a, num_bins, density=True)

# x轴刻度
plt.xticks(range(min(a), max(a) + d, d))

# 绘制网格
plt.grid(alpha=0.5)

plt.show()
