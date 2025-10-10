from abc import ABC, abstractmethod
from typing import List, Dict, Any


class IAutomatizacionDAO(ABC):
    @abstractmethod
    def get(self, id_automatizacion: int):
        pass

    @abstractmethod
    def get_all(self) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def create(self, valor: Dict[str, Any]):
        pass

    @abstractmethod
    def update(self, id_automatizacion: int, valor: Dict[str, Any]):
        pass

    @abstractmethod
    def delete(self, id_automatizacion: int):
        pass

    @abstractmethod
    def find_by_accion(self, accion: str) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    def set_estado(self, id_automatizacion: int, estado: bool):
        pass

    @abstractmethod
    def get_by_estado(self, estado: bool) -> List[Dict[str, Any]]:
        pass