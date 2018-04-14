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

if __name__ == '__main__':
    unittest.main()