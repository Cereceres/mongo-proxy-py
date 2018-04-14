import unittest
import main
import json

class TestGet(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_get(self):
        """Debe de regresar el objeto guardado en la base de datos"""
        headers = {"Content-Type": "application/json" }
        result = self.app.get('/testParaObtener', query_string={"id":0}, headers=headers)
        self.assertEqual(result.status_code, 200)
        data = result.data
        self.assertEqual(0, 'valor')

    def test_get_400(self):
        """Debe de regresar 400 si el id es no enviado"""        
        result = self.app.get('/testParaObtener')
        self.assertEqual(result.status_code, 400)

    def test_get_404(self):
        """Debe de regresar 404 si el objero no existe"""                
        query = {"id":1}
        result = self.app.get('/testParaObtener', query_string=query)
        self.assertEqual(result.status_code, 404)



if __name__ == '__main__':
    unittest.main()