from matplotlib import pyplot as plt, font_manager

y_3 = [11, 10, 11, 9, 8, 8, 9, 14, 18, 16, 16, 15, 14, 14, 15, 15, 15, 16, 17,
       16, 15, 14, 16, 15, 14, 15, 16, 17, 14, 20, 19]
y_10 = [28, 23, 25, 23, 23, 24, 25, 19, 18, 16, 16, 15, 14, 14, 15, 15, 15, 16,
        17, 16, 15, 14, 16, 15, 14, 15, 16, 17, 14, 20, 16]

x_3 = range(1, 32)
x_10 = range(51, 82)

# 设置图纸大小
plt.figure(figsize=(20, 8), dpi=80)
# 设置中文
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei.ttf")
# 绘制散点图
plt.scatter(x_3, y_3, label="3月")
plt.scatter(x_10, y_10, label="10月")

# 调整x轴的刻度
_x = list(x_3) + list(x_10)
_xticks_labels = ["3月{}日".format(i) for i in x_3]
_xticks_labels += ["10月{}日".format(i-50) for i in x_10]
plt.xticks(_x[::3], _xticks_labels[::3], fontproperties=my_font, rotation=45)

# 添加描述信息
plt.xlabel("时间", fontproperties=my_font)
plt.ylabel("温度", fontproperties=my_font)
plt.title("3月和10月每天的气温变化", fontproperties=my_font)

# 添加图例
plt.legend(prop=my_font, loc="upper center")

plt.show()
