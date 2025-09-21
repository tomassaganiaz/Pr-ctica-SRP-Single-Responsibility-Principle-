from fuentes.fuente_datos import FuenteDatos
from procesadores.procesador_promedio import ProcesadorPromedio
from generadores.generador_texto import GeneradorTexto
from entregadores.mostrar_consola import MostrarConsola
from reporte.reporte import Reporte

def test_reporte_ejecutar(capfd):
    """
    Test de integración: ejecuta el flujo completo y captura salida en consola.
    """
    fuente = FuenteDatos()
    procesador = ProcesadorPromedio()
    generador = GeneradorTexto()
    entregador = MostrarConsola()

    reporte = Reporte(fuente, procesador, generador, entregador)
    reporte.ejecutar()

    out, err = capfd.readouterr()
    assert "El resultado es:" in out
