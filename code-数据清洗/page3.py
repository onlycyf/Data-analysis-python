"""
练习题假设在30岁的时候，根据自己和同桌的情况，统计出来了从11到30岁每年看的动漫的数
量如列表a,请绘制出折线图
要求：y轴表示个数
     x轴表示岁数,比如 11岁，12岁
"""
from matplotlib import pyplot as plt, font_manager

x = range(11, 31)
y_1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 6, 7, 8, 9, 11, 2]
y_2 = [2, 31, 45, 5, 1, 2, 4, 1, 4, 3, 5, 1, 5, 5, 6, 3, 3, 1, 4, 3]

# 设置图纸大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置中文字体
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei.ttf")

# 绘图
# label: 设置图例注释  color设置线条颜色， linestyle: 设置线条样式
plt.plot(x, y_1, label="自己", color="orange", linestyle="--")
plt.plot(x, y_2, label="同桌", color="cyan", linestyle="-.")

# 设置x轴
x_age = ["{}岁".format(i) for i in x]
plt.xticks(x, x_age, fontproperties=my_font)
plt.xlabel("年龄", fontproperties=my_font)

# 设置y轴
# plt.yticks(range(min(y), max(y) + 1))
plt.ylabel("番剧数量", fontproperties=my_font)

# 设置标题
plt.title("11~30岁每年看番数量", fontproperties=my_font)

# 绘制网格
plt.grid(alpha=0.2, linestyle="--")

# 添加图例
# prop:设置中文  loc设置图例位置
plt.legend(prop=my_font, loc="upper left")

# 展示图纸
plt.show()
