# coding=utf-8
from pymongo import MongoClient
from config import MONGO_PORT,MONGO_HOST,MONGO_DB,MONGO_COLLECTION

class SaveClient: #实现数据的保存
    def __init__(self):
        client = MongoClient(host=MONGO_HOST,port=MONGO_PORT)
        self.collection = client[MONGO_DB][MONGO_COLLECTION]

    def save_to_db(self,content_list):
        if isinstance(content_list,list):
            for content in content_list:
                self.collection.insert(content)
        elif isinstance(content_list,dict):
            self.collection.insert(content)
        print("save suceesss")

_mongo_client = SaveClient()
mongo_client = _mongo_client

