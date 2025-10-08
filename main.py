from app.conn.db_connection import DBConn

if __name__ == "__main__":
    db = DBConn()
    conexion = db.connect_to_mysql()
    if conexion:
        print("Conexión establecida correctamente.")
        conexion.close()
