import unittest
from lib.delete import delete
import main
import json

class TestDelete(unittest.TestCase):

    def test_delete_callable(self):
        """Debe definir una funcion delete"""
        self.assertTrue(callable(delete))

    def test_delete_404(self):
        """Debe regresar 404 si objeto con id dado no existe"""
        body, code = delete('test', {"id":"idParaProbarDelete"})
        self.assertTrue(code == 404)
    def test_delete_200(self):
        """Debe regresar 200 si objeto existe"""
        body, code = delete('test', {"id":"idQueSiExiste"})
        self.assertTrue(code == 200)
    def test_delete_400(self):
        """Debe regresar 400 si  no se envia el id"""
        body, code = delete('test', {})
        self.assertTrue(code == 400)

if __name__ == '__main__':
    unittest.main()