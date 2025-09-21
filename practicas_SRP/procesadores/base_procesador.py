from abc import ABC, abstractmethod

class BaseProcesador(ABC):
    """
    Clase abstracta que define la interfaz para procesadores de datos.
    """

    @abstractmethod
    def procesar(self, datos):
        """
        Procesa los datos y retorna un resultado.
        """
        pass
