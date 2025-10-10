import pytest
from app.dominio.dispositivo import Dispositivo, ControladorDispositivos

@pytest.fixture
def controlador():
    """crea y devuelve una nueva instancia de ControladorDispositivos para cada prueba"""
    print("\nIniciando prueba...")
    return ControladorDispositivos()

def test_agregar_dispositivo(controlador):
    resultado = controlador.agregar_dispositivo("Luz Sala", Dispositivo.TIPO_LUZ, False)
    assert resultado is True
    assert controlador.buscar_por_nombre("Luz Sala") is not None

def test_no_agregar_dispositivo_duplicado(controlador):
    controlador.agregar_dispositivo("Luz Sala", Dispositivo.TIPO_LUZ, False)
    resultado = controlador.agregar_dispositivo("Luz Sala", Dispositivo.TIPO_LUZ, True)
    assert resultado is False  # Debe devolver False al intentar agregar un duplicado

def test_buscar_dispositivo_existente(controlador):
    controlador.agregar_dispositivo("Cámara Entrada", Dispositivo.TIPO_CAMARA, True)
    dispositivo = controlador.buscar_por_nombre("Cámara Entrada")
    assert dispositivo is not None
    assert isinstance(dispositivo, Dispositivo)
    assert dispositivo.nombre == "Cámara Entrada"

def test_buscar_dispositivo_inexistente(controlador):
    dispositivo = controlador.buscar_por_nombre("Dispositivo Fantasma")
    assert dispositivo is None

def test_eliminar_dispositivo(controlador):
    controlador.agregar_dispositivo("Música Patio", Dispositivo.TIPO_MUSICA, True)
    resultado = controlador.eliminar_dispositivo("Música Patio")
    assert resultado is True
    assert controlador.buscar_por_nombre("Música Patio") is None
    
def test_eliminar_dispositivo_inexistente(controlador):
    resultado = controlador.eliminar_dispositivo("Dispositivo Fantasma")
    assert resultado is False