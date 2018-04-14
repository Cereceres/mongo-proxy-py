import unittest
from lib.get import get
import main
import json

class Testget(unittest.TestCase):

    def test_get_callable(self):
        """Debe definir una funcion get"""
        self.assertTrue(callable(get))
    def test_get_200(self):
        """Debe regresar 200 si objeto existe"""
        body, code = get('test', {"id":"idQueSiExiste"})
        self.assertTrue(code == 200)

if __name__ == '__main__':
    unittest.main()