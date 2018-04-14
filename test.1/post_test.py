import unittest
from lib.post import post
import main
import json

class Testpost(unittest.TestCase):

    def test_post_callable(self):
        """Debe definir una funcion post"""
        self.assertTrue(callable(post))
    def test_post_200(self):
        """Debe regresar 200 cuando el objeto es creado"""
        body, code = post('test', {"data": "paraGuardar"})
        print 'test ', body, code
        self.assertTrue(code == 200)
        self.assertTrue(body)
if __name__ == '__main__':
    unittest.main()