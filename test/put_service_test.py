import unittest
import main
from lib.db import DB as database
import json

class TestPut(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_put(self):
        """Debe regresar 200 si objeto existe y lo actualiza"""
        database.insert('testParaActualizar', {"key":"idQueSiExiste", "algunaValor": "algunValor"})
        saved = database.find_one('testParaActualizar', {"key":"idQueSiExiste"})
        print 'saved ', saved
        headers = {"Content-Type": "application/json" }
        query = {"key":"idQueSiExiste"}
        data = {"algunaValor": "updateAlgunValor"}
        response = self.app.put('/testParaActualizar', query_string=query, headers=headers, data=json.dumps(data))
        print 'response ', response.status_code
        self.assertTrue(response.status_code == 200)
        object_saved = json.loads(response.get_data())
        print 'object_saved ', object_saved
        self.assertTrue(object_saved )



if __name__ == '__main__':
    unittest.main()