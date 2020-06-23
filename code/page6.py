# 绘制横着的条形图
from matplotlib import pyplot as plt, font_manager

a = ["战狼2", "速度与激情8", "功夫瑜伽", "西游伏妖篇", "变形金刚5", "最后的骑士",
     "摔跤吧！爸爸", "加勒比海盗5", "死无对证", "金刚"]
b = [56.01, 26.94, 17.53, 16.49, 15.45, 12.96, 11.8, 11.61, 11.28, 11.12]

# 设置图纸大小
plt.figure(figsize=(20, 8), dpi=80)
# 绘制条形图
plt.barh(range(len(a)), b, height=0.3)
# 设置中文
my_font = font_manager.FontProperties(fname="C:\Windows\Fonts\SimHei.ttf")
# 设置x轴
plt.yticks(range(len(a)), a, fontproperties=my_font)
# 绘制网格
plt.grid(alpha=0.4)
# 展示
plt.show()