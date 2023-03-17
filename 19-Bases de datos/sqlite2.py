################################################ importar modulo de base de datos

import sqlite3  # sqlite es una base de datos que trae python

################################################ Abrir la conexion

conexion = sqlite3.connect("./19-Bases de datos/pruebas2.db")  # entre parentesis definimos el nombre para nuestra base de datos

################################################ Crear un cursos : es lo que me permite hacer consultas en una tabla

cursor = conexion.cursor()


################################################ Crear una tabla

cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Titulo VARCHAR(255),
    Descripcion TEXT,
    Precio int(255)
);
""")

################################################ Guardar cambios

conexion.commit()

################################################ Insertar datos

"""
cursor.execute("INSERT INTO productos VALUES(null, 'Primer producto', 'Descripcion de mi producto', 550)")
conexion.commit()
"""

################################################ Borrar registros 'todos los registros'

cursor.execute("DELETE FROM productos")

################################################ Insertar muchos registros a la vez

productos = [
   ("Ordenador portatil", "Buen PC", 700),
   ("Telefono", "Buen telefono", 140),
   ("Placa Base", "Buena placa", 80),
   ("Tablet", "Buena tablet", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null,?,?,?)", productos)
conexion.commit()

################################################ Update »» Actualizar datos
# si por ejemplo queremos que el precio de los productos que valen 80 se actualice a 678

# cursor.execute("UPDATE productos SET precio = 678 WHERE precio = 80")


################################################ Listar Datos

cursor.execute("SELECT * FROM productos;")
# tambien puedo ponerle condiciones de que quiero que muestre
#cursor.execute("SELECT * FROM productos WHERE precio >= 100;") # si queremos poner condicion para que nos muestre solo los produtos >= 100
#cursor.execute("SELECT * FROM productos WHERE precio >= 300;") # si queremos poner condicion para que nos muestre solo los produtos >= 300
productos = cursor.fetchall()

print(f"\nEste es el cursor: {cursor}\n")
print(f"\nEste es el Producto: {productos}\n")

for producto in productos:
    print(f"Estos son los productos agregados: {producto}")

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("")

cursor.execute("SELECT titulo FROM productos;")
producto = cursor.fetchone()
print(producto)


################################################ Cerrar la conexion

conexion.close()


