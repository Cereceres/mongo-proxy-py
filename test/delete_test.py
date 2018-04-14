import unittest
from lib.delete import delete
import main
import json

class TestDelete(unittest.TestCase):

    def test_delete_callable(self):
        """Debe definir una funcion delete"""
        self.assertTrue(callable(delete))
    def test_delete_200(self):
        """Debe regresar 200 si objeto existe"""
        body, code = delete('test', {"id":"idQueSiExiste"})
        self.assertTrue(code == 200)

if __name__ == '__main__':
    unittest.main()