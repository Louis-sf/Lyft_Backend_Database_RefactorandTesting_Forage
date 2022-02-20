from abc import ABC, abstractclassmethod, abstractmethod

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self):
        pass
