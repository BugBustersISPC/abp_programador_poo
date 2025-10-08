from abc import ABC, abstractmethod
from typing import List, Optional, Dict, Any

class IDispositivoDAO(ABC):
    """
    DAO de Dispositivo sin SQL
    para simplificar el modelo cada registro se maneja como un dict con
    las columnas de la tabla Dispositivo
    """

    @abstractmethod
    def create(self, data: Dict[str, Any]) -> int:
        """inserta y devuelve el ID_dispositivo creado"""
        pass

    @abstractmethod
    def get_by_id(self, id_dispositivo: int) -> Optional[Dict[str, Any]]:
        """obtiene un dispositivo por su ID o None si no existe."""
        pass

    @abstractmethod
    def find_by_nombre(self, nombre: str) -> List[Dict[str, Any]]:
        """busca dispositivos por nombre"""
        pass

    @abstractmethod
    def get_all(self) -> List[Dict[str, Any]]:
        """devuelve todos los dispositivos ordenados por ID asc"""
        pass

    @abstractmethod
    def update(self, id_dispositivo: int, data: Dict[str, Any]) -> bool:
        """actualiza por ID. es True si se afectó al menos 1 fila"""
        pass

    @abstractmethod
    def delete(self, id_dispositivo: int) -> bool:
        """elimina por ID. es True si se afectó al menos 1 fila"""
        pass

    @abstractmethod
    def set_estado(self, id_dispositivo: int, estado: bool) -> bool:
        """y cambia el estado On/Off, es True si se afectó al menos 1 fila"""
        pass
