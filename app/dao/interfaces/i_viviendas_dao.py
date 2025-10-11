from abc import ABC, abstractmethod

class IViviendasDAO(ABC):
    @abstractmethod
    def get(self, id_vivienda: int):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, vivienda):
        pass

    @abstractmethod
    def update(self, vivienda):
        pass

    @abstractmethod
    def delete(self, id_vivienda: int):
        pass