# coding=utf-8
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


df = pd.read_csv("./911.csv")

df["timeStamp"] = pd.to_datetime(df["timeStamp"])

df.set_index("timeStamp",inplace=True)


#统计出911数据中不同月份电话次数的
count_by_month = df.resample("M").count()["title"]
print(count_by_month)

#画图
_x = count_by_month.index
_y = count_by_month.values

# for i in _x:
#     print(dir(i))
#     break
_x = [i.strftime("%Y%m%d") for i in _x]

plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y)

plt.xticks(range(len(_x)),_x,rotation=45)

plt.show()
