from typing import List, Optional
from ubicacion import Ubicacion

class Vivienda:
    _viviendas: List["Vivienda"] = []  
    _contador_id = 1  

    def __init__(self, nombre: str, direccion: str):
        if not nombre.strip():
            raise ValueError("El nombre de la vivienda no puede estar vacío.")
        if not direccion.strip():
            raise ValueError("La dirección de la vivienda no puede estar vacía.")

        self._id_vivienda = Vivienda._contador_id
        Vivienda._contador_id += 1

        self._nombre = nombre.strip()
        self._direccion = direccion.strip()
        self._ubicaciones: List[Ubicacion] = []

        Vivienda._viviendas.append(self)

    # Getters 
    def get_id(self) -> int:
        return self._id_vivienda

    def get_nombre(self) -> str:
        return self._nombre

    def get_direccion(self) -> str:
        return self._direccion

    def get_ubicaciones(self) -> List[str]:
        return [u.nombre for u in self._ubicaciones]

    # Setters 
    def set_nombre(self, nuevo_nombre: str) -> bool:
        if nuevo_nombre.strip():
            self._nombre = nuevo_nombre.strip()
            return True
        return False

    def set_direccion(self, nueva_direccion: str) -> bool:
        if nueva_direccion.strip():
            self._direccion = nueva_direccion.strip()
            return True
        return False

    # Metodos de instancia
    def agregar_ubicacion(self, ubicacion: Ubicacion) -> bool:
        if not isinstance(ubicacion, Ubicacion):
            raise TypeError("Debe agregarse un objeto de tipo Ubicacion.")
        if ubicacion in self._ubicaciones:
            return False
        self._ubicaciones.append(ubicacion)
        return True

    def obtener_ubicacion(self, nombre: str) -> Optional[Ubicacion]:
        for u in self._ubicaciones:
            if u.nombre.lower() == nombre.lower():
                return u
        return None

    def eliminar_ubicacion(self, nombre: str) -> bool:
        u = self.obtener_ubicacion(nombre)
        if u:
            self._ubicaciones.remove(u)
            return True
        return False

    # Metodos de clase 
    @classmethod
    def buscar_vivienda_por_nombre(cls, nombre: str) -> Optional["Vivienda"]:
        for v in cls._viviendas:
            if v._nombre.lower() == nombre.lower():
                return v
        return None

    @classmethod
    def eliminar_vivienda(cls, nombre: str, confirmar: str) -> str:
        vivienda = cls.buscar_vivienda_por_nombre(nombre)
        if vivienda:
            if confirmar.lower() == "si":
                cls._viviendas.remove(vivienda)
                return f"La vivienda '{nombre}' fue eliminada."
            elif confirmar.lower() == "no":
                return "Operación cancelada..."
            else:
                return "Error: Solo 'si' o 'no'."
        return f"No se encontró ninguna vivienda llamada '{nombre}'."

    @classmethod
    def listar_viviendas(cls) -> List[dict]:
        return [
            {
                "id": v._id_vivienda,
                "nombre": v._nombre,
                "direccion": v._direccion,
                "ubicaciones": [u.nombre for u in v._ubicaciones]
            } for v in cls._viviendas
        ]