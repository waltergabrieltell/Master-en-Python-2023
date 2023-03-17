# importar modulo de base de datos

import sqlite3  # sqlite es una base de datos que trae python

# Abrir la conexion

conexion = sqlite3.connect("./19-Bases de datos/pruebas2.db")  # entre parentesis definimos el nombre para nuestra base de datos

# Crear un cursos : es lo que me permite hacer consultas en una tabla

cursor = conexion.cursor()


# Crear una tabla

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(255),
    descripcion TEXT,
    precio int(255)
);
""")

# Guardar cambios

conexion.commit()

# Insertar datos

"""
cursor.execute("INSERT INTO productos VALUES(null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()
"""

# Borrar registros 'todos los registros'

# >> cursor.execute("DELETE FROM productos")

# Insertar muchos registros a la vez

productos = [
   ("Ordenador portatil", "Buen PC", 700),
   ("Telefono", "Buen telefono", 140),
   ("Placa Base", "Buena placa", 80),
   ("Tablet", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
cursor.commit()


# Listar Datos

cursor.execute("SELECT * FROM productos;")
productos = cursor.fetchall()

print(f"\nEste es el cursor: {cursor}\n")
print(f"\nEste es el Producto: {productos}\n")

for producto in productos:
    print(f"Estos son los productos agregados: {producto}")

for producto in productos:
    print("")
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)


# Cerrar la conexion

conexion.close()


