import unittest
import main
import json

class TestPost(unittest.TestCase):
    def setUp(self):
        self.app = main.app.test_client()
        self.app.testing = True

    def test_post(self):
        """Debe de create un objeto en la base de datos"""        
        data = {'llave':'valor'}
        headers = {"Content-Type": "application/json" }
        result = self.app.post('/testCrear', data=json.dumps(data), headers=headers)
        print 'result ', result
        self.assertEqual(result.status_code, 200)
        self.assertEqual(None, 'valor')



if __name__ == '__main__':
    unittest.main()