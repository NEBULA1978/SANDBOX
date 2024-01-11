#!/usr/bin/env zxpy

# Ejecutar el comando ls para obtener la lista de archivos en el directorio actual
resultado = ~"ls"

# Iterar sobre cada línea en la salida del comando ls
for linea in resultado.splitlines():
    # Dividir cada línea en nombre y extensión
    name, extension = linea.split(".")

    # Imprimir el nombre en mayúsculas y la extensión en minúsculas
    print(name.upper(), extension.lower())

# Resultado por consola

# ❯ zxpy ejejmplo3.py
# EJEJMPLO1 py
# EJEJMPLO2 py
# EJEJMPLO3 py


# //////////////


# resultado = ~"ls": Ejecuta el comando ls para obtener la lista de archivos en el directorio actual y asigna la salida a la variable resultado.

# for linea in resultado.splitlines():: Itera sobre cada línea en la salida del comando ls.

# name, extension = linea.split("."): Divide cada línea en el punto para obtener el nombre del archivo y su extensión.

# print(name.upper(), extension.lower()): Imprime el nombre del archivo en mayúsculas y la extensión en minúsculas.