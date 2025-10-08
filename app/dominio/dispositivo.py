from typing import Optional, Dict, Any, List, Union
from enum import Enum

class TipoDispositivoEnum(Enum):
    CAMARA = "CAMARA"
    LUZ = "LUZ"
    MUSICA = "MUSICA"


class Dispositivo:
    """
    representa un dispositivo inteligente dentro del hogar
    los atributos se mantienen privados y se accede a ellos a través de propiedades
    """
    # constantes tipo (para compatibilidad con tu código original)
    TIPO_CAMARA = 1
    TIPO_LUZ = 2
    TIPO_MUSICA = 3

    # map para mostrar texto en __str__
    __TIPO_A_TEXTO = {
        TIPO_CAMARA: "Cámara",
        TIPO_LUZ: "Luz",
        TIPO_MUSICA: "Música"
    }

    def __init__(self, nombre: str, tipo: int, estado: bool):
        # validación de atributos
        if not nombre or not isinstance(nombre, str):
            raise ValueError("El nombre no puede estar vacío y debe ser un texto.")
        if tipo not in self.__TIPO_A_TEXTO:
            raise ValueError(f"El tipo de dispositivo '{tipo}' no es válido.")
        if not isinstance(estado, bool):
            raise ValueError("El estado debe ser un valor booleano (True/False).")
        # atributos privados
        self.__nombre = nombre
        self.__tipo = tipo
        self.__estado = estado

    # getters
    @property
    def nombre(self) -> str:
        return self.__nombre

    @property
    def tipo(self) -> int:
        return self.__tipo

    @property
    def estado(self) -> bool:
        return self.__estado

    # setter
    @estado.setter
    def estado(self, nuevo_estado: bool):
        if not isinstance(nuevo_estado, bool):
            raise ValueError("El estado solo puede ser True o False.")
        self.__estado = nuevo_estado

    # métodos
    def encender(self):
        self.__estado = True
        print(f"El dispositivo '{self.nombre}' ha sido encendido.")

    def apagar(self):
        self.__estado = False
        print(f"El dispositivo '{self.nombre}' ha sido apagado.")

    def __str__(self):
        tipo_texto = self.__TIPO_A_TEXTO.get(self.__tipo, "Desconocido")
        estado_texto = "On" if self.__estado else "Off"
        return f"{self.nombre} (Tipo: {tipo_texto}) - Estado: {estado_texto}"



#controlador usando DAO sin listas en memoria

from app.dao.interfaces.i_dispositivo_dao import IDispositivoDAO

#mapas entre enteros 1/2/3 y el ENUM de la DB
_INT_TO_ENUM: Dict[int, str] = {
    Dispositivo.TIPO_CAMARA: "CAMARA",
    Dispositivo.TIPO_LUZ: "LUZ",
    Dispositivo.TIPO_MUSICA: "MUSICA",
}
_ENUM_TO_INT: Dict[str, int] = {v: k for k, v in _INT_TO_ENUM.items()}

def _to_enum_str(tipo: Union[int, TipoDispositivoEnum]) -> str:
    """convierte un tipo int o Enum al string de ENUM de la DB"""
    if isinstance(tipo, TipoDispositivoEnum):
        return tipo.value
    return _INT_TO_ENUM.get(int(tipo), "")  # "" for invalid

def _to_int_tipo(enum_str: str) -> int:
    """convierte el string ENUM de la DB al entero usado por la clase Dispositivo"""
    return _ENUM_TO_INT.get(enum_str, Dispositivo.TIPO_LUZ)  # default prudente


class ControladorDispositivos:
    """
    operaciones DB vía DAO.
    mantiene nombres/estilo similares al controlador original
    """
    def __init__(self, dispositivo_dao: IDispositivoDAO):
        self._dao = dispositivo_dao

    def agregar_dispositivo(
        self,
        nombre: str,
        tipo: Union[int, TipoDispositivoEnum],
        estado: bool,
        id_usuario: int,
        id_ubicacion: int,
        marca: Optional[str] = None,
        modelo: Optional[str] = None,
        id_automatizacion: Optional[int] = None
    ) -> bool:
        #duplicado por nombre 
        if self.buscar_por_nombre(nombre) is not None:
            print(f"Error: Ya existe un dispositivo con el nombre '{nombre}'.")
            return False

        #validación con la clase
        tipo_int = _to_int_tipo(_to_enum_str(tipo)) if isinstance(tipo, TipoDispositivoEnum) else int(tipo)
        try:
            _ = Dispositivo(nombre, tipo_int, estado)
        except ValueError as e:
            print(f"Error al crear el dispositivo: {e}")
            return False

        tipo_enum = _to_enum_str(tipo)
        if not tipo_enum:  # tipo inválido
            print("Tipo inválido.")
            return False

        data = {
            "Nombre": nombre,
            "Marca": marca,
            "Modelo": modelo,
            "Tipo": tipo_enum,            # enum db
            "Estado": bool(estado),
            "ID_usuario": id_usuario,
            "ID_ubicacion": id_ubicacion,
            "ID_automatizacion": id_automatizacion,
        }

        new_id = self._dao.create(data)
        print(f"Dispositivo '{nombre}' agregado correctamente con ID {new_id}.")
        return True

    def buscar_por_nombre(self, nombre: str) -> Optional[Dispositivo]:
        filas = self._dao.find_by_nombre(nombre)
        if not filas:
            return None
        fila = filas[0]
        tipo_int = _to_int_tipo(fila["Tipo"])
        d = Dispositivo(fila["Nombre"], tipo_int, bool(fila["Estado"]))
        return d

    def eliminar_dispositivo(self, nombre: str) -> bool:
        filas = self._dao.find_by_nombre(nombre)
        if not filas:
            print(f"Error: No se encontró el dispositivo '{nombre}' para eliminar.")
            return False
        id_dispositivo = filas[0]["ID_dispositivo"]
        ok = self._dao.delete(id_dispositivo)
        if ok:
            print(f"Dispositivo '{nombre}' eliminado.")
        return ok

    def listar_dispositivos(self):
        print("\n--- LISTA DE DISPOSITIVOS (DB) ---")
        filas = self._dao.get_all()
        if not filas:
            print("No hay dispositivos registrados.")
        else:
            for f in filas:
                tipo_int = _to_int_tipo(f["Tipo"])
                d = Dispositivo(f["Nombre"], tipo_int, bool(f["Estado"]))
                print(f"- {d}")
        print("----------------------------------\n")

    def set_estado_por_nombre(self, nombre: str, nuevo_estado: bool) -> bool:
        filas = self._dao.find_by_nombre(nombre)
        if not filas:
            print(f"Error: No se encontró el dispositivo '{nombre}'.")
            return False
        id_dispositivo = filas[0]["ID_dispositivo"]
        return self._dao.set_estado(id_dispositivo, nuevo_estado)
