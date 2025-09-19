class Reporte:
    def __init__(self, fuente, procesador, generador, entregador):
        self.fuente = fuente
        self.procesador = procesador
        self.generador = generador
        self.entregador = entregador

    def ejecutar(self):
        datos = self.fuente.obtener()
        resultado = self.procesador.procesar(datos)
        salida = self.generador.generar(resultado)
        self.entregador.guardar(salida)
