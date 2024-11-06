from abc import ABC, abstractmethod

class InterfaceIterador(ABC):
    @abstractmethod
    def primero(self):
        pass

    @abstractmethod
    def haterminado(self):
        pass

    @abstractmethod
    def getActual(self):
        pass

    @abstractmethod
    def siguiente(self):
        pass