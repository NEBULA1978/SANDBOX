#!/usr/bin/env zxpy

# Contenido HTML
contenido_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Mi Página HTML Generada con ZXpy</title>
</head>
<body>
    <h1>Hola, esta es mi página HTML generada con ZXpy</h1>
    <p>¡ZXpy hace que las cosas sean más fáciles!</p>
</body>
</html>
"""

# Escribir el contenido en un archivo HTML
with open("index.html", "w") as archivo_html:
    archivo_html.write(contenido_html)

print("Archivo HTML generado con éxito: index.html")


# Este script genera un archivo HTML llamado index.html con el contenido proporcionado en la variable contenido_html.

# Ejecutar:
# zxpy crea_html.py
