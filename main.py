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
    coleccion = collection
    # se obtiene el dato para guardar
    datoParaGuardar =  parse_string(request.data)
    # se obtiene el metodo
    metodo = request.method
    # se obtiene la consulta
    consulta = request.args
    # se comprueban los metodos llamados
    if (metodo == 'GET'):
        return get(coleccion, consulta)
    if (metodo == 'PUT'):
        return put(coleccion, consulta, datoParaGuardar)
    if (metodo == 'POST'):
        res =  post(coleccion, datoParaGuardar)
        print 'res ', res
        return res
    if (metodo == 'DELETE'):
        return remove(coleccion, consulta)
# se inicia la app
if __name__ == "__main__":
    app.run(debug=True)