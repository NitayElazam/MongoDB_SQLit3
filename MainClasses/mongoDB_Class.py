from pymongo import *


class Mongo:
    def __init__(self, string_connection: str, database_name: str):
        try:
            self._connection = MongoClient(string_connection)
            self._database_connection = self._connection[database_name]
        except Exception as error:
            raise error

    def create_collection(self, collection_name: str):
        try:
            self._collection = self._database_connection[collection_name]
            self._collection.insert_one({})
        except Exception as error:
            raise error

    def insert_data_to_collection(self, collection_name: str, data: list):
        try:
            _collection = self._database_connection[collection_name]
            _collection.insert_many(data)
        except Exception as error:
            raise error

    def findByLimitAndConditions(self, collection_name: str, limit: int=None, condition=None, keys=None) -> str:
        try:
            total = ""
            _collection = self._database_connection[collection_name]
            if condition is None: condition = {}
            if keys is None: keys = {}
            if limit is None: limit = len(list(_collection.find()))

            for data in _collection.find(condition, keys).limit(limit): total += str(data) + "\n"
            return total
        except Exception as error:
            raise error

    def deleteOneByCondition(self, collection_name: str, condition: dict):
        try:
            _collection = self._database_connection[collection_name]
            _collection.delete_one(condition)
        except Exception as error:
            raise error

    def deleteCollection(self, collection_name: str):
        try: self._database_connection[collection_name].drop()
        except Exception as error: raise error

    def updateData(self, collection_name: str, condition: dict, newData: dict):
        try:
            _collection = self._database_connection[collection_name]
            newData = {"$set": newData}
            _collection.update_one(condition, newData)
        except Exception as error: raise error
