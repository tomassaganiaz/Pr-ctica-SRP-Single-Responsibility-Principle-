from fuentes.fuente_datos import FuenteDatos
from procesadores.procesador_promedio import ProcesadorPromedio
from procesadores.procesador_suma import ProcesadorSuma
from procesadores.procesador_maximo import ProcesadorMaximo
from generadores.generador_texto import GeneradorTexto
from generadores.generador_json import GeneradorJSON
from entregadores.guardar_archivo import GuardarArchivo
from entregadores.mostrar_consola import MostrarConsola
from reporte.reporte import Reporte

if __name__ == "__main__":
    # 🔹 Ejemplo 1: promedio + texto + archivo
    reporte1 = Reporte(
        FuenteDatos(),
        ProcesadorPromedio(),
        GeneradorTexto(),
        GuardarArchivo()
    )
    reporte1.ejecutar()

    # 🔹 Ejemplo 2: suma + JSON + consola
    reporte2 = Reporte(
        FuenteDatos(),
        ProcesadorSuma(),
        GeneradorJSON(),
        MostrarConsola()
    )
    reporte2.ejecutar()

    # 🔹 Ejemplo 3: máximo + texto + consola
    reporte3 = Reporte(
        FuenteDatos(),
        ProcesadorMaximo(),
        GeneradorTexto(),
        MostrarConsola()
    )
    reporte3.ejecutar()
