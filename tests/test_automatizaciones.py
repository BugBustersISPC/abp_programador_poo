import unittest
from automatizaciones import Automatizaciones

class TestAutomatizaciones(unittest.TestCase):

    def setUp(self):
        self.dispositivos = [{"tipo": 1, "estado": True}, {"tipo" : 2, "estado": True}, {"tipo": 3, "estado": True}]
        self.auto = Automatizaciones(self.dispositivos)
        self.estado_fiesta = Automatizaciones(self.estado_fiesta)

    def test_consultar_automatizaciones_activas(self):
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: On")

    def test_consultar_automatizaciones_apagadas(self):
        for dispositivo in self.dispositivos:
            dispositivo["estado"] = False
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: Off")

    
    
    def test_activar_modo(self):
        mensaje = self.auto.activar_modo_fiesta()
        self.assertEqual(mensaje, "Modo Fiesta activado: Equipo de Musica y Luces encendidas.")
        self.assertTrue(self.dispositivos[1]["estado"])
        self.assertTrue(self.dispositivos[2]["estado"])

    def test_apagar_modo(self):
        mensaje = self.auto.apagar_modo_fiesta()
        self.assertEqual(mensaje, "Modo fiesta desactivado: Equipo de Musica y Luces apagadas.")
        self.assertFalse(self.dispositivos[1]["estado"])
        self.assertFalse(self.dispositivos[2]["estado"])

    def test_configurar_hora_valida(self):
        self.assertTrue(self.auto.configurar_hora_modo_noche(22))
        self.assertEqual(self.auto.hora_activacion_modo_noche, 22)
if __name__ == "__main__":
    unittest.main()