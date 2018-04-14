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
        headers = {"Content-Type": "application/json" }
        query = {"key":"idQueSiExiste"}
        data = {"algunaValor": "updateAlgunValor"}
        response = self.app.put('/testParaActualizar', query_string=query, headers=headers, data=json.dumps(data))
        self.assertTrue(response.status_code == 200)
        object_saved = json.loads(response.get_data())
        self.assertTrue(object_saved)

    def test_put_not_exists(self):
        """Debe regresar 200 si objeto not existe y no lo actualiza"""
        headers = {"Content-Type": "application/json" }
        query = {"key":"idQueNoExiste"}
        data = {"algunaValor": "updateAlgunValor"}
        response = self.app.put('/testParaActualizar', query_string=query, headers=headers, data=json.dumps(data))
        self.assertTrue(response.status_code == 200)
        object_saved = json.loads(response.get_data())
        self.assertFalse(object_saved)



if __name__ == '__main__':
    unittest.main()