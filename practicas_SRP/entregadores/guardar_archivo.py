class GuardarArchivo:
    def guardar(self, contenido, nombre="reporte.txt"):
        with open(nombre, "w") as f:
            f.write(contenido)
            print(f"reporte guardado en {nombre}") 
