import mysql.connector
from typing import List, Dict, Any
from app.dao.interfaces.i_automatizaciones_dao import IAutomatizacionDAO
from app.conn.db_connection import DBConn


class AutomatizacionDAO(IAutomatizacionDAO):

    def __init__(self, db_conn: DBConn):
        self.db_conn = db_conn
        self.db_name = db_conn.db_config.get("database")


    def get(self, id_automatizacion: int):
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor(dictionary=True) as cursor:
                query = f"SELECT ID_automatizacion, Accion, Estado FROM {self.db_name}.Automatizacion WHERE ID_automatizacion = %s"
                cursor.execute(query, (id_automatizacion,))
                row = cursor.fetchone()
                return row
        except mysql.connector.Error as err:
                raise err

    def get_all(self) -> List[Dict[str, Any]]:
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor(dictionary=True) as cursor:
                query = f"SELECT ID_automatizacion, Accion, Estado FROM {self.db_name}.Automatizacion"
                cursor.execute(query, )
                rows = cursor.fetchall()
                return rows if rows else []
        except mysql.connector.Error as err:
            print(err)

    def create(self, valor: Dict[str, Any]):
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor() as cursor:
                query = f"INSERT INTO {self.db_name}.Automatizacion (Accion, Estado) VALUES (%s, %s)"
                # convertir estado booleano a TINYINT
                estado_int = 1 if valor.get("Estado") else 0 
                cursor.execute(query, (valor.get("Accion"),estado_int))
                conn.commit()
                return cursor.lastrowid # obtiene el valor del ID generado por una columna AUTO_INCREMENT en la última fila que se insertó o modificó con una sentencia INSERT o UPDATE
        except mysql.connector.Error as err:
            conn.rollback() #  restaura la base de datos a su estado anterior
            raise err
    
    def update(self, id_automatizacion: int, valor: Dict[str, Any]):
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor() as cursor:
                campos = []
                valores = []
                    
                if "Accion" in valor:
                    campos.append("Accion = %s")
                    valores.append(valor["Accion"])
                if "Estado" in valor:
                    campos.append("Estado = %s")
                    estado_int = 1 if valor["Estado"] else 0
                    valores.append(estado_int)   
                if not campos:
                    return False
                    
                valores.append(id_automatizacion)   
                query = f"UPDATE {self.db_name}.Automatizacion SET {', '.join(campos)} WHERE ID_automatizacion = %s"  
                cursor.execute(query, tuple(valores))
                conn.commit()
                return cursor.rowcount > 0
        except mysql.connector.Error as err:
            conn.rollback()
            raise err

    def delete(self, id_automatizacion: int):
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor() as cursor:
                query = f"DELETE FROM {self.db_name}.Automatizacion WHERE ID_automatizacion = %s"
                cursor.execute(query, (id_automatizacion,))
                conn.commit()
                return cursor.rowcount > 0
        except mysql.connector.Error as err:
            conn.rollback()
            raise err

    def find_by_accion(self, accion: str) -> List[Dict[str, Any]]:
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor(dictionary=True) as cursor:
                query = f"SELECT ID_automatizacion, Accion, Estado FROM {self.db_name}.Automatizacion WHERE Accion = %s"
                cursor.execute(query, (accion,))
                rows = cursor.fetchall()
                return rows if rows else []
        except mysql.connector.Error as err:
            raise err

    def set_estado(self, id_automatizacion: int, estado: bool):
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor() as cursor:
                query = f"UPDATE {self.db_name}.Automatizacion SET Estado = %s WHERE ID_automatizacion = %s"
                estado_int = 1 if estado else 0
                cursor.execute(query, (estado_int, id_automatizacion))
                conn.commit()
                return cursor.rowcount > 0
        except mysql.connector.Error as err:
            conn.rollback()
            raise err

    def get_by_estado(self, estado: bool) -> List[Dict[str, Any]]:
        conn = self.db_conn.connect_to_mysql()

        try:
            with conn.cursor(dictionary=True) as cursor:
                query = f"SELECT ID_automatizacion, Accion, Estado FROM {self.db_name}.Automatizacion WHERE Estado = %s"
                estado_int = 1 if estado else 0
                cursor.execute(query, (estado_int,))
                rows = cursor.fetchall()
                return rows if rows else []
        except mysql.connector.Error as err:
            raise err