#!/usr/bin/env zxpy

import mysql.connector
from mysql.connector import Error


# Función para conectar a la base de datos
def conectar_bd():
    try:
        conexion = mysql.connector.connect(
            host="tu_host",
            user="tu_usuario",
            password="tu_contraseña",
            database="tu_base_de_datos",
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print("Error al conectar a la base de datos:", e)
        return None


# Función para crear la tabla si no existe
def crear_tabla(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS camisetas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                color VARCHAR(20) NOT NULL,
                manga VARCHAR(20) NOT NULL,
                precio DECIMAL(10, 2) NOT NULL
            )
        """
        )
        print("Tabla creada exitosamente")
    except Error as e:
        print("Error al crear la tabla:", e)


# Función para agregar una camiseta a la base de datos
def agregar_camiseta(conexion, nombre, color, manga, precio):
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            INSERT INTO camisetas (nombre, color, manga, precio)
            VALUES (%s, %s, %s, %s)
        """,
            (nombre, color, manga, precio),
        )
        conexion.commit()
        print("Camiseta agregada exitosamente")
    except Error as e:
        print("Error al agregar la camiseta:", e)


# Función para ver todas las camisetas en la base de datos
def ver_camisetas(conexion):
    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM camisetas")
        camisetas = cursor.fetchall()
        if not camisetas:
            print("No hay camisetas en la tienda")
        else:
            for camiseta in camisetas:
                print(camiseta)
    except Error as e:
        print("Error al obtener las camisetas:", e)


# Función para actualizar el precio de una camiseta
def actualizar_precio(conexion, id_camiseta, nuevo_precio):
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            UPDATE camisetas
            SET precio = %s
            WHERE id = %s
        """,
            (nuevo_precio, id_camiseta),
        )
        conexion.commit()
        print("Precio actualizado exitosamente")
    except Error as e:
        print("Error al actualizar el precio:", e)


# Función para eliminar una camiseta
def eliminar_camiseta(conexion, id_camiseta):
    try:
        cursor = conexion.cursor()
        cursor.execute(
            """
            DELETE FROM camisetas
            WHERE id = %s
        """,
            (id_camiseta,),
        )
        conexion.commit()
        print("Camiseta eliminada exitosamente")
    except Error as e:
        print("Error al eliminar la camiseta:", e)


# Ejemplo de uso del script
conexion = conectar_bd()
if conexion:
    crear_tabla(conexion)

    agregar_camiseta(conexion, "Camiseta Roja", "Rojo", "Manga Corta", 19.99)
    agregar_camiseta(conexion, "Camiseta Negra", "Negro", "Manga Corta", 24.99)
    agregar_camiseta(conexion, "Camiseta Marrón", "Marrón", "Manga Larga", 29.99)

    print("\nCamisetas en la tienda:")
    ver_camisetas(conexion)

    actualizar_precio(conexion, 1, 22.99)

    print("\nCamisetas actualizadas:")
    ver_camisetas(conexion)

    eliminar_camiseta(conexion, 3)

    print("\nCamisetas después de eliminar:")
    ver_camisetas(conexion)

    conexion.close()

# Reemplaza "tu_host", "tu_usuario", "tu_contraseña", y "tu_base_de_datos" con las credenciales de tu base de datos MySQL.

# Este script realiza las siguientes operaciones:

# Crea una tabla llamada camisetas en la base de datos si no existe.
# Agrega tres camisetas a la tienda.
# Muestra todas las camisetas en la tienda.
# Actualiza el precio de la primera camiseta.
# Muestra las camisetas actualizadas.
# Elimina la tercera camiseta.
# Muestra las camisetas después de la eliminación.
# Guarda el script en un archivo con extensión .zx y ejecútalo con zxpy:

# zxpy tienda_camisetas.py

