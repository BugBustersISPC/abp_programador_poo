import mysql.connector 
from mysql.connector import errorcode
from app.dominio.usuario import Usuario
from app.conn.db_connection import DBConn
from app.dao.interfaces.i_usuario_dao import InterfaceUsuario

class UsuarioDAO(InterfaceUsuario):
    
    def __init__(self, db_connection: DBConn):
        self.db_connection = db_connection

    def get_by_email(self, email: str) -> Usuario:
        conexion = self.db_connection.connect_to_mysql()

        try:
            cursor = conexion.cursor()
            query = f'SELECT * FROM Usuario WHERE Email = "{email}"'
            cursor.execute(query)

            user = Usuario.from_object(cursor.fetchone())

            return user
        except mysql.connector.Error as err:
            raise f'Error al buscar por email, {err}'
        finally:
            conexion.close()

    def get_all(self) -> list[Usuario]:
        conexion = self.db_connection.connect_to_mysql()

        try:
            cursor = conexion.cursor()
            query = f'SELECT * FROM Usuario'
            cursor.execute(query)

            users = Usuario.from_list(cursor.fetchall())

            return users
        except mysql.connector.Error as err:
            raise f'Error al obtener todos los elementos, {err}'
        finally:
            conexion.close()

    def create(self, object: dict) -> int:
        conexion = self.db_connection.connect_to_mysql()

        try:
            cursor = conexion.cursor()
            query = f'''INSERT INTO Usuario (Nombre, Apellido, Email, Nombre_rol, Contrasenia)
                        VALUES (%s, %s, %s, %s, %s)'''
            cursor.execute(query, (object['nombre'], object['apellido'], object['email'], object['rol'], object['contrasenia']))
            id_fila = cursor.lastrowid
            conexion.commit()

            return id_fila
        except mysql.connector.Error as err:
            raise f'Error al insertar: {err}'
        finally:
            conexion.close()

    def update(self, id: int, object: dict):
        conexion = self.db_connection.connect_to_mysql()

        try:
            cursor = conexion.cursor()
            query = f'''UPDATE Usuario SET Nombre=%s, Apellido=%s, Email=%s, Nombre_rol=%s, Contrasenia=%s WHERE ID_usuario = %s'''
            cursor.execute(query, (object['nombre'], object['apellido'], object['email'], object['rol'], object['contrasenia'], id))
            id_fila = cursor.lastrowid
            conexion.commit()

            return id_fila
        except mysql.connector.Error as err:
            raise f'Error al modificar: {err}'
        finally:
            conexion.close()


    def delete_by_id(self, id: int):
        conexion = self.db_connection.connect_to_mysql()

        try:
            cursor = conexion.cursor()

            # Eliminar todas las entradas de la tabla intermedia usuario_vivienda
            query_usuario_vivienda = 'DELETE FROM usuario_vivienda WHERE ID_usuario=%s'
            cursor.execute(query_usuario_vivienda, (id,))

            # Ahora si se puede eliminar el usuario
            query_usuario = 'DELETE FROM Usuario WHERE ID_usuario=%s'
            cursor.execute(query_usuario, (id,))
            filas_eliminadas = cursor.rowcount
            conexion.commit()

            return filas_eliminadas
        except mysql.connector.Error as err:
            raise f'Error al eliminar: {err}'
        finally:
            conexion.close()