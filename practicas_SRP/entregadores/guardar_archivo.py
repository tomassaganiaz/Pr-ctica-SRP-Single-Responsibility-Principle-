class GuardarArchivo:
    """
    Entrega el reporte guardándolo en un archivo de texto.
    """

    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def entregar(self, salida):
        with open(self.nombre_archivo, "w", encoding="utf-8") as f:
            f.write(salida)
