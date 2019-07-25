# coding=utf-8
from spider.parse import parse_url
import json
from spider.save import mongo_client

class DoubanSpider:
    def __init__(self):
        self.url_temp = "https://m.douban.com/rexxar/api/v2/subject_collection/{}/items?os=ios&for_mobile=1&start={}&count=50&_=0"
        self.start_urls_temp =[
            {
                "tv_category":"chinese",
                "tv_url_parameter":"filter_tv_domestic_hot",
                "total_num":None
            },
            {
                "tv_category":"american",
                "tv_url_parameter":"filter_tv_american_hot",
                "total_num": None
            },
            {
                "tv_category":"english",
                "tv_url_parameter":"filter_tv_english_hot",
                "total_num": None
            },
            {
                "tv_category":"korean",
                "tv_url_parameter":"filter_tv_korean_drama_hot",
                "total": None
            },
            {
                "tv_category": "japanese",
                "tv_url_parameter": "filter_tv_japanese_hot",
                "total": None
            },
        ]

    def get_start_urls(self): #设置开始的url
        items = []
        for item in self.start_urls_temp:
            item["parse_url"] = self.url_temp.format(item["tv_url_parameter"], 0)
            items.append(item)
        return items

    def get_content_list(self,html_str,item): #提取数据
        data = json.loads(html_str)
        if item.get("total") is None:
            item["total"] = data["total"]
        subject_collection_items = data["subject_collection_items"]
        content_list = []
        for item_temp in subject_collection_items:
            print(item_temp)
            item_temp.update(item)
            content_list.append(item_temp)
        now_page_start = data["start"]  #当前url启动的时候的offsite
        if now_page_start<item["total"]:
            next_page_url = self.url_temp.format(item["tv_url_parameter"], now_page_start+50)
        else:
            next_page_url = None

        return  content_list,next_page_url


    def run(self): #主逻辑
        items = self.get_start_urls()
        print(items)
        for item in items:
            next_page_url = item["parse_url"]
            while next_page_url is not None:
                html_str = parse_url(next_page_url)
                content_list,next_page_url = self.get_content_list(html_str,item)
                mongo_client.save_to_db(content_list)

if __name__ == '__main__':
    douban_spider = DoubanSpider()
    douban_spider.run()

