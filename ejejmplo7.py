#!/usr/bin/env zxpy

import re


# Función para buscar correos en el texto
def buscarCorreos(texto):
    patronCorreo = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
    correosEncontrados = re.findall(patronCorreo, texto)
    return correosEncontrados


# Función para contar palabras en el texto
def contarPalabras(texto):
    palabras = re.findall(r"\b\w+\b", texto)
    return len(palabras)


# Función para reemplazar texto basado en un patrón y un reemplazo
def reemplazarTexto(texto, patron, reemplazo):
    textoModificado = re.sub(patron, reemplazo, texto)
    return textoModificado


# Ejemplo de uso del script
textoDePrueba = """
Hola, mi dirección de correo es alguien@dominio.com.
Recibí un mensaje de otro_correo@otrodominio.org ayer.
Este es un ejemplo de texto con 123 números y algunos signos de puntuación.
"""

# Buscar correos en el texto
correosEncontrados = buscarCorreos(textoDePrueba)
print("Correos encontrados:", correosEncontrados)

# Contar palabras en el texto
numeroDePalabras = contarPalabras(textoDePrueba)
print("Número de palabras:", numeroDePalabras)

# Reemplazar números con la palabra "NUMERO"
textoModificado = reemplazarTexto(textoDePrueba, r"\d+", "NUMERO")
print("Texto modificado:\n", textoModificado)

# Un análisis de la salida:

# Correos encontrados:

# El script utiliza una expresión regular para buscar direcciones de correo electrónico en el texto proporcionado.
# En el ejemplo dado, ha encontrado dos direcciones de correo: 'alguien@dominio.com' y 'otro_correo@otrodominio.org'.
# Número de palabras:

# La función cuenta la cantidad de palabras en el texto proporcionado.
# En el ejemplo, hay 31 palabras en el texto.
# Texto modificado:

# La función reemplaza todos los números en el texto con la palabra "NUMERO".
# El texto modificado se presenta en la salida, donde los números originales se han sustituido por "NUMERO".
# En resumen, el script realiza tres tareas:

# Encuentra direcciones de correo electrónico en el texto.
# Cuenta la cantidad de palabras en el texto.
# Reemplaza todos los números con la palabra "NUMERO".