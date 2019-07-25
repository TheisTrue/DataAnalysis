# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_visualization.data_format import choose_data
import matplotlib.font_manager as fm


'''
可以统计分析一下结果
1.四个国家电视剧的平均分
2.8分以上的不同分类电视剧的数量统计
2.1 8分以上的不同分类电视剧的用户评价次数
5.不同国家7分以上的电视剧随时间的变化情况
'''

#设置字体
myfont = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')

def get_data_frame(): #从数据库获取数据,并且把release_date变成时间格式
    temp_df = pd.DataFrame(choose_data())
    temp_df["release_date"] = pd.to_datetime(temp_df["release_date"])
    return temp_df

def plot_four_country_ave_rating_value():
    figure = plt.figure()
    ax = plt.subplot()
    df = get_data_frame()
    df_country_rating = df[["country","rating_value"]]
    #根据国家分组,并且获取平均值
    grouped_rating = df_country_rating.groupby("country").mean()
    print(type(grouped_rating))
    y = grouped_rating["rating_value"]
    x = np.arange(len(grouped_rating.index))
    ax.bar(x,y,width=0.5,align="center")
    plt.xticks(x,grouped_rating.index)
    # x轴的值
    plt.xlabel("国家",fontproperties=myfont)
    # y轴值
    plt.ylabel("平均分",fontproperties=myfont)
    # 图的标题
    plt.title("豆瓣电视剧平均分统计",fontproperties=myfont)
    plt.show()


if __name__ == '__main__':
    # plot_four_country_ave_rating_value()
    show_tag_count()