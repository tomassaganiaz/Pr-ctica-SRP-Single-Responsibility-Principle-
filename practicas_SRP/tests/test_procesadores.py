import pytest
from procesadores.procesador_promedio import ProcesadorPromedio
from procesadores.procesador_suma import ProcesadorSuma
from procesadores.procesador_maximo import ProcesadorMaximo

def test_procesador_promedio():
    proc = ProcesadorPromedio()
    datos = [10, 20, 30]
    assert proc.procesar(datos) == pytest.approx(20.0)

def test_procesador_suma():
    proc = ProcesadorSuma()
    datos = [10, 20, 30]
    assert proc.procesar(datos) == 60

def test_procesador_maximo():
    proc = ProcesadorMaximo()
    datos = [10, 20, 30]
    assert proc.procesar(datos) == 30
