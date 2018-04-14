import unittest
import main
import json

class TestPut(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_put(self):
        """Debe de actualizar el objeto en la base de datos"""        
        headers = {"Content-Type": "application/json" }
        query = {"id":0}
        data = {'llave':'valorActualizado'}
        result = self.app.put('/testParaActualizar', query_string=query, headers=headers, data = json.dumps(data))
        self.assertEqual(result.status_code, 200)
        self.assertEqual(json.loads(result.data)["llave"], 'valorActualizado')
        self.assertEqual(None, 'valorActualizado')

    def test_put_400(self):
        """Debe de regresar 400 si el id es no enviado"""
        result = self.app.put('/testParaActualizar')
        self.assertEqual(result.status_code, 400)

    def test_put_404(self):
        """Debe de regresar 404 si el objeto no existe"""
        query = {"id":1}
        result = self.app.put('/testParaActualizar', query_string=query)
        self.assertEqual(result.status_code, 404)



if __name__ == '__main__':
    unittest.main()