
#listas o arrays son colecciones de datas bajo un unico nombre
#podemos acceder a los valores usando un indice numerico.

pelicula = "Batman"  # esto es una variable simple
print(pelicula + " Esto es una variable simple")

################### Definir una lista ################################################

peliculas = ["Batman", "Spideman", "El señor de los anillos"] # esto es una lista
print(str(peliculas) + " Esto es una lista")
print(peliculas) #cada elemento dentro de la lista es una variable independiente y tiene un indice o posicion dentro de la lista
                 #por lo tanto gracias al indice puedo identificar la posicion y transformar (borrar, modificar,actualizar, mover) el contenido de la variable que este en ese lugar

################### Definir una lista con el comando 'list()' ################################################ 

cantantes = list(('Tupac','Drake','Bon Jovi','Steven Tyler')) #necesita encerrar dentro de () el contenido de list(), esto se llama TUPLA
print(cantantes)  

################### Definir una lista con rango numerico 'list()' ################################################ 

years = list(range(2020,2050))
print(years)

################### Definir una lista variada sin restriccion de tipo de dato ################################################ 

variada = ["Walter",80,4.4,True,"texto"]
print(variada)