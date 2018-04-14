# se importan las dependencias externas
import json
from flask import Flask
from flask import request
# se importan las dependencias locales
from lib.get import get
from lib.put import put
from lib.post import post
from lib.delete import delete as remove
# se instancia la app
app = Flask(__name__)
# funcion para parsear una cadena a json
def parse_string(string):
    try:
        return json.loads(string)
    except:
        return string

@app.route("/<collection>", methods=["GET", "PUT", "POST", "DELETE"])
def home(collection):
    collection = collection
    # se obtiene el dato para guardar
    datoParaGuardar =  parse_string(request.data)
    # se obtiene el metodo
    metodo = request.method
    # se obtiene la query
    query = request.args.to_dict()
    # se comprueban los metodos llamados
    if (metodo == 'GET'):
        return get(collection, query)
    if (metodo == 'PUT'):
        response =  put(collection, query, datoParaGuardar)
        print 'respobse ', response
        return response
    if (metodo == 'POST'):
        res =  post(collection, datoParaGuardar)
        print 'res ', res
        return res
    if (metodo == 'DELETE'):
        return remove(collection, query)
# se inicia la app
if __name__ == "__main__":
    app.run(debug=True)