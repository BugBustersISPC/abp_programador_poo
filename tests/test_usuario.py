import pytest
from app.dominio.usuario import Usuario, Rol

@pytest.fixture(autouse=True)
def limpiar_usuarios():
    Usuario.usuarios = []
    yield

def test_registrar_usuario():
    usuario_manager = Usuario(None, "","","", None, "")
    nuevo_usuario = usuario_manager.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    assert nuevo_usuario is not None
    assert len(Usuario.usuarios) == 1
    assert Usuario.usuarios[0]._Usuario__email == "juan.perez@example.com"

def test_iniciar_sesion_credenciales_correctas():
    usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    assert usuario.iniciar_sesion("juan.perez@example.com", "password123") is True

def test_iniciar_sesion_credenciales_incorrectas():
    usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    assert usuario.iniciar_sesion("juan.perez@example.com", "pass_incorrecta") is False
    assert usuario.iniciar_sesion("email_incorrecto@example.com", "password123") is False

def test_modificar_rol_exitoso():
    usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    nuevo_rol = usuario.modificar_rol_usuario(Rol.ADMIN.value)
    assert nuevo_rol == Rol.ADMIN

def test_buscar_usuario_por_email_encontrado():
    usuario_db = Usuario(None, "","","", None, "")
    usuario_db.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    usuario_encontrado = usuario_db.buscar_por_email("juan.perez@example.com")
    assert usuario_encontrado is not None
    assert usuario_encontrado._Usuario__email == "juan.perez@example.com"

def test_buscar_usuario_por_email_no_encontrado():
    usuario_db = Usuario(None, "","","", None, "")
    usuario_db.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    usuario_no_encontrado = usuario_db.buscar_por_email("otro.email@example.com")
    assert usuario_no_encontrado is None

def test_consultar_datos_personales():
    usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
    datos = usuario.consultar_datos_personales()
    assert isinstance(datos, str)
    assert "Juan" in datos
    assert "juan.perez@example.com" in datos