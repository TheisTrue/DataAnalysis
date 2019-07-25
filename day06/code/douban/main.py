# coding=utf-8
from spider.douban_spider import DoubanSpider
from data_visualization.show_data import plot_four_country_ave_rating_value
from data_visualization.tag_count import show_tag_count
from data_visualization.tv_date_distribute import show_tv_date_distribute
# from data_visualization.tv_date_distribute_by_country import show_tv_date_distribute
if __name__ == '__main__':
    # douban_spider = DoubanSpider()
    # douban_spider.run()
    # plot_four_country_ave_rating_value()
    # show_tag_count()
    show_tv_date_distribute()