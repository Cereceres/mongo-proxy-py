
import json
from db import DB as database

def get(collection, query = {}):
    inserted = database.find_one('testParaObtener', {"key":"idQueSiExiste"})
    data = database.find(collection, query)
    data_to_return = []
    for datum in data:
        datum['_id'] = str(datum['_id'])
        data_to_return.append(datum)
    return json.dumps(data_to_return), 200