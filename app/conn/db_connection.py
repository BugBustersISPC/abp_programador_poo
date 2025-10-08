import mysql.connector
from mysql.connector import errorcode
import configparser
import pathlib

class DBConn:
    def __init__(self, config_file = "config.ini"):
        self.config = configparser.ConfigParser()
        config_path = pathlib.Path(__file__).parent.absolute() / config_file
        self.config.read(config_path)
        self.db_config = self.config["database"]

    def connect_to_mysql(self):
        try:
            return mysql.connector.connect(
                host = self.db_config.get("host"),
                port = self.db_config.get("port"),
                user = self.db_config.get("user"),
                password = self.db_config.get("password"),
                database = self.db_config.get("database")
            )
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception("Usuario o Password no válido")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("La base de datos no existe")
            else:
                raise(err)
