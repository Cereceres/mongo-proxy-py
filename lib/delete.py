from db import DB as database

def delete(collection='', query={}):
    database.remove(collection, query)
    return 'ok', 200