#!/usr/bin/env zxpy

# Nombre del archivo HTML
nombre_archivo = "index.html"

# Leer el contenido actual del archivo HTML
with open(nombre_archivo, "r") as archivo_html:
    contenido_html = archivo_html.read()

# Solicitar al usuario que ingrese el nombre del elemento HTML
elemento_a_modificar = input(
    "Ingrese el nombre del elemento HTML que desea modificar (h1 o p): "
).lower()

# Verificar si el elemento ingresado es válido
if elemento_a_modificar not in ["h1", "p"]:
    print("Elemento no válido. Debe ser 'h1' o 'p'.")
    exit()

# Mostrar el contenido actual del elemento seleccionado
inicio_elemento = f"<{elemento_a_modificar}>"
fin_elemento = f"</{elemento_a_modificar}>"

inicio_indice = contenido_html.find(inicio_elemento)
fin_indice = contenido_html.find(fin_elemento) + len(fin_elemento)

elemento_actual = contenido_html[inicio_indice:fin_indice]

print(f"Contenido actual del elemento {elemento_a_modificar}:")
print(elemento_actual)

# Preguntar al usuario si desea modificar el contenido o crear un nuevo elemento
opcion = input("¿Desea modificar el contenido? (s/n): ").lower()

if opcion == "s":
    # Solicitar al usuario el nuevo contenido
    nuevo_contenido = input(
        f"Ingrese el nuevo contenido para el elemento {elemento_a_modificar}: "
    )

    # Modificar el contenido en el archivo HTML
    nuevo_contenido_html = contenido_html.replace(
        elemento_actual, f"{inicio_elemento}{nuevo_contenido}{fin_elemento}"
    )

    # Escribir el nuevo contenido en el archivo HTML
    with open(nombre_archivo, "w") as archivo_html:
        archivo_html.write(nuevo_contenido_html)

    print("Contenido modificado con éxito.")

elif opcion == "n":
    # Solicitar al usuario el contenido para el nuevo elemento
    nuevo_contenido = input("Ingrese el contenido para el nuevo elemento: ")

    # Crear un nuevo elemento HTML con lista
    nuevo_elemento = f"<{elemento_a_modificar}>{nuevo_contenido}<ul><li>Elemento1</li><li>Elemento2</li></ul></{elemento_a_modificar}>"

    # Insertar el nuevo elemento en el archivo HTML
    nuevo_contenido_html = (
        contenido_html[:fin_indice] + nuevo_elemento + contenido_html[fin_indice:]
    )

    # Escribir el nuevo contenido en el archivo HTML
    with open(nombre_archivo, "w") as archivo_html:
        archivo_html.write(nuevo_contenido_html)

    print("Nuevo elemento creado con éxito.")

else:
    print("Opción no válida. Debe ser 's' o 'n'.")
