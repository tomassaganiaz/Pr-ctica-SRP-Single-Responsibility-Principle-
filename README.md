# 📊 Proyecto: Reporte con Principio SRP + Strategy

Este proyecto implementa un **sistema de reportes** aplicando el **Principio de Responsabilidad Única (SRP)** y el **Patrón Strategy** para los procesadores de datos.

---

## 📋 Descripción

<table>
  <tr>
    <th>Módulo</th>
    <th>Responsabilidad</th>
  </tr>
  <tr>
    <td><code>FuenteDatos</code></td>
    <td>Obtener datos desde una fuente (ejemplo: lista fija).</td>
  </tr>
  <tr>
    <td><code>Procesadores</code> (Strategy)</td>
    <td>Definir distintas estrategias de procesamiento (promedio, suma, máximo).</td>
  </tr>
  <tr>
    <td><code>Generadores</code></td>
    <td>Dar formato a la salida (texto o JSON).</td>
  </tr>
  <tr>
    <td><code>Entregadores</code></td>
    <td>Guardar o mostrar el resultado (archivo o consola).</td>
  </tr>
  <tr>
    <td><code>Reporte</code></td>
    <td>Orquestar el flujo completo.</td>
  </tr>
</table>

---

## 🚀 Ejecución del código

1. Clonar el repositorio:
```bash
git clone <URL_DEL_REPO>
cd practica_srp
```

2. Ejecutar el programa:

python main.py

3. Ejemplos incluidos en main.py:

Promedio + Texto + Archivo → genera reporte.txt

Suma + JSON + Consola

Máximo + Texto + Consola

🧪 Testing

1. Instalar pytest (si no lo tenés):

pip install pytest

2. Ejecutar los tests desde la carpeta raíz del proyecto:

pytest -v

3. Ejemplo de salida esperada:

collected 5 items

tests/test_procesadores.py::test_procesador_promedio PASSED
tests/test_procesadores.py::test_procesador_suma PASSED
tests/test_procesadores.py::test_procesador_maximo PASSED
tests/test_generadores.py::test_generador_texto PASSED
tests/test_generadores.py::test_generador_json PASSED

🧩 Diagrama de clases (Mermaid)

classDiagram
    Reporte --> FuenteDatos
    Reporte --> BaseProcesador
    Reporte --> GeneradorTexto
    Reporte --> GuardarArchivo

    BaseProcesador <|-- ProcesadorPromedio
    BaseProcesador <|-- ProcesadorSuma
    BaseProcesador <|-- ProcesadorMaximo

📌 Resumen de mejoras del proyecto
<table> <thead> <tr> <th>Categoría</th> <th>Qué se hizo</th> <th>Beneficio</th> </tr> </thead> <tbody> <tr> <td><strong>SRP (Single Responsibility Principle)</strong></td> <td>Se separó la clase Reporte en: FuenteDatos, Procesadores, Generadores, Entregadores y Reporte como orquestador.</td> <td>Cada clase tiene <strong>una sola razón para cambiar</strong>; código modular y fácil de mantener.</td> </tr> <tr> <td><strong>Strategy</strong></td> <td>Los procesadores (ProcesadorPromedio, ProcesadorSuma, ProcesadorMaximo) implementan un patrón Strategy mediante una clase base BaseProcesador.</td> <td>Permite <strong>cambiar el algoritmo de procesamiento</strong> sin modificar el resto del sistema; muestra un patrón de diseño real.</td> </tr> <tr> <td><strong>Extensibilidad</strong></td> <td>Se agregaron nuevas variantes: GeneradorJSON, MostrarConsola además de GeneradorTexto y GuardarArchivo.</td> <td>Demuestra que se pueden agregar nuevas formas de salida y entrega sin tocar las clases originales.</td> </tr> <tr> <td><strong>Estructura de carpetas</strong></td> <td>Proyecto organizado en: fuentes/, procesadores/, generadores/, entregadores/, reporte/, tests/.</td> <td>Código <strong>ordenado y modular</strong>, fácil de navegar y mantener.</td> </tr> <tr> <td><strong>README mejorado</strong></td> <td>Incluye: descripción, tabla de responsabilidades, diagrama Mermaid, instrucciones de ejecución y testing.</td> <td>Documentación clara y profesional; facilita entender el proyecto y su uso.</td> </tr> <tr> <td><strong>Tests unitarios (pytest)</strong></td> <td>Tests para procesadores y generadores, independientes del main.py.</td> <td>Garantiza que <strong>las piezas críticas funcionan correctamente</strong>; buenas prácticas de testing.</td> </tr> <tr> <td><strong>Ejemplos en main.py</strong></td> <td>Tres ejemplos distintos: promedio+texto+archivo, suma+JSON+consola, máximo+texto+consola.</td> <td>Permite <strong>ver resultados inmediatos</strong> y muestra cómo combinar las piezas; documentación viva.</td> </tr> <tr> <td><strong>Comandos claros</strong></td> <td>README incluye comandos para ejecutar el código (python main.py) y correr tests (pytest -v).</td> <td>Facilita la <strong>ejecución y prueba</strong> para cualquier usuario sin necesidad de instrucciones externas.</td> </tr> <tr> <td><strong>Posibles mejoras adicionales</strong></td> <td>- Agregar docstrings en clases y métodos<br>- Test de integración del Reporte<br>- Scripts de ejecución automatizada (run.sh o run.bat)</td> <td>Eleva la calidad del proyecto y lo hace más profesional; prepara el proyecto para producción o portfolio.</td> </tr> </tbody> </table>

