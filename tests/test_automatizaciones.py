import unittest
from automatizaciones import Automatizaciones

class TestAutomatizaciones(unittest.TestCase):

    def setUp(self):
        self.dispositivos = [{"tipo": 1, "estado": True}, {"tipo" : 2, "estado": True}, {"tipo": 3, "estado": True}]
        self.auto = Automatizaciones(self.dispositivos)

    def test_consultar_automatizaciones_activas(self):
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: On")

    def test_consultar_automatizaciones_apagadas(self):
        dispositivos = self.auto.get_dispositivos()
        for dispositivo in dispositivos:
            dispositivo["estado"] = False
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: Off")

    def test_fiestaoff_nocheon(self):
        dispositivos = self.auto.get_dispositivos()
        dispositivos[1]["estado"] = False
        dispositivos[2]["estado"] = False
        
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: On")
    
    def test_fiestaon_nocheoff(self):
        dispositivos = self.auto.get_dispositivos()
        dispositivos[0]["estado"] = False

        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: Off")

    def test_activar_modo_fiesta(self):
        dispositivos = self.auto.get_dispositivos()
        dispositivos[1]["estado"] = False
        dispositivos[2]["estado"] = False

        mensaje = self.auto.activar_modo_fiesta()
        self.assertEqual(mensaje, "Modo Fiesta activado: Equipo de Musica y Luces encendidas.")
        self.assertTrue(self.dispositivos[1]["estado"])
        self.assertTrue(self.dispositivos[2]["estado"])

    def test_apagar_modo_fiesta(self):
        dispositivos = self.auto.get_dispositivos()
        dispositivos[1]["estado"] = True
        dispositivos[2]["estado"] = True

        mensaje = self.auto.apagar_modo_fiesta()
        self.assertEqual(mensaje, "Modo fiesta desactivado: Equipo de Musica y Luces apagadas.")
        self.assertFalse(self.dispositivos[1]["estado"])
        self.assertFalse(self.dispositivos[2]["estado"])

    def test_configurar_hora_valida(self):
        self.auto.set_hora_activacion_modo_noche(22)
        self.assertEqual(self.auto.get_hora_activacion_modo_noche(), 22)

if __name__ == "__main__":
    unittest.main()