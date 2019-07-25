# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

my_font = font_manager.FontProperties(fname="/System/Library/Fonts/PingFang.ttc")

y_1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y_2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y_1,label="自己",color="#F08080")
plt.plot(x,y_2,label="同桌",color="#DB7093",linestyle="--")

#设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels,fontproperties=my_font)
# plt.yticks(range(0,9))

#绘制网格
plt.grid(alpha=0.4,linestyle=':')

#添加图例
plt.legend(prop=my_font,loc="upper left")

#展示
plt.show()
