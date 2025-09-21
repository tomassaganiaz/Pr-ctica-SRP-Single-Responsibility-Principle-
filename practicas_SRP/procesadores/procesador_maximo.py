from procesadores.base_procesador import BaseProcesador

class ProcesadorMaximo(BaseProcesador):
    """
    Estrategia concreta: obtiene el valor máximo de los datos.
    """

    def procesar(self, datos):
        return max(datos) if datos else None
