import pytest
from unittest.mock import create_autospec
from app.dominio.dispositivo import Dispositivo, ControladorDispositivos
from app.dao.interfaces.i_dispositivo_dao import IDispositivoDAO

@pytest.fixture
def dao_mock():
    
    #mock del DAO con la misma interfaz que IDispositivoDAO
    #lo inyectamos en el Controlador para aislarlo de la bdd
    return create_autospec(IDispositivoDAO, instance=True)

@pytest.fixture
def controlador(dao_mock):
    #creamos un ControladorDispositivos con el DAO mockeado
    return ControladorDispositivos(dao_mock)

def _row(nombre: str, tipo_enum: str, estado_bool: bool, id_disp: int = 1):
    #con esto generamos un 'registro' como dict, igual a lo que devuelve el DAO real
    return {
        "ID_dispositivo": id_disp,
        "Nombre": nombre,
        "Marca": None,
        "Modelo": None,
        "Tipo": tipo_enum,        # 'LUZ' 'CAMARA' 'MUSICA'
        "Estado": int(bool(estado_bool)),
        "ID_usuario": 1,
        "ID_ubicacion": 1,
        "ID_automatizacion": None,
    }

def test_agregar_dispositivo(controlador, dao_mock):
    # no existe duplicado por nombre
    dao_mock.find_by_nombre.return_value = []
    # lo que hace create() es q devuelve un ID nuevo
    dao_mock.create.return_value = 123

    ok = controlador.agregar_dispositivo(
        nombre="Luz Sala",
        tipo=Dispositivo.TIPO_LUZ,
        estado=False,
        id_usuario=1,
        id_ubicacion=2
    )
    assert ok is True
    # nos fijamos que haya llamado a create con los campos correctos
    dao_mock.create.assert_called_once()
    sent = dao_mock.create.call_args.kwargs or dao_mock.create.call_args.args[0]

    assert sent["Nombre"] == "Luz Sala"
    assert sent["Tipo"] == "LUZ"
    assert sent["Estado"] in (0, False)

    # y acá simulamos que ya existe para que buscar devuelva algo
    dao_mock.find_by_nombre.return_value = [_row("Luz Sala", "LUZ", False, 123)]
    d = controlador.buscar_por_nombre("Luz Sala")
    assert isinstance(d, Dispositivo)
    assert d.nombre == "Luz Sala"
    assert d.tipo == Dispositivo.TIPO_LUZ
    assert d.estado is False

def test_no_agregar_dispositivo_duplicado(controlador, dao_mock):
    # simulo que ya existe un dispositivo con ese nombre
    dao_mock.find_by_nombre.return_value = [_row("Luz Sala", "LUZ", False, 10)]

    ok = controlador.agregar_dispositivo(
        nombre="Luz Sala",
        tipo=Dispositivo.TIPO_LUZ,
        estado=True,
        id_usuario=1,
        id_ubicacion=2
    )
    assert ok is False
    dao_mock.create.assert_not_called()

def test_buscar_dispositivo_existente(controlador, dao_mock):
    dao_mock.find_by_nombre.return_value = [_row("Cámara Entrada", "CAMARA", True, 7)]
    disp = controlador.buscar_por_nombre("Cámara Entrada")
    assert disp is not None
    assert isinstance(disp, Dispositivo)
    assert disp.nombre == "Cámara Entrada"
    assert disp.tipo == Dispositivo.TIPO_CAMARA
    assert disp.estado is True

def test_buscar_dispositivo_inexistente(controlador, dao_mock):
    dao_mock.find_by_nombre.return_value = []
    disp = controlador.buscar_por_nombre("Dispositivo Fantasma")
    assert disp is None

def test_eliminar_dispositivo(controlador, dao_mock):
    # primero simula que lo encuentra
    dao_mock.find_by_nombre.return_value = [_row("Música Patio", "MUSICA", True, id_disp=55)]
    dao_mock.delete.return_value = True

    ok = controlador.eliminar_dispositivo("Música Patio")
    assert ok is True
    dao_mock.delete.assert_called_once_with(55)

    #  despues que ya no está
    dao_mock.find_by_nombre.return_value = []
    disp = controlador.buscar_por_nombre("Música Patio")
    assert disp is None

def test_eliminar_dispositivo_inexistente(controlador, dao_mock):
    dao_mock.find_by_nombre.return_value = []
    ok = controlador.eliminar_dispositivo("Dispositivo Fantasma")
    assert ok is False
    dao_mock.delete.assert_not_called()