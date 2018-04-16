import json
from flask import Flask
from flask import request
from lib.get import get
from lib.put import put
from lib.post import post
from lib.delete import delete as remove
app = Flask(__name__)
def parse_string(string):
    try:
        return json.loads(string)
    except:
        return string

@app.route("/<collection>", methods=["GET", "PUT", "POST", "DELETE"])
@app.route("/<collection>/<id>", methods=["GET", "PUT", "DELETE"])
def home(collection, id=None):
    collection = collection
    dataParaGuardar =  parse_string(request.data)
    metodo = request.method
    query = request.args.to_dict()

    if not len(query) and id:
        query = { "_id": id }
    if (metodo == 'GET'):
        return get(collection, query)
    if (metodo == 'PUT'):
        return put(collection, query, dataParaGuardar)
    if (metodo == 'POST'):
        res =  post(collection, dataParaGuardar)
        return res
    if (metodo == 'DELETE'):
        return remove(collection, query)
if __name__ == "__main__":
    app.run(debug=True)