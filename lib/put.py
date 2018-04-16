from db import DB as database
import json

def put(collection='', query={}, data={}):
    update = data
    data_saved = database.update(collection, query, update)
    if not data_saved:
        return json.dumps(data_saved), 200
    return json.dumps(data_saved), 200