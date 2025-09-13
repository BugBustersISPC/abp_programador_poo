import unittest
from automatizaciones import Automatizaciones

class TestAutomatizaciones(unittest.TestCase):

    def setUp(self):
        self.dispositivos = [{"tipo": 1, "estado": True}]
        self.auto = Automatizaciones(self.dispositivos)

    def test_consultar_automatizaciones_activas(self):
        resultado = self.auto.consultar_automatizaciones()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo: On")
    
    def test_consultar_automatizaciones_apagadas(self):
        self.dispositivos[0]["estado"] = False
        resultado = self.auto.consultar_automatizaciones()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo: Off")
    
    def test_activar_modo(self):
        mensaje = self.auto.activar_modo()
        self.assertEqual(mensaje, "Modo activado")
        self.assertTrue(self.dispositivos[0]["estado"])

    def test_apagar_modo(self):
        mensaje = self.auto.apagar_modo()
        self.assertEqual(mensaje, "Modo apagado")
        self.assertFalse(self.dispositivos[0]["estado"])

if __name__ == "__main__":
    unittest.main()