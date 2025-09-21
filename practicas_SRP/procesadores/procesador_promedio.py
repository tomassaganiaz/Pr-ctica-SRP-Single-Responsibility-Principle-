from procesadores.base_procesador import BaseProcesador

class ProcesadorPromedio(BaseProcesador):
    """
    Estrategia concreta: calcula el promedio de los datos.
    """

    def procesar(self, datos):
        return sum(datos) / len(datos) if datos else 0
