import json
from generadores.generador_texto import GeneradorTexto
from generadores.generador_json import GeneradorJSON

def test_generador_texto():
    gen = GeneradorTexto()
    salida = gen.generar(25)
    assert "25" in salida
    assert salida.startswith("El resultado es:")

def test_generador_json():
    gen = GeneradorJSON()
    salida = gen.generar(25)
    data = json.loads(salida)
    assert data["resultado"] == 25
