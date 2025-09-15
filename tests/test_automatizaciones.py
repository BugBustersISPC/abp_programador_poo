import unittest
from automatizaciones import Automatizaciones
from dispositivo import Dispositivo

class TestAutomatizaciones(unittest.TestCase):

    def setUp(self):
        self.camara = Dispositivo("Camara Entrada", Dispositivo.TIPO_CAMARA, True)
        self.luz = Dispositivo("Luz Living", Dispositivo.TIPO_LUZ, True)
        self.musica = Dispositivo("Equipo Musica Living", Dispositivo.TIPO_MUSICA, True)
        self.auto = Automatizaciones([self.camara, self.luz, self.musica])

    def test_consultar_automatizaciones_activas(self):
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: On")

    def test_consultar_automatizaciones_apagadas(self):
        self.camara.apagar()
        self.luz.apagar()
        self.musica.apagar()

        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: Off")

    def test_fiestaoff_nocheon(self):
        self.luz.apagar()
        self.musica.apagar()
        
        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: On")
    
    def test_fiestaon_nocheoff(self):
        self.camara.apagar()

        resultado = self.auto.mostrar_estado()
        self.assertEqual(resultado, "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: Off")

    def test_activar_modo_fiesta(self):
        self.luz.apagar()
        self.musica.apagar()

        mensaje = self.auto.activar_modo_fiesta()
        self.assertEqual(mensaje, "Modo Fiesta activado: Equipo de Musica y Luces encendidas.")
        self.assertTrue(self.luz.estado)
        self.assertTrue(self.musica.estado)

    def test_apagar_modo_fiesta(self):
        mensaje = self.auto.apagar_modo_fiesta()
        self.assertEqual(mensaje, "Modo fiesta desactivado: Equipo de Musica y Luces apagadas.")
        self.assertFalse(self.luz.estado)
        self.assertFalse(self.musica.estado)

    def test_configurar_hora_valida(self):
        self.auto.set_hora_activacion_modo_noche(22)
        self.assertEqual(self.auto.get_hora_activacion_modo_noche(), 22)

if __name__ == "__main__":
    unittest.main()