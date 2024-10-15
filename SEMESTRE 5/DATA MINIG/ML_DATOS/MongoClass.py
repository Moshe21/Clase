from mongoConfig import config
from pymongo import MongoClient

class MongoClass:

    def __init__(self):
        self.client = MongoClient(config["URI"])
        self.dbman = self.client[config["DATABASE"]]
        self.collman = self.dbman[config["COLLECTION"]]

    def storeData(self,json):
        result = self.collman.insert_one(json)
        self.client.close()
        return result.inserted_id

    def storeDataMany(self,jsonDataArray):
        result = self.collman.insert_many(jsonDataArray)
        self.client.close()
        return result.inserted_ids