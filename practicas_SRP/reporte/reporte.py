class Reporte:
    """
    Clase orquestadora del flujo de generación de reportes.

    Atributos:
        fuente (FuenteDatos): Objeto que obtiene los datos.
        procesador (BaseProcesador): Estrategia para procesar los datos.
        generador (Generador): Clase que formatea la salida.
        entregador (Entregador): Clase que entrega o guarda el resultado.
    """

    def __init__(self, fuente, procesador, generador, entregador):
        """
        Inicializa el reporte con sus componentes.
        """
        self.fuente = fuente
        self.procesador = procesador
        self.generador = generador
        self.entregador = entregador

    def ejecutar(self):
        """
        Ejecuta el flujo completo:
        1. Obtiene datos
        2. Procesa
        3. Genera salida
        4. Entrega resultado
        """
        datos = self.fuente.obtener_datos()
        resultado = self.procesador.procesar(datos)
        salida = self.generador.generar(resultado)
        self.entregador.entregar(salida)
