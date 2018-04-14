import unittest
from lib.get import get
import main
import json

class Testget(unittest.TestCase):

    def test_get_callable(self):
        """Debe definir una funcion get"""
        self.assertTrue(callable(get))

    def test_get_404(self):
        """Debe regresar 404 si objeto con id dado no existe"""
        body, code = get('test', {"id":"idParaProbarGetQueNoExiste"})
        self.assertTrue(code == 404)
    def test_get_200(self):
        """Debe regresar 200 si objeto existe"""
        body, code = get('test', {"id":"idQueSiExiste"})
        self.assertTrue(code == 200)
    def test_get_400(self):
        """Debe regresar 400 si  no se envia el id"""
        body, code = get('test', {})
        self.assertTrue(code == 400)

if __name__ == '__main__':
    unittest.main()