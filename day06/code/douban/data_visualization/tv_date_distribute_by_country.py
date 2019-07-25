# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# from data_visualization.data_format import choose_data
from data_visualization.show_data import get_data_frame
import matplotlib.font_manager as fm

'''
实现功能:5.7分以上的不同国家电视剧随时间的变化情况
'''

#设置字体
myfont = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

def show_tv_date_distribute(rate=7):
    fig = plt.figure(figsize=(16, 8))
    ax = plt.subplot()
    #获取数据
    df = get_data_frame()
    #为现存的每条数据作出统计,即让其数量为1,方便之后分组后的聚合
    count_df = pd.DataFrame(np.ones(shape=(len(df),1)),columns=["count"])
    df = df.join(count_df)
    #去除没有时间的电视剧
    new_df = df[pd.notnull(df["release_date"])]
    #选择2000年之后的电视剧
    new_df = new_df[new_df["release_date"]>"19991231"]
    #选择7分以上的上市局
    new_df = new_df[new_df["rating_value"]>=rate]
    #不同国家的电视剧的数量和时间的对应关系并不相同,需要先统一统计的时间,没有的时间段填充0
    date_start = new_df["release_date"].min()
    date_end = new_df["release_date"].max()
    date_period = pd.DataFrame(pd.date_range(date_start, date_end, freq="D",),columns=["release_date"])
    #定义绘图的颜色
    colors = ['red', 'green', 'blue', "cyan", "orange"]
    country_list = new_df["country"].unique().tolist()
    #分组
    for country,grouped in new_df.groupby(by=["country"]):
        #对不同的国家添加统一的时间段,并设置为index
        temp_grouped = grouped.merge(date_period,how="outer",on="release_date")
        temp_grouped = temp_grouped[["release_date","count"]].set_index("release_date")
        #对空白的时间段填充0
        temp_grouped = temp_grouped.fillna(0)
        temp_grouped = temp_grouped.resample("3M").sum()
        # print(temp_grouped.index)
        _x = range(len(temp_grouped.index))
        _y = temp_grouped["count"]
        #绘制散点图,但是效果不明显
        # ax.scatter(_x, _y,
        #            c=colors[country_list.index(country)],
        #            alpha=0.5,
        #            label=country
        #            )
        #绘制折线图
        ax.plot(_x, _y,
                   c=colors[country_list.index(country)],
                   alpha=0.5,
                   label=country
                   )
    #添加图例
    plt.legend()
    # 解决xticklable时间带时分秒
    xticklables = [i.strftime('%Y-%m') for i in temp_grouped.index]
    # 解决xticklable刻度太密集
    plt.xticks(range(0, len(temp_grouped.index), 4), xticklables[::4], rotation=45)
    plt.xlabel("时间",fontproperties=myfont)
    plt.ylabel("时间段内的数量合计",fontproperties=myfont)
    plt.title("不同国家7分以上的电视剧随时间的变化情况",fontproperties=myfont)
    plt.savefig("不同国家7分以上的电视剧随时间的变化情况.png")
    plt.show()


if __name__ == '__main__':
    show_tv_date_distribute()