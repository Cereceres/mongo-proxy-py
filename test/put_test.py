import unittest
from lib.put import put
from lib.db import DB as database
import main
import json

class Testput(unittest.TestCase):

    def test_put_callable(self):
        """Debe definir una funcion put"""
        self.assertTrue(callable(put))
    def test_put_200(self):
        """Debe regresar 200 si objeto existe y lo actualiza"""
        database.insert('test', {"id":"idQueSiExiste", "algunaValor": "algunValor"})
        body, code = put('test', {"id":"idQueSiExiste"},{"algunaValor": "ConAlgunDatoActualizado"})
        self.assertTrue(code == 200)
        print 'body ', body
        object_saved = json.loads(body)
        print 'object_saved ', object_saved
        self.assertTrue(object_saved )

if __name__ == '__main__':
    unittest.main()