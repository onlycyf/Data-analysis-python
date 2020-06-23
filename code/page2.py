# 练习题请绘制10点到12点每分钟温度变化情况，气温从20-35度中取随机数

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

# windows/linux 设置字体的方式
# font = {'family': 'MicroSoft YaHei',
#         'weight': 'bold',
#         'size': 'larger'}
# matplotlib.rc("font", **font)

# 通用解决方式
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei.ttf")

x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]

plt.figure(figsize=(20, 8), dpi=80)

plt.plot(x, y)

# 调整x轴的刻度
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
# 取步长，数字和字符串一一对应
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation=45, fontproperties=my_font)  # rotation旋转90度

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("10点到12点每分钟温度变化情况", fontproperties=my_font)

plt.show()


