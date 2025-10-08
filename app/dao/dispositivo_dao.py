from typing import List, Optional, Dict, Any, Tuple
import mysql.connector

from app.dao.interfaces.i_dispositivo_dao import IDispositivoDAO
from app.conn.db_connection import DBConn  # ← usa tu clase DBConn

# Columnas en el orden de los SELECTs para mapear tupla -> dict
_COLS = [
    "ID_dispositivo", "Nombre", "Marca", "Modelo", "Tipo",
    "Estado", "ID_usuario", "ID_ubicacion", "ID_automatizacion"
]

def _row_to_dict(row: Tuple) -> Dict[str, Any]:
    return {k: v for k, v in zip(_COLS, row)}

class DispositivoDAO(IDispositivoDAO):
    """
    DAO que usa DBConn para abrir/cerrar conexiones reales a MySQL.
    Ejemplo de uso:
        dao = DispositivoDAO(DBConn())  # DBConn lee config.ini y crea conexiones
    """
    def __init__(self, db_conn: DBConn):
        self._db = db_conn  # guardamos el helper, NO una conexión abierta

    # ---------- CRUD ----------
    def create(self, data: Dict[str, Any]) -> int:
        sql = """
        INSERT INTO Dispositivo (Nombre, Marca, Modelo, Tipo, Estado, ID_usuario, ID_ubicacion, ID_automatizacion)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            data.get("Nombre"),
            data.get("Marca"),
            data.get("Modelo"),
            data.get("Tipo"),  # 'LUZ' | 'CAMARA' | 'MUSICA'
            int(bool(data.get("Estado", False))),
            int(data["ID_usuario"]),
            int(data["ID_ubicacion"]),
            data.get("ID_automatizacion"),
        )
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql, params)
            conn.commit()
            return cur.lastrowid
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def get_by_id(self, id_dispositivo: int) -> Optional[Dict[str, Any]]:
        sql = f"SELECT {', '.join(_COLS)} FROM Dispositivo WHERE ID_dispositivo=%s"
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql, (id_dispositivo,))
            row = cur.fetchone()
            return _row_to_dict(row) if row else None
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def find_by_nombre(self, nombre: str) -> List[Dict[str, Any]]:
        sql = f"SELECT {', '.join(_COLS)} FROM Dispositivo WHERE LOWER(Nombre)=LOWER(%s)"
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql, (nombre,))
            rows = cur.fetchall()
            return [_row_to_dict(r) for r in rows]
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def get_all(self) -> List[Dict[str, Any]]:
        sql = f"SELECT {', '.join(_COLS)} FROM Dispositivo ORDER BY ID_dispositivo ASC"
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            rows = cur.fetchall()
            return [_row_to_dict(r) for r in rows]
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def update(self, id_dispositivo: int, data: Dict[str, Any]) -> bool:
        sql = """
        UPDATE Dispositivo
        SET Nombre=%s, Marca=%s, Modelo=%s, Tipo=%s, Estado=%s, ID_usuario=%s, ID_ubicacion=%s, ID_automatizacion=%s
        WHERE ID_dispositivo=%s
        """
        params = (
            data.get("Nombre"),
            data.get("Marca"),
            data.get("Modelo"),
            data.get("Tipo"),
            int(bool(data.get("Estado", False))),
            int(data["ID_usuario"]),
            int(data["ID_ubicacion"]),
            data.get("ID_automatizacion"),
            id_dispositivo
        )
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql, params)
            conn.commit()
            return cur.rowcount > 0
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def delete(self, id_dispositivo: int) -> bool:
        sql = "DELETE FROM Dispositivo WHERE ID_dispositivo=%s"
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql, (id_dispositivo,))
            conn.commit()
            return cur.rowcount > 0
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()

    def set_estado(self, id_dispositivo: int, estado: bool) -> bool:
        sql = "UPDATE Dispositivo SET Estado=%s WHERE ID_dispositivo=%s"
        conn = self._db.connect_to_mysql()
        cur = conn.cursor()
        try:
            cur.execute(sql, (int(bool(estado)), id_dispositivo))
            conn.commit()
            return cur.rowcount > 0
        finally:
            try:
                cur.close()
            except Exception:
                pass
            conn.close()
