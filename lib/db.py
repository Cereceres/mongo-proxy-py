from pymongo import MongoClient, uri_parser
from bson.objectid import ObjectId
import os
host =  os.environ.get('HOST') or 'mongodb://localhost'
port =  os.environ.get('PORT') or '27017'
url =  os.environ.get('URL') or host + ':' + port
url_parsed = uri_parser.parse_uri(url)
database_name = url_parsed.get('database')
database =  os.environ.get('DB') or database_name or 'testing'
client = MongoClient(url)
db = client.get_database(name=database)



class DB:
    @staticmethod
    def find(collection, query = {}):
        if query.get('_id'):
            query['_id'] = ObjectId(query.get('_id'))
        fund  = db[collection].find(query)
        returned = []
        for data in fund:
            data['_id'] = str(data['_id'])
            returned.append(data)
        return returned
    @staticmethod
    def find_one(collection, query = {}):
        if query.get('_id'):
            query['_id'] = ObjectId(query.get('_id'))
        fund = db[collection].find_one(query)
        fund['_id'] = str(fund['_id'])
        return fund
    @staticmethod
    def insert(collection, data):
        inserted = db[collection].insert(data)
        return inserted
    @staticmethod
    def update(collection, query={},data={}):
        if query.get('_id'):
            query['_id'] = ObjectId(query.get('_id'))
        db[collection].update(query, {"$set": data})
        updated = db[collection].find(query)
        returned = []
        for data in updated:
            data['_id'] = str(data['_id'])
            returned.append(data)
        return returned
    @staticmethod
    def remove(collection, query={},data={}):
        if query.get('_id'):
            query['_id'] = ObjectId(query.get('_id'))
        return db[collection].delete_many(query, data)