import mysql.connector
from typing import Optional,List
from app.dao.interfaces.i_ubicacion_dao import interfaceUbicacion
from app.dominio.ubicacion import Ubicacion
from app.conn.db_connection import DBConn

class UbicacionDAO(interfaceUbicacion):
    def __init__(self):
        self.db = DBConn()
    
    def obtener_por_id(self, id_ubicacion: int) -> Optional[Ubicacion]:
        """
        Obtiene una ubicación por su ID.
        
        Args:
            id_ubicacion: ID de la ubicación a buscar
            
        Returns:
            Objeto Ubicacion si existe, None si no se encuentra
        """
        conexion = None
        try:
            conexion = self.db.connect_to_mysql()
            cursor = conexion.cursor(dictionary=True)
            
            query = """
                SELECT ID_ubicacion, nombre_ubicacion, ID_vivienda 
                FROM Ubicacion 
                WHERE ID_ubicacion = %s
            """
            cursor.execute(query, (id_ubicacion,))
            resultado = cursor.fetchone()
            
            if resultado:
                return Ubicacion(
                    nombre=resultado['nombre_ubicacion'],
                    id_vivienda=resultado['ID_vivienda'],
                    id_ubicacion=resultado['ID_ubicacion']
                )
            return None
            
        except mysql.connector.Error as e:
            print(f"Error al obtener ubicación: {e}")
            return None
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()
    
    def obtener_por_vivienda(self, id_vivienda: int) -> List[Ubicacion]:
        conexion = None
        ubicaciones = []
        try:
            conexion = self.db.connect_to_mysql()
            cursor = conexion.cursor(dictionary=True)
            
            query = """
                SELECT ID_ubicacion, nombre_ubicacion, ID_vivienda 
                FROM Ubicacion 
                WHERE ID_vivienda = %s
                ORDER BY nombre_ubicacion
            """
            cursor.execute(query, (id_vivienda,))
            resultados = cursor.fetchall()
            
            for row in resultados:
                ubicacion = Ubicacion(
                    nombre=row['nombre_ubicacion'],
                    id_vivienda=row['ID_vivienda'],
                    id_ubicacion=row['ID_ubicacion']
                )
                ubicaciones.append(ubicacion)
            
            return ubicaciones
            
        except mysql.connector.Error as e:
            print(f"Error al obtener ubicaciones por vivienda: {e}")
            return []
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()
    
    def create(self, ubicacion: Ubicacion) -> int:
        conexion = None
        try:
            conexion = self.db.connect_to_mysql()
            cursor = conexion.cursor()
            
            query = """
                INSERT INTO Ubicacion (nombre_ubicacion, ID_vivienda) 
                VALUES (%s, %s)
            """
            cursor.execute(query, (ubicacion.nombre, ubicacion.id_vivienda))
            conexion.commit()
            
            nuevo_id = cursor.lastrowid
            print(f"Ubicación '{ubicacion.nombre}' creada con ID: {nuevo_id}")
            return nuevo_id
            
        except mysql.connector.Error as e:
            print(f"Error al crear ubicación: {e}")
            if conexion:
                conexion.rollback()
            return 0
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()
    
    def update(self, ubicacion: Ubicacion) -> bool:
        conexion = None
        try:
            conexion = self.db.connect_to_mysql()
            cursor = conexion.cursor()
            
            query = """
                UPDATE Ubicacion 
                SET nombre_ubicacion = %s, ID_vivienda = %s 
                WHERE ID_ubicacion = %s
            """
            cursor.execute(query, (ubicacion.nombre, ubicacion.id_vivienda, ubicacion.id))
            conexion.commit()
            
            if cursor.rowcount > 0:
                print(f"Ubicación ID {ubicacion.id} actualizada correctamente")
                return True
            else:
                print(f"No se encontró ubicación con ID {ubicacion.id}")
                return False
            
        except mysql.connector.Error as e:
            print(f"Error al actualizar ubicación: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()
    
    def delete(self, id_ubicacion: int) -> bool:
        conexion = None
        try:
            conexion = self.db.connect_to_mysql()
            cursor = conexion.cursor()
            
            query = "DELETE FROM Ubicacion WHERE ID_ubicacion = %s"
            cursor.execute(query, (id_ubicacion,))
            conexion.commit()
            
            if cursor.rowcount > 0:
                print(f"Ubicación ID {id_ubicacion} eliminada correctamente")
                return True
            else:
                print(f"No se encontró ubicación con ID {id_ubicacion}")
                return False
            
        except mysql.connector.Error as e:
            print(f"Error al eliminar ubicación: {e}")
            if conexion:
                conexion.rollback()
            return False
        finally:
            if conexion and conexion.is_connected():
                cursor.close()
                conexion.close()