from io import open
import pathlib
import shutil


#abrir archivo
"""
archivo = open("./14 - Sistema-archivos/fichero_texto.txt","a+")  #crea un archivo usando el permiso a+
archivo = open("14 - Sistema-archivos/fichero_texto2.txt","a+")
archivo = open("fichero_texto3.txt","a+")

"""
#ruta = pathlib.Path().absolute() + "fichero_texto.txt"
#print(ruta)

ruta = str(pathlib.Path().absolute()) + "./14 - Sistema-archivos/fichero_texto.txt" # Esta es la manera mas segura de abrir un archivo
archivo = open(ruta, "a+")
print(ruta)
archivo.write("*** Soy un texto metido desde Python *** \n") # Escribir

ruta = str(pathlib.Path().absolute()) + "./14 - Sistema-archivos/fichero_texto2.txt" # Esta es la manera mas segura de abrir un archivo
archivo = open(ruta, "a+")
print(ruta)
archivo.write("*** Soy un Segundo texto metido desde Python *** \n")

ruta = str(pathlib.Path().absolute()) + "./fichero_texto3.txt" # Esta es la manera mas segura de abrir un archivo
archivo = open(ruta, "a+")
print(ruta)
archivo.write("*** Soy un tercer texto metido desde Python *** \n")

# Cerrar archivos - Metodo Close
archivo.close()

# Abrir archivo

ruta = str(pathlib.Path().absolute()) + "./14 - Sistema-archivos/fichero_texto.txt" # Esta es la manera mas segura de abrir un archivo
archivo_lectura = open(ruta, "r")  # "r" es igual a "read" o sea leer

# Leer contenido

#contenido =  archivo_lectura.read()
#print(f"\nEl contenido del archivo '{ruta}' es:\n\n{contenido}")

#leer contenido y guardarlo en lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

print(f"\n\nEsto es una lista \n\n {lista} \n")

print("Primer For\n")

for frase in lista:
    print(" - " + frase)

print("Segundo FOR\n")

for frase in lista:
    if not frase.isnumeric():
       print(" - " + frase.upper())

print("Para que una frase se convierta en una lista FOR\n")

for frase in lista:
    lista_frase = frase.split()
    print(lista_frase)

# hacer copias

rutaOriginal = str(pathlib.Path().absolute()) + "./14 - Sistema-archivos/fichero_texto.txt"
rutaNueva = str(pathlib.Path().absolute()) + "./14 - Sistema-archivos/fichero_copiado.txt"
rutaAlternativa= "./fichero_copiado_afuera.txt"

shutil.copyfile(rutaOriginal,rutaNueva)
shutil.copyfile(rutaOriginal,rutaAlternativa)