# coding=utf-8
from matplotlib import pyplot as plt
from matplotlib import font_manager

interval = [0,5,10,15,20,25,30,35,40,45,60,90]
width = [5,5,5,5,5,5,5,5,5,15,30,60]
quantity = [836,2737,3723,3926,3596,1438,3273,642,824,613,215,47]


print(len(interval),len(width),len(quantity))

#设置图形大小
plt.figure(figsize=(20,8),dpi=80)



plt.bar(range(12),quantity,width=1)

#设置x轴的刻度
_x = [i-0.5 for i in range(13)]
_xtick_labels =  interval+[150]
plt.xticks(_x,_xtick_labels)

plt.grid(alpha=0.4)
plt.show()
