from app.dominio.ubicacion import Ubicacion

def test_creacion_de_ubicacion():
    """Prueba que una Ubicacion se crea con los valores iniciales correctos."""
    ubicacion = Ubicacion("Baño", id_vivienda=1)
    assert ubicacion.nombre == "Baño"
    assert ubicacion.id_vivienda == 1
    assert ubicacion.obtener_dispositivos() == []
    assert isinstance(ubicacion.id, int)

def test_ids_son_unicos_y_autoincrementales():
    """Prueba que cada nueva ubicación obtiene un ID consecutivo."""
    Ubicacion._contador_id = 0
    ubicacion1 = Ubicacion("Cocina", id_vivienda=1)
    ubicacion2 = Ubicacion("Dormitorio", id_vivienda=1)
    assert ubicacion1.id == 1
    assert ubicacion2.id == 2
    assert ubicacion2.id > ubicacion1.id

def test_agregar_un_dispositivo():
    """Prueba que podemos agregar un dispositivo a una ubicación."""
    ubicacion = Ubicacion("Living", id_vivienda=1)
    resultado = ubicacion.agregar_dispositivo("Televisor")
    assert resultado is True
    assert "Televisor" in ubicacion.obtener_dispositivos()

def test_no_agregar_dispositivos_duplicados():
    """Prueba que no se puede agregar el mismo dispositivo dos veces."""
    ubicacion = Ubicacion("Garaje", id_vivienda=1)
    ubicacion.agregar_dispositivo("Bicicleta")
    resultado = ubicacion.agregar_dispositivo("Bicicleta")
    assert resultado is False
    assert len(ubicacion.obtener_dispositivos()) == 1
    assert ubicacion.obtener_dispositivos() == ["Bicicleta"]

def test_no_agregar_dispositivo_vacio():
    """Prueba que no se pueden agregar dispositivos con nombre vacío."""
    ubicacion = Ubicacion("Patio", id_vivienda=1)
    resultado = ubicacion.agregar_dispositivo("")
    assert resultado is False
    assert len(ubicacion.obtener_dispositivos()) == 0

def test_ubicacion_con_id_desde_base_datos():
    """Prueba que podemos crear una ubicación con ID existente (desde BD)."""
    ubicacion = Ubicacion("Cocina", id_vivienda=1, id_ubicacion=100)
    assert ubicacion.id == 100
    assert ubicacion.nombre == "Cocina"
    assert ubicacion.id_vivienda == 1