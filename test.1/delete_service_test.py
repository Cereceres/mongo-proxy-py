import unittest
import main
import json

class TestDelete(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_delete(self):
        """Debe de remover el objeto guardado en la base de datos"""
        query = {"id":0}
        result = self.app.delete('/testParaDelete', query_string=query)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.data, 'ok')
        self.assertEqual(None, None)

    def test_delete_400(self):
        """Debe de regresar 400 si el id es no enviado"""
        result = self.app.delete('/testParaDelete')
        self.assertEqual(result.status_code, 400)

    def test_delete_404(self):
        """Debe 404 si el objeto no existe"""
        query = {"id":1}
        result = self.app.delete('/testParaDelete', query_string=query)
        self.assertEqual(result.status_code, 404)

if __name__ == '__main__':
    unittest.main()