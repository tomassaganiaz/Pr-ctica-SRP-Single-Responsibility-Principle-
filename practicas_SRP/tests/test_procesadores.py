from procesadores.procesador_promedio import ProcesadorPromedio
from procesadores.procesador_suma import ProcesadorSuma
from procesadores.procesador_maximo import ProcesadorMaximo

def test_procesador_promedio():
    p = ProcesadorPromedio()
    assert p.procesar([10, 20, 30]) == 20

def test_procesador_suma():
    p = ProcesadorSuma()
    assert p.procesar([10, 20, 30]) == 60

def test_procesador_maximo():
    p = ProcesadorMaximo()
    assert p.procesar([10, 20, 30]) == 30
