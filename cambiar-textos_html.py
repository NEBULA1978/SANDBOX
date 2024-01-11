#!/usr/bin/env zxpy

# Leer el contenido actual del archivo HTML
with open("index.html", "r") as archivo_html:
    contenido_html = archivo_html.read()

# Modificar el texto en los elementos <h1> y <p>
nuevo_contenido = contenido_html.replace(
    "<h1>Hola, esta es mi página HTML generada con ZXpy</h1>", "<h1>Nuevo Título</h1>"
).replace(
    "<p>¡ZXpy hace que las cosas sean más fáciles!</p>",
    "<p>Nuevo Texto del Párrafo</p>",
)

# Escribir el nuevo contenido en el archivo HTML
with open("index.html", "w") as archivo_html:
    archivo_html.write(nuevo_contenido)

print("Textos modificados con éxito en el archivo HTML: index.html")
