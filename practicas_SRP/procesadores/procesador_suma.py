from procesadores.base_procesador import BaseProcesador

class ProcesadorSuma(BaseProcesador):
    """
    Estrategia concreta: calcula la suma de los datos.
    """

    def procesar(self, datos):
        return sum(datos)
