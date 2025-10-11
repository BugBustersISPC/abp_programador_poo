from abc import ABC,  abstractmethod

from app.dominio.ubicacion import Ubicacion


class interfaceUbicacion(ABC):
    @abstractmethod
    def obtener_por_id(self, id_ubicacion: int):
        pass

    @abstractmethod
    def obtener_por_vivienda(self,id_vivienda:int) -> list[Ubicacion]:
        pass

    @abstractmethod
    def create(self,ubicacion:Ubicacion):
        pass

    @abstractmethod
    def update(self,ubicacion:Ubicacion):
        pass

    @abstractmethod
    def delete(self,id_ubicacion:int):
        pass