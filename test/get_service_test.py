import unittest
import main
import json

class TestGet(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_get(self):
        """Debe de regresar el objeto guardado en la base de datas"""
        headers = {"Content-Type": "application/json" }
        result = self.app.get('/testParaObtener', query_string={"id":0}, headers=headers)
        self.assertEqual(result.status_code, 200)
        data = result.data
        print 'data ', data
        self.assertTrue(len(data))



if __name__ == '__main__':
    unittest.main()