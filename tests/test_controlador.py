import unittest
from dispositivo import Dispositivo, ControladorDispositivos

class TestControladorDispositivos(unittest.TestCase):

    def setUp(self):
        self.controlador = ControladorDispositivos()
        print("\nIniciando prueba...")

    def test_agregar_dispositivo(self):
        resultado = self.controlador.agregar_dispositivo("Luz Sala", Dispositivo.TIPO_LUZ, False)
        self.assertTrue(resultado)
        self.assertIsNotNone(self.controlador.buscar_por_nombre("Luz Sala"))

    def test_no_agregar_dispositivo_duplicado(self):
        self.controlador.agregar_dispositivo("Luz Sala", Dispositivo.TIPO_LUZ, False)
        resultado = self.controlador.agregar_dispositivo("Luz Sala", Dispositivo.TIPO_LUZ, True)
        self.assertFalse(resultado) # Debe devolver False al intentar agregar un duplicado

    def test_buscar_dispositivo_existente(self):
        self.controlador.agregar_dispositivo("Cámara Entrada", Dispositivo.TIPO_CAMARA, True)
        dispositivo = self.controlador.buscar_por_nombre("Cámara Entrada")
        self.assertIsNotNone(dispositivo)
        self.assertIsInstance(dispositivo, Dispositivo)
        self.assertEqual(dispositivo.nombre, "Cámara Entrada")

    def test_buscar_dispositivo_inexistente(self):
        dispositivo = self.controlador.buscar_por_nombre("Dispositivo Fantasma")
        self.assertIsNone(dispositivo)

    def test_eliminar_dispositivo(self):
        self.controlador.agregar_dispositivo("Música Patio", Dispositivo.TIPO_MUSICA, True)
        resultado = self.controlador.eliminar_dispositivo("Música Patio")
        self.assertTrue(resultado)
        self.assertIsNone(self.controlador.buscar_por_nombre("Música Patio"))
        
    def test_eliminar_dispositivo_inexistente(self):
        resultado = self.controlador.eliminar_dispositivo("Dispositivo Fantasma")
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()