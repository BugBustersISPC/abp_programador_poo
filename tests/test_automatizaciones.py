import pytest
from unittest.mock import MagicMock
from app.dominio.automatizaciones import Automatizaciones
from app.dominio.dispositivo import Dispositivo


@pytest.fixture
def mock_daos():
    """Crea mocks de los DAOs para evitar conexión a la base de datos."""
    mock_auto_dao = MagicMock()
    mock_disp_dao = MagicMock()

    return mock_auto_dao, mock_disp_dao

@pytest.fixture
def setup_automatizaciones(mock_daos):
    """Crea un entorno de prueba con dispositivos y mocks."""
    mock_auto_dao, mock_disp_dao = mock_daos
    camara = Dispositivo("Camara Entrada", Dispositivo.TIPO_CAMARA, True)
    luz = Dispositivo("Luz Living", Dispositivo.TIPO_LUZ, True)
    musica = Dispositivo("Equipo Musica Living", Dispositivo.TIPO_MUSICA, True)
    auto = Automatizaciones([camara, luz, musica], mock_auto_dao, mock_disp_dao)
    return auto, camara, luz, musica


def test_consultar_automatizaciones_activas(setup_automatizaciones):
    auto, _, _, _ = setup_automatizaciones
    resultado = auto.mostrar_estado()
    assert resultado == "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: On"


def test_consultar_automatizaciones_apagadas(setup_automatizaciones):
    auto, camara, luz, musica = setup_automatizaciones
    camara.apagar()
    luz.apagar()
    musica.apagar()
    resultado = auto.mostrar_estado()
    assert resultado == "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: Off"


def test_fiestaoff_nocheon(setup_automatizaciones):
    auto, _, luz, musica = setup_automatizaciones
    luz.apagar()
    musica.apagar()
    resultado = auto.mostrar_estado()
    assert resultado == "Estado de Automatizaciones: - Modo Fiesta: Off / - Modo Noche: On"


def test_fiestaon_nocheoff(setup_automatizaciones):
    auto, camara, _, _ = setup_automatizaciones
    camara.apagar()
    resultado = auto.mostrar_estado()
    assert resultado == "Estado de Automatizaciones: - Modo Fiesta: On / - Modo Noche: Off"


def test_activar_modo_fiesta(setup_automatizaciones):
    auto, _, luz, musica = setup_automatizaciones
    luz.apagar()
    musica.apagar()
    mensaje = auto.activar_modo_fiesta()
    assert mensaje == "Modo Fiesta activado: Equipo de Musica y Luces encendidas."
    assert luz.estado is True
    assert musica.estado is True


def test_apagar_modo_fiesta(setup_automatizaciones):
    auto, _, luz, musica = setup_automatizaciones
    mensaje = auto.apagar_modo_fiesta()
    assert mensaje == "Modo fiesta desactivado: Equipo de Musica y Luces apagadas."
    assert luz.estado is False
    assert musica.estado is False


def test_configurar_hora_valida(setup_automatizaciones):
    auto, _, _, _ = setup_automatizaciones
    auto.set_hora_activacion_modo_noche(22)
    assert auto.get_hora_activacion_modo_noche() == 22