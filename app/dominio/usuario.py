from enum import Enum

class Rol(Enum):
    USUARIO = 'USUARIO'
    ADMIN = 'ADMIN'

class Usuario:

    def __init__(self, id_usuario, nombre, apellido, email, rol: Rol, contrasenia):
        self.id_usuario = id_usuario
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__rol = rol
        self._contrasenia = contrasenia

    def __str__(self):
        return f'''
            -> id_usuario: {self.id_usuario}
            -> nombre: {self.__nombre}
            -> apellido: {self.__apellido}
            -> email: {self.__email}
            -> rol: {self.__rol}
        '''
    
    def from_object(objeto):
        usuario = Usuario(
            id_usuario=objeto[0],
            nombre=objeto[1],
            apellido=objeto[2],
            email=objeto[3],
            rol=objeto[4],
            contrasenia=objeto[5],
        )

        return usuario
    
    def to_object(self):
        return {
            'nombre': self.__nombre,
            'apellido': self.__apellido,
            'email': self.__email,
            'rol': self.__rol.value,
            'contrasenia': self._contrasenia,
        }
    
    def from_list(lista):
        lista_usuarios = []

        for i in lista:
            usuario = Usuario(
                id_usuario=i[0],
                nombre=i[1],
                apellido=i[2],
                email=i[3],
                rol=i[4],
                contrasenia=i[5],
            )

            lista_usuarios.append(usuario)

        return lista_usuarios