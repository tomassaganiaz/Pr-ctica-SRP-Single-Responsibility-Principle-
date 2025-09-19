from procesadores.base_procesador import BaseProcesador

class ProcesadorPromedio(BaseProcesador):
    def procesar(self, datos):
        return sum(datos) / len(datos)
