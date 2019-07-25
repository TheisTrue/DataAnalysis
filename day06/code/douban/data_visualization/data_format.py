# coding=utf-8
from pymongo import MongoClient
from config import MONGO_PORT,MONGO_HOST,MONGO_DB,MONGO_COLLECTION
import re

def choose_data():
    '''
    处理mongodb中的数据,提取有用的字段
    :return: list
    '''
    client = MongoClient(host=MONGO_HOST, port=MONGO_PORT)
    collection = client[MONGO_DB][MONGO_COLLECTION]
    db_data = collection.find()
    data_list = []
    for data in db_data:
        item = {}
        #国家
        item["country"] = data["tv_category"]
        #电视剧的名字
        item["title"] = data["title"]
        #导演
        item["directors"] = "_".join(data["directors"])
        #演员
        item["actors"] = "_".join(data["actors"])
        #data["info"] "刘进/张嘉译/秦海璐/何冰/剧情/历史/2017-04-16(中国大陆)"

        directors_actors_list = data["directors"]
        directors_actors_list.extend(data["actors"])
        temp_info = data["info"].split("(")[0]
        #提取时间
        item["release_date"] = re.findall(r"\d+.*", temp_info)
        if len(item["release_date"])<1:
            item["release_date"] = None
            temp_info = temp_info.split("/")
        else:
            item["release_date"] = item["release_date"][0]
            if "/" in item["release_date"]:
                item["release_date"] = item["release_date"].split("/")[-1]
            temp_info = temp_info.split("/")[:-1]
        #提取分类即tag
        tag_list = []
        temp_info = [i.strip() for i in temp_info if 2>=len(i.strip())>0]
        for i in temp_info:
            if i.strip() not in directors_actors_list:
                tag_list.append(i)
        item["tag"] = "_".join(tag_list)
        #打分的人数
        item["rating_count"] = data["rating"]["count"]
        #分数
        item["rating_value"] = data["rating"]["value"]
        data_list.append(item)
    return data_list

if __name__ == '__main__':
    data_list = choose_data()
    for i in data_list:
        print(i["tag"],"***",i["release_date"])
    print(data_list)



