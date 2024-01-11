#!/usr/bin/env zxpy

# Ejecutar el comando ls para obtener la lista de archivos en el directorio actual
resultado = ~"ls"

# Iterar sobre cada línea en la salida del comando ls
for linea in resultado.splitlines():
    # Dividir cada línea en puntos para obtener partes del nombre del archivo
    partes = linea.split(".")

    # Imprimir la lista resultante de partes para cada línea
    print(partes)
