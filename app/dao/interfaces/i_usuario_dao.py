from abc import ABC, abstractmethod

class InterfaceUsuario(ABC):

    @abstractmethod
    def get_by_email(self, email: str):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def create(self, object: dict):
        pass

    @abstractmethod
    def update(self, id: int, object: dict):
        pass

    @abstractmethod
    def delete_by_id(self, id: int):
        pass