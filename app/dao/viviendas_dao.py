import mysql.connector
from app.dao.interfaces.i_viviendas_dao import IViviendasDAO
from app.dominio.viviendas import Vivienda
from app.conn.db_connection import DBConn

class ViviendasDAO(IViviendasDAO):
    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn

    def get(self, id_vivienda: int):
        conn = self.db_conn.connect_to_mysql()
        try:
            with conn.cursor() as cursor:
                query = "SELECT ID_vivienda, Nombre, Direccion FROM vivienda WHERE ID_vivienda = %s;"
                cursor.execute(query, (id_vivienda,))
                row = cursor.fetchone()

                if row:
                    vivienda = Vivienda(nombre=row[1], direccion=row[2])
                    vivienda._id_vivienda = row[0]
                    return vivienda
                return None
        except mysql.connector.Error as err:
            print(f"Error al obtener vivienda: {err}")
            return None

    def get_all(self):
        viviendas = []
        conn = self.db_conn.connect_to_mysql()
        try:
            with conn.cursor() as cursor:
                query = "SELECT ID_vivienda, Nombre, Direccion FROM vivienda;"
                cursor.execute(query)
                rows = cursor.fetchall()

                for row in rows:
                    vivienda = Vivienda(nombre=row[1], direccion=row[2])
                    vivienda._id_vivienda = row[0]
                    viviendas.append(vivienda)
            return viviendas
        except mysql.connector.Error as err:
            print(f"Error al listar viviendas: {err}")
            return []

    def create(self, vivienda: Vivienda):
        conn = self.db_conn.connect_to_mysql()
        try:
            with conn.cursor() as cursor:
                query = "INSERT INTO vivienda (Nombre, Direccion) VALUES (%s, %s);"
                values = (vivienda.get_nombre(), vivienda.get_direccion())
                cursor.execute(query, values)
                conn.commit()
                vivienda._id_vivienda = cursor.lastrowid
                return vivienda
        except mysql.connector.Error as err:
            print(f"Error al crear vivienda: {err}")
            conn.rollback()
            return None

    def update(self, vivienda: Vivienda):
        conn = self.db_conn.connect_to_mysql()
        try:
            with conn.cursor() as cursor:
                query = "UPDATE vivienda SET Nombre = %s, Direccion = %s WHERE ID_vivienda = %s;"
                values = (vivienda.get_nombre(), vivienda.get_direccion(), vivienda.get_id())
                cursor.execute(query, values)
                conn.commit()
                return vivienda
        except mysql.connector.Error as err:
            print(f"Error al actualizar vivienda: {err}")
            conn.rollback()
            return None

    def delete(self, id_vivienda: int):
        conn = self.db_conn.connect_to_mysql()
        try:
            with conn.cursor() as cursor:
                query = "DELETE FROM vivienda WHERE ID_vivienda = %s;"
                cursor.execute(query, (id_vivienda,))
                conn.commit()
                return True
        except mysql.connector.Error as err:
            print(f"Error al eliminar vivienda: {err}")
            conn.rollback()
            return False