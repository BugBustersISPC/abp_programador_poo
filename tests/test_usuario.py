import pytest
from app.dominio.usuario import Usuario, Rol

@pytest.fixture
def usuario_normal():
    return Usuario(
        id_usuario=1,
        nombre="Juan",
        apellido="Pérez",
        email="juan.perez@ejemplo.com",
        rol=Rol.USUARIO,
        contrasenia="password123"
    )

@pytest.fixture
def usuario_admin():
    return Usuario(
        id_usuario=2,
        nombre="Ana",
        apellido="García",
        email="ana.garcia@ejemplo.com",
        rol=Rol.ADMIN,
        contrasenia="admin_secret"
    )

def test_usuario_creacion_correcta(usuario_normal):
    assert usuario_normal.id_usuario == 1
    assert usuario_normal._Usuario__nombre == "Juan"
    assert usuario_normal._Usuario__apellido == "Pérez"
    assert usuario_normal._Usuario__email == "juan.perez@ejemplo.com"
    assert usuario_normal._Usuario__rol == Rol.USUARIO
    assert usuario_normal._contrasenia == "password123"

def test_usuario_str(usuario_normal):
    representacion = str(usuario_normal)
    assert '-> id_usuario: 1' in representacion
    assert '-> nombre: Juan' in representacion
    assert '-> apellido: Pérez' in representacion
    assert '-> email: juan.perez@ejemplo.com' in representacion
    assert '-> rol: Rol.USUARIO' in representacion

def test_usuario_is_admin_false(usuario_normal):
    assert usuario_normal.is_admin() is False

def test_usuario_is_admin_true(usuario_admin):
    assert usuario_admin.is_admin() is True

def test_usuario_get_nombre_apellido(usuario_admin):
    resultado = usuario_admin.get_nombre_apellido()
    assert resultado == 'Ana García - ID: 2'
    assert 'Ana García' in resultado
    assert 'ID: 2' in resultado

def test_usuario_from_object_usuario():
    datos_usuario = [3, "Luis", "Gómez", "luis@ejemplo.com", "USUARIO", "secreto1"]
    usuario_creado = Usuario.from_object(datos_usuario)
    
    assert isinstance(usuario_creado, Usuario)
    assert usuario_creado.id_usuario == 3
    assert usuario_creado._Usuario__nombre == "Luis"
    assert usuario_creado._Usuario__rol == Rol.USUARIO

def test_usuario_from_object_admin():
    datos_admin = [4, "Carlos", "Sanz", "carlos@ejemplo.com", "ADMIN", "adminpass"]
    usuario_creado = Usuario.from_object(datos_admin)
    
    assert isinstance(usuario_creado, Usuario)
    assert usuario_creado.id_usuario == 4
    assert usuario_creado._Usuario__nombre == "Carlos"
    assert usuario_creado._Usuario__rol == Rol.ADMIN

def test_usuario_to_object(usuario_normal):
    objeto_dict = usuario_normal.to_object()
    
    assert isinstance(objeto_dict, dict)
    assert objeto_dict['nombre'] == 'Juan'
    assert objeto_dict['apellido'] == 'Pérez'
    assert objeto_dict['email'] == 'juan.perez@ejemplo.com'
    assert objeto_dict['rol'] == 'USUARIO'
    assert objeto_dict['contrasenia'] == 'password123'

def test_usuario_from_list():
    lista_datos = [
        (5, "Elena", "Vargas", "elena@ejemplo.com", "USUARIO", "pass1"),
        (6, "Marcos", "Rey", "marcos@ejemplo.com", "ADMIN", "pass2"),
    ]
    
    lista_usuarios = Usuario.from_list(lista_datos)
    
    assert isinstance(lista_usuarios, list)
    assert len(lista_usuarios) == 2
    
    # Usuario 1
    usuario1 = lista_usuarios[0]
    assert isinstance(usuario1, Usuario)
    assert usuario1.id_usuario == 5
    assert usuario1._Usuario__rol == Rol.USUARIO
    
    # Usuario 2
    usuario2 = lista_usuarios[1]
    assert isinstance(usuario2, Usuario)
    assert usuario2.id_usuario == 6
    assert usuario2._Usuario__rol == Rol.ADMIN