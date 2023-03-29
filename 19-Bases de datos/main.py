import mysql.connector

# print("anda")

#<< conexion>>

dataBase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="31425290"
    #dataBase="master_python_11"
)

#<< conexion exitosa?>>

#print(dataBase)

#<< cursor>>

cursor = dataBase.cursor()

#<< crear base de datos>>

cursor.execute("CREATE DATABASE IF NOT EXISTS master_python_11")

#<< Mostrar bases de datos>>

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)

#<< Crear tabla>>

# cursor.execute("""
# CREATE TABLE IF NOT EXISTS vehiculos(
#     id int (10) auto_increment not null,
#     marca varchar (40) not null,
#     modelo varchar (40 not null),
#     precio float (10,2) not null,
#     CONSTRAINT pk_vehiculo PRIMARY KEY(id) 
# )
# """);
