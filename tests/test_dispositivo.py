import pytest
from dispositivo import Dispositivo

def test_creacion_dispositivo_valido():
    dispositivo = Dispositivo(nombre="Luz Living", tipo=Dispositivo.TIPO_LUZ, estado=False)
    assert dispositivo.nombre == "Luz Living"
    assert dispositivo.tipo == 2
    assert dispositivo.estado is False

def test_creacion_falla_por_nombre_vacio():
    with pytest.raises(ValueError):
        Dispositivo(nombre="", tipo=Dispositivo.TIPO_LUZ, estado=True)

def test_creacion_falla_por_tipo_invalido():
    with pytest.raises(ValueError):
        Dispositivo(nombre="Dispositivo Raro", tipo=99, estado=True)

def test_cambiar_estado():
    dispositivo = Dispositivo(nombre="Cámara Jardín", tipo=Dispositivo.TIPO_CAMARA, estado=False)
    assert dispositivo.estado is False

    #probamos encender
    dispositivo.encender()
    assert dispositivo.estado is True

    #probamos apagar
    dispositivo.apagar()
    assert dispositivo.estado is False

def test_falla_al_cambiar_estado_con_valor_no_booleano():
    dispositivo = Dispositivo(nombre="Parlante", tipo=Dispositivo.TIPO_MUSICA, estado=True)
    with pytest.raises(ValueError):
        dispositivo.estado = "apagado"

def test_representacion_string():
    disp_on = Dispositivo("Luz RGB", Dispositivo.TIPO_LUZ, True)
    disp_off = Dispositivo("Alarma", Dispositivo.TIPO_CAMARA, False)

    assert str(disp_on) == "Luz RGB (Tipo: Luz) - Estado: On"
    assert str(disp_off) == "Alarma (Tipo: Cámara) - Estado: Off"
