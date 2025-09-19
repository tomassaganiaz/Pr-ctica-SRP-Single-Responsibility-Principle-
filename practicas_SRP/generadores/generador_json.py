import json

class GeneradorJSON:
    def generar(self, resultado):
        return json.dumps({"resultado": resultado}, indent=2)
