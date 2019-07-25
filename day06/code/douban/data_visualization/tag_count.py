# coding=utf-8
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from data_visualization.show_data import get_data_frame
import matplotlib.font_manager as fm
'''
实现功能:不同分类的电视剧数量的统计
'''

myfont = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
def show_tag_count():
    df = get_data_frame()
    df_tag = df[["country", "rating_value", "tag"]]

    # 切割组成集合,tags是一个带集合的列表
    tags = [set(x.split("_")) for x in df_tag["tag"]]
    # 把所有的tag组成一个集合
    tags = set.union(*tags)
    # 设置一个(len(df_tag),len(tags))的全是0元素的2维数组
    dummies = pd.DataFrame(np.zeros((len(df_tag), len(tags))), columns=tags)

    for i, tag in enumerate(df_tag["tag"]):
        dummies.ix[i, tag.split("_")] = 1
    # df_new = df_tag.join(dummies.add_prefix("tag_")) #添加join之后字段的前缀
    df_new = df_tag.join(dummies)
    # 删除空字符串的那一列
    df_new = df_new.drop("", axis=1)
    print(df_new.columns)
    tag_list = df_new.columns[4:]
    tag_count = []
    for tag in tag_list:
        tag_count.append([tag,df_new[tag].sum()])
    #排序,让柱状图按照顺序显示
    tag_count.sort(key=lambda x:x[1],reverse=True)
    figure = plt.figure(figsize=(10, 8))
    ax = plt.subplot()
    # 画竖着的直方图
    # ax.bar(range(len(tag_list)), count, width=0.5, align="center",)
    # plt.xticks(range(len(tag_list)), tag_list,rotation=90,fontproperties=myfont)
    # 画横着的直方图
    ax.barh(range(len(tag_count)), [i[1] for i in tag_count], align="center", color='#EE7600', ecolor='black')
    plt.yticks(range(len(tag_count)), [i[0] for i in tag_count], fontproperties=myfont)

    plt.ylabel("分类", fontproperties=myfont)
    # y轴值
    plt.xlabel("数量", fontproperties=myfont)
    # 图的标题
    plt.title("不同分类电视剧的数量统计", fontproperties=myfont)
    plt.savefig("不同分类电视剧的数量统计.jpg")
    plt.show()


if __name__ == '__main__':
    # plot_four_country_ave_rating_value()
    show_tag_count()
    # coding=utf-8