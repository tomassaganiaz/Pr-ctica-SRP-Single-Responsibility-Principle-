from procesadores.base_procesador import BaseProcesador

class ProcesadorMaximo(BaseProcesador):
    def procesar(self, datos):
        return max(datos)
