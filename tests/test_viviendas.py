import pytest
from app.dominio.viviendas import Vivienda
from app.dominio.ubicacion import Ubicacion

# Fixture para reiniciar la clase antes de cada test
@pytest.fixture(autouse=True)
def reset_viviendas():
    Vivienda._viviendas.clear()
    Vivienda._contador_id = 1

# TEST 1: Constructor básico
def test_crear_vivienda():
    v = Vivienda("Mi Casa", "Calle 123")
    assert v.get_nombre() == "Mi Casa"
    assert v.get_direccion() == "Calle 123"
    assert v.get_id() == 1

# TEST 2: Validar nombre vacío
def test_nombre_vacio():
    with pytest.raises(ValueError):
        Vivienda("", "Calle 123")

# TEST 3: Validar dirección vacía
def test_direccion_vacia():
    with pytest.raises(ValueError):
        Vivienda("Mi Casa", "")

# TEST 4: Setters funcionan
def test_cambiar_nombre():
    v = Vivienda("Casa", "Calle")
    resultado = v.set_nombre("Nueva Casa")
    assert resultado
    assert v.get_nombre() == "Nueva Casa"

# TEST 5: Setters con valor vacío
def test_cambiar_nombre_vacio():
    v = Vivienda("Casa", "Calle")
    resultado = v.set_nombre("")
    assert not resultado
    assert v.get_nombre() == "Casa"

# TEST 6: Agregar ubicación
def test_agregar_ubicacion():
    v = Vivienda("Casa", "Calle")
    ub = Ubicacion("Sala")
    resultado = v.agregar_ubicacion(ub)
    assert resultado
    assert "Sala" in v.get_ubicaciones()

# TEST 7: No agregar ubicación duplicada
def test_ubicacion_duplicada():
    v = Vivienda("Casa", "Calle")
    ub = Ubicacion("Sala")
    v.agregar_ubicacion(ub)
    resultado = v.agregar_ubicacion(ub)
    assert not resultado
    assert len(v.get_ubicaciones()) == 1

# TEST 8: Obtener ubicación
def test_obtener_ubicacion():
    v = Vivienda("Casa", "Calle")
    ub = Ubicacion("Cocina")
    v.agregar_ubicacion(ub)
    encontrada = v.obtener_ubicacion("Cocina")
    assert encontrada is not None
    assert encontrada.nombre == "Cocina"

# TEST 9: Eliminar ubicación
def test_eliminar_ubicacion():
    v = Vivienda("Casa", "Calle")
    v.agregar_ubicacion(Ubicacion("Baño"))
    resultado = v.eliminar_ubicacion("Baño")
    assert resultado
    assert "Baño" not in v.get_ubicaciones()

# TEST 10: Buscar vivienda por nombre
def test_buscar_vivienda():
    v = Vivienda("Casa Verde", "Av. 456")
    encontrada = Vivienda.buscar_vivienda_por_nombre("Casa Verde")
    assert encontrada == v

# TEST 11: Eliminar vivienda
def test_eliminar_vivienda_si():
    Vivienda("Casa Roja", "Calle 789")
    resultado = Vivienda.eliminar_vivienda("Casa Roja", "si")
    assert "eliminada" in resultado
    assert Vivienda.buscar_vivienda_por_nombre("Casa Roja") is None

# TEST 12: No eliminar vivienda
def test_eliminar_vivienda_no():
    v = Vivienda("Casa Azul", "Calle 000")
    resultado = Vivienda.eliminar_vivienda("Casa Azul", "no")
    assert "cancelada" in resultado.lower()
    assert Vivienda.buscar_vivienda_por_nombre("Casa Azul") == v

# TEST 13: Listar viviendas
def test_listar_viviendas():
    v1 = Vivienda("Casa 1", "Dir 1")
    v2 = Vivienda("Casa 2", "Dir 2")
    v1.agregar_ubicacion(Ubicacion("Sala"))
    lista = Vivienda.listar_viviendas()
    assert len(lista) == 2
    assert lista[0]["nombre"] == "Casa 1"
    assert lista[0]["ubicaciones"] == ["Sala"]