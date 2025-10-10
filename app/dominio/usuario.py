from enum import Enum

class Rol(Enum):
    USUARIO = 1
    ADMIN = 2
    DUENIO = 3

class Usuario:
    # Lista estática que simula ser una base de datos
    usuarios = []

    def __init__(self, id_usuario, nombre, apellido, email, rol: Rol, contrasenia):
        self.__id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__rol = rol
        self._contrasenia = contrasenia

    def buscar_por_email(self, email):
        for usuario in self.usuarios:
            if usuario.__email == email:
                return usuario
        return None

    def registrar_usuario(self, id_usuario: str, nombre: str, apellido: str, email: str, rol: Rol, contraseña: str):
        if self.buscar_por_email(email):
            raise ValueError("El usuario con ese email ya existe")
        nuevo_usuario = Usuario(id_usuario, nombre, apellido, email, rol, contraseña)
        self.usuarios.append(nuevo_usuario)
        return nuevo_usuario

    def iniciar_sesion(self, email, contrasenia):
        credenciales_correctas = self.__email == email and self._contrasenia == contrasenia
        return credenciales_correctas

    def consultar_datos_personales(self):
        return f'''
            -> id_usuario: {self.__id_usuario}
            -> nombre: {self.__nombre}
            -> apellido: {self.__apellido}
            -> email: {self.__email}
            -> rol: {self.__rol}
        '''

    def modificar_rol_usuario(self, nuevo_rol: int):
        try:
            self.__rol = Rol(nuevo_rol)
        except ValueError:
            raise ValueError(f"Rol invalido: {nuevo_rol}")
        return self.__rol