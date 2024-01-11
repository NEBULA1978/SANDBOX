#!/usr/bin/env zxpy

import re
from collections import Counter


# Función para buscar y mostrar direcciones de correo electrónico en el texto
def buscarCorreos(texto):
    patronCorreo = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    correosEncontrados = re.findall(patronCorreo, texto)
    print("Correos encontrados:", correosEncontrados)


# Función para contar la frecuencia de cada palabra en el texto
def contarPalabras(texto):
    palabras = re.findall(r"\b\w+\b", texto)
    contadorPalabras = Counter(palabras)
    print("Frecuencia de palabras:")
    for palabra, frecuencia in contadorPalabras.items():
        print(f"{palabra}: {frecuencia} veces")


# Función para reemplazar un término con otro en el texto
def reemplazarTermino(texto, termino, reemplazo):
    textoModificado = re.sub(termino, reemplazo, texto)
    print("Texto modificado:\n", textoModificado)


# Ejemplo de uso del script
with open("archivo_de_texto.txt", "r") as archivo:
    textoDePrueba = archivo.read()

# Tareas del script
buscarCorreos(textoDePrueba)
contarPalabras(textoDePrueba)
reemplazarTermino(textoDePrueba, "python", "zxpy")

# Este script realiza las siguientes acciones:

# Busca y muestra direcciones de correo electrónico en un archivo de texto.
# Cuenta la frecuencia de cada palabra en el archivo de texto.
# Reemplaza todas las ocurrencias de "python" con "zxpy" en el archivo de texto.
# Asegúrate de tener un archivo de texto llamado archivo_de_texto.txt con contenido significativo antes de ejecutar el script. Puedes ajustar el nombre del archivo según sea necesario. Guarda este script en un archivo con extensión .zx y ejecútalo con zxpy:
# zxpy ejejmplo8.py


