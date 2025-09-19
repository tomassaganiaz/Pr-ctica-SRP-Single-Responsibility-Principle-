from abc import ABC, abstractmethod

class BaseProcesador(ABC):
    @abstractmethod
    def procesar(self, datos):
        pass
