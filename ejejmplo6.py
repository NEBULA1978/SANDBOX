#!/usr/bin/env zxpy

import subprocess

# Ejecutar el comando curl y capturar la salida
resultado = subprocess.run(
    "curl -s google.es", shell=True, capture_output=True, text=True
).stdout

# /////////////////

# resultado.splitlines(): Esta parte toma la cadena resultado y la divide en una lista de líneas. Cada línea es un elemento de la lista.

# enumerate(): Esta función devuelve tanto el índice como el valor del elemento en la iteración. Aquí, se utiliza para obtener tanto el índice como el contenido de cada línea en la lista.

# for index, line in ...: Un bucle for que itera sobre cada línea del resultado.

# print(index, line): Imprime el índice y el contenido de cada línea en la consola.

# Entonces, en resumen, este fragmento de código imprime el índice y el contenido de cada línea del resultado obtenido al ejecutar el comando curl. Es útil para visualizar la salida línea por línea y entender la estructura del contenido recuperado.
for index, line in enumerate(resultado.splitlines()):
    print(index, line)


# Funciones de suma y multiplicación
def suma(a, b):
    return a + b


def multiplicacion(a, b):
    return a * b


# Ejemplo de uso de las funciones
resultado_suma = suma(2, 3)
resultado_multiplicacion = multiplicacion(2, 3)

# Imprimir resultados
print("Resultado de la suma:", resultado_suma)
print("Resultado de la multiplicación:", resultado_multiplicacion)
