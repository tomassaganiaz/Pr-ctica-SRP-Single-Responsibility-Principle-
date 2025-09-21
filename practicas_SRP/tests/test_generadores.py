from generadores.generador_texto import GeneradorTexto
from generadores.generador_json import GeneradorJSON
import json

def test_generador_texto():
    g = GeneradorTexto()
    assert g.generar(50) == "El resultado es: 50"

def test_generador_json():
    g = GeneradorJSON()
    salida = g.generar(100)
    assert json.loads(salida)["resultado"] == 100
