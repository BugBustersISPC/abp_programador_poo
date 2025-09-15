import unittest
from usuario import Usuario, Rol

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        # Por las dudas reseteo cualquier dato en nuestra base de datos ficticia
        Usuario.usuarios = []

    def test_registrar_usuario_exitoso(self):
        usuario = Usuario(None, "","","", None, "")
        nuevo_usuario = usuario.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        self.assertIsNotNone(nuevo_usuario)
        self.assertEqual(len(Usuario.usuarios), 1)
        self.assertEqual(Usuario.usuarios[0]._Usuario__email, "juan.perez@example.com")

    def test_registrar_usuario_existente(self):
        usuario = Usuario(None, "","","", None, "")
        usuario.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        with self.assertRaises(ValueError) as context:
            usuario.registrar_usuario("2", "Ana", "Gomez", "juan.perez@example.com", Rol.USUARIO, "pass456")
        self.assertIn("El usuario con ese email ya existe", str(context.exception))
        self.assertEqual(len(Usuario.usuarios), 1)

    def test_iniciar_sesion_credenciales_correctas(self):
        usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        self.assertTrue(usuario.iniciar_sesion("juan.perez@example.com", "password123"))

    def test_iniciar_sesion_credenciales_incorrectas(self):
        usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        self.assertFalse(usuario.iniciar_sesion("juan.perez@example.com", "pass_incorrecta"))
        self.assertFalse(usuario.iniciar_sesion("email_incorrecto@example.com", "password123"))
    
    def test_modificar_rol_exitoso(self):
        usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        nuevo_rol = usuario.modificar_rol_usuario(Rol.ADMIN.value)
        self.assertEqual(nuevo_rol, Rol.ADMIN)

    def test_modificar_rol_invalido(self):
        usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        with self.assertRaises(ValueError) as context:
            usuario.modificar_rol_usuario(99)  # 99 no es un valor válido para el enum Rol
        self.assertIn("Rol invalido: 99", str(context.exception))
    
    def test_buscar_usuario_por_email_encontrado(self):
        usuario_db = Usuario(None, "","","", None, "")
        usuario_db.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        usuario_encontrado = usuario_db.buscar_por_email("juan.perez@example.com")
        self.assertIsNotNone(usuario_encontrado)
        self.assertEqual(usuario_encontrado._Usuario__email, "juan.perez@example.com")

    def test_buscar_usuario_por_email_no_encontrado(self):
        usuario_db = Usuario(None, "","","", None, "")
        usuario_db.registrar_usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        usuario_no_encontrado = usuario_db.buscar_por_email("otro.email@example.com")
        self.assertIsNone(usuario_no_encontrado)
    
    def test_consultar_datos_personales(self):
        usuario = Usuario("1", "Juan", "Perez", "juan.perez@example.com", Rol.USUARIO, "password123")
        datos = usuario.consultar_datos_personales()
        self.assertIsInstance(datos, str)
        self.assertIn("Juan", datos)
        self.assertIn("juan.perez@example.com", datos)