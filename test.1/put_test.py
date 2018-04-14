import unittest
from lib.put import put
import main
import json

class Testput(unittest.TestCase):

    def test_put_callable(self):
        """Debe definir una funcion put"""
        self.assertTrue(callable(put))
    def test_put_200(self):
        """Debe regresar 200 si objeto existe y lo actualiza"""
        body, code = put('test', {"id":"idQueSiExiste"},{"algunaValor": "ConAlgunDatoActualizado"})
        self.assertTrue(code == 200)
        object_saved = json.loads(body)
        self.assertTrue(object_saved["algunaValor"] =="ConAlgunDatoActualizado" )
    def test_put_404(self):
        """Debe regresar 404 si objeto con id dado no existe"""
        body, code = put('test', {"id":"idParaProbarputQueNoExiste"})
        self.assertTrue(code == 404)
    def test_put_400(self):
        """Debe regresar 400 si  no se envia el id"""
        body, code = put('test', {})
        self.assertTrue(code == 400)
if __name__ == '__main__':
    unittest.main()