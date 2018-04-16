import json

from db import DB as database

def post(collection, data):
    number_of_keys = len(data)
    if not number_of_keys:
        return '', 400
    id = database.insert(collection, data)

    return json.dumps({'id': str(id)}), 200