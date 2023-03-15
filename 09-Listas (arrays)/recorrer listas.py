"""
#recorrer listas con bucle for

peliculas = ["Movie 1","Movie 2","Movie 3","Movie 4","Movie 5"]

print("\n### Listado de Peliculas ### \n")

for individual in peliculas:

    print(f" {peliculas.index(individual)+1} » {individual}") 
    
    # Utilizo el metodo .index() para saber la posicion, 
    # tambien agrego + para que no arranque en cero al mostrar
    
"""
################### VARIACION PIDIENDO AL USUARIO INGRESAR DATOS

peliculas = ["Movie 1","Movie 2","Movie 3","Movie 4","Movie 5"]
print("\n### Listado de Peliculas ### \n")

nueva_pelicula=""
while nueva_pelicula != "listo":
    nueva_pelicula = input("Ingrese Nueva Pelicula: ")
    
    if nueva_pelicula !="listo":
        peliculas.append(nueva_pelicula)

#del peliculas[-1] #esto evita que dentro de la lista se agregue e imprima el comando de corte "listo" eliminando del final de lista 
for individual in peliculas:
    print(f" {peliculas.index(individual)+1} » {individual}") 
    # Utilizo el metodo .index() para saber la posicion, 
    # tambien agrego + para que no arranque en cero al mostrar