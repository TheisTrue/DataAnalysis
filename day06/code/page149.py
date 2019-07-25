# coding=utf-8
import pandas as pd
from matplotlib import  pyplot as plt
file_path = "./PM2.5/BeijingPM20100101_20151231.csv"

df = pd.read_csv(file_path)

#把分开的时间字符串通过periodIndex的方法转化为pandas的时间类型
period = pd.PeriodIndex(year=df["year"],month=df["month"],day=df["day"],hour=df["hour"],freq="H")
df["datetime"] = period
# print(df.head(10))

#把datetime 设置为索引
df.set_index("datetime",inplace=True)

#进行降采样
df = df.resample("7D").mean()
print(df.head())
#处理缺失数据，删除缺失数据
# print(df["PM_US Post"])

data  =df["PM_US Post"]
data_china = df["PM_Nongzhanguan"]

print(data_china.head(100))
#画图
_x = data.index
_x = [i.strftime("%Y%m%d") for i in _x]
_x_china = [i.strftime("%Y%m%d") for i in data_china.index]
print(len(_x_china),len(_x_china))
_y = data.values
_y_china = data_china.values


plt.figure(figsize=(20,8),dpi=80)

plt.plot(range(len(_x)),_y,label="US_POST",alpha=0.7)
plt.plot(range(len(_x_china)),_y_china,label="CN_POST",alpha=0.7)

plt.xticks(range(0,len(_x_china),10),list(_x_china)[::10],rotation=45)

plt.legend(loc="best")

plt.show()