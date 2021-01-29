import matplotlib.pyplot as plt
import numpy as np

# 火柴杆图
'''
火柴杆的线条格式
x轴从0到20，画50根火柴,根据x计算y轴的值
'''
x = np.linspace(0, 20, 50)
y = np.sin(x + 1) + np.cos(x ** 2)

# Y轴基线位置
bottom = -0.1
# 设置图例
label = 'delta'

'''
markerline 火柴杆末端的标记
baseline 规定基线的外观
label设置火柴杆图图例的标签
'''
markerline, stemlines, baseline = plt.stem(x, y, bottom=bottom, label=label)

'''
plt.setp()绘制阶梯图, 第三个参数设置火柴杆的形状
'''
plt.setp(markerline, color='red', marker='o')
plt.setp(stemlines, color='blue', linestyle=':')
plt.setp(baseline, color='grey', linewidth=2, linestyle='-')

plt.legend()

plt.show()
