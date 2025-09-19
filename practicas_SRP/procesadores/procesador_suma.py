from procesadores.base_procesador import BaseProcesador

class ProcesadorSuma(BaseProcesador):
    def procesar(self, datos):
        return sum(datos)
