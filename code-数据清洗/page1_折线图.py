import random
from matplotlib import pyplot as plt

x = range(2, 26, 2)
y = [1, 2, 5, 23, 5, 26, 26, 27, 3, 14, 5, 14]

# 设置图片大小
plt.figure(figsize=(20, 8), dpi=80)

# 绘图
plt.plot(x, y)

# 绘制X轴的刻度
_xtick_labels = [i / 2 for i in range(4, 49)]
plt.xticks(_xtick_labels[::3])

# 绘制Y轴长度
plt.yticks(range(min(y), max(y) + 1))

# 保存
# plt.savefig("./t1.png")

# 展示图形
plt.show()
