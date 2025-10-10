from app.dominio.automatizaciones import Automatizaciones
from app.dominio.dispositivo import Dispositivo

class TestAutomatizaciones:
    def setup_method(self):
        self.camara = Dispositivo("Camara Entrada", Dispositivo.TIPO_CAMARA, True)
        self.luz = Dispositivo("Luz Living", Dispositivo.TIPO_LUZ, True)
        self.musica = Dispositivo("Equipo Musica Living", Dispositivo.TIPO_MUSICA, True)
        self.auto = Automatizaciones([self.camara, self.luz, self.musica])

    def test_consultar_automatizaciones_activas(self):
        resultado = self.auto.mostrar_estado()
        assert resultado == "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: On"

    def test_consultar_automatizaciones_apagadas(self):
        self.camara.apagar()
        self.luz.apagar()
        self.musica.apagar()
        resultado = self.auto.mostrar_estado()
        assert resultado == "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: Off"

    def test_fiestaoff_nocheon(self):
        self.luz.apagar()
        self.musica.apagar()
        resultado = self.auto.mostrar_estado()
        assert resultado == "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: On"

    def test_fiestaon_nocheoff(self):
        self.camara.apagar()
        resultado = self.auto.mostrar_estado()
        assert resultado == "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: Off"

    def test_activar_modo_fiesta(self):
        self.luz.apagar()
        self.musica.apagar()
        mensaje = self.auto.activar_modo_fiesta()
        assert mensaje == "Modo Fiesta activado: Equipo de Musica y Luces encendidas."
        assert self.luz.estado is True
        assert self.musica.estado is True

    def test_apagar_modo_fiesta(self):
        mensaje = self.auto.apagar_modo_fiesta()
        assert mensaje == "Modo fiesta desactivado: Equipo de Musica y Luces apagadas."
        assert self.luz.estado is False
        assert self.musica.estado is False

    def test_configurar_hora_valida(self):
        self.auto.set_hora_activacion_modo_noche(22)
        assert self.auto.get_hora_activacion_modo_noche() == 22