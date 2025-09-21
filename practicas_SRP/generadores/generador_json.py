import json

class GeneradorJSON:
    """
    Genera la salida del reporte en formato JSON.
    """

    def generar(self, resultado):
        return json.dumps({"resultado": resultado}, indent=2)
