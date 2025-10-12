import pytest
from enum import Enum
from app.dominio.usuario import Usuario, Rol

@pytest.fixture
def usuario_base():
    """Retorna una instancia de Usuario con valores conocidos."""
    return Usuario(
        id_usuario=101,
        nombre="Juan",
        apellido="Perez",
        email="juan.perez@test.com",
        rol=Rol.USUARIO,
        contrasenia="hashed_pass_123"
    )

@pytest.fixture
def usuario_db_data_tuple():
    """Retorna una tupla que simula un registro de la base de datos."""
    return (
        202, 
        "Ana", 
        "Gomez", 
        "ana.gomez@test.com", 
        Rol.ADMIN, 
        "hashed_pass_456"
    )

@pytest.fixture
def lista_db_data():
    """Retorna una lista de tuplas que simulan múltiples registros de la base de datos."""
    return [
        (303, "Luis", "Ruiz", "luis.ruiz@test.com", Rol.USUARIO, "pass_A"),
        (404, "Marta", "Vega", "marta.vega@test.com", Rol.ADMIN, "pass_B"),
    ]

def test_usuario_inicializacion_correcta(usuario_base):
    """Verifica que la instancia de Usuario se inicializa con los valores correctos."""
    assert usuario_base.id_usuario == 101
    # Accediendo a atributos privados a través del name mangling de Python
    assert usuario_base._Usuario__nombre == "Juan"
    assert usuario_base._Usuario__apellido == "Perez"
    assert usuario_base._Usuario__email == "juan.perez@test.com"
    assert usuario_base._Usuario__rol == Rol.USUARIO
    assert usuario_base._contrasenia == "hashed_pass_123"

def test_rol_es_un_enum(usuario_base):
    """Verifica que el rol se almacene como el objeto Enum Rol."""
    assert isinstance(usuario_base._Usuario__rol, Rol)
    assert usuario_base._Usuario__rol == Rol.USUARIO

def test_from_object_crea_usuario_correctamente(usuario_db_data_tuple):
    """Verifica la creación de un Usuario a partir de una tupla de datos."""
    usuario = Usuario.from_object(usuario_db_data_tuple)
    
    assert isinstance(usuario, Usuario)
    assert usuario.id_usuario == 202
    assert usuario._Usuario__nombre == "Ana"
    assert usuario._Usuario__rol == Rol.ADMIN

def test_to_object_retorna_diccionario_correcto(usuario_base):
    """Verifica que to_object retorna un diccionario con los valores correctos y rol.value."""
    objeto_diccionario = usuario_base.to_object()
    
    assert isinstance(objeto_diccionario, dict)
    assert objeto_diccionario['nombre'] == "Juan"
    assert objeto_diccionario['apellido'] == "Perez"
    assert objeto_diccionario['email'] == "juan.perez@test.com"
    assert objeto_diccionario['rol'] == "USUARIO"
    assert objeto_diccionario['contrasenia'] == "hashed_pass_123"
    assert 'id_usuario' not in objeto_diccionario

def test_from_list_retorna_lista_de_usuarios(lista_db_data):
    """Verifica que from_list convierte una lista de tuplas en una lista de objetos Usuario."""
    lista_usuarios = Usuario.from_list(lista_db_data)
    
    assert isinstance(lista_usuarios, list)
    assert len(lista_usuarios) == 2
    
    # Verificar el primer usuario
    usuario1 = lista_usuarios[0]
    assert isinstance(usuario1, Usuario)
    assert usuario1.id_usuario == 303
    assert usuario1._Usuario__nombre == "Luis"
    assert usuario1._Usuario__rol == Rol.USUARIO

    # Verificar el segundo usuario
    usuario2 = lista_usuarios[1]
    assert isinstance(usuario2, Usuario)
    assert usuario2.id_usuario == 404
    assert usuario2._Usuario__nombre == "Marta"
    assert usuario2._Usuario__rol == Rol.ADMIN

def test_str_contiene_informacion_clave(usuario_base):
    """Verifica que el método __str__ contiene los datos del usuario."""
    str_output = str(usuario_base)
    
    assert "id_usuario: 101" in str_output
    assert "nombre: Juan" in str_output
    assert "apellido: Perez" in str_output
    assert "rol: Rol.USUARIO" in str_output 
    assert "contrasenia" not in str_output