# Generar una lista con 8 numeros enteros
# A) Recorrerla y mostrarla
#        - Hacer una funcion que recorra listas de num y devuelva un string
# B) ordenarla y mostrarla
# C) mostrar su logitud
# D) Buscar un elemento de la lista segun pida el usuario por input

###################################################################################

import random   #importe esta galeria para poder usar funciones que generen numeros random



# Punto "A"

print("\nPunto 'A' ***************************************************************\n")

numeros = list()  # genero una variable apara contener la lista de numeros

for enteros in range(8): 
    numeros.append(random.randint(1,100))  #con esta linea uso random.randit(1,100) para generar numeros enteros dentro de un rango y luego con .append los voy poniendo en la lista

print(f"Esto es el primer bloque y contiene los siguiente: {numeros}\n")

# defino la funcion

def recorreLista(listaDeNum):
    
    resultado = ""       #generamos una variable para guardar los resultados pero como strings

    for elemento in listaDeNum:
        resultado += "Elemento: " + str(elemento)
        resultado += "\n"

    return resultado

print("Esto es el resultado de la funcion\n")
print(recorreLista(numeros)) # llamo a la funcion


# Punto "B"
print("\nPunto 'B' ***************************************************************\n")

numeros.sort() #esto ordena la lista
print(f"Lista ordenada: {numeros}\n")
numeros.reverse() # invierte la lista
print(f"Lista Invertida: {numeros}")

# Punto "C"
print("\nPunto 'C' ***************************************************************\n")
print(f"La longitud de la lista es de {len(numeros)} elementos.")

#Punto "D"
print("\nPunto 'D' ***************************************************************\n")

try:
    print(int(input("ingrese numero: ")) in numeros)  #arrojara True o False

### segundo metodo de comparacion
    busqueda = int(input("Introduce un numero: "))  # guarda en la variable lo que pide el usuario

    comprobar = isinstance(busqueda, int) # comprueba si es un entero
    while not comprobar or busqueda <= 0 or None:   
        busqueda = int(input("Introduce un numero: "))
    else: 
        print(f"Has introducido {busqueda}")

    print("\nf### Buscar en la lista el numero {busqueda} ### \n")


    serch = numeros.index(busqueda) #con index busca un elemento en la lista puede ser true or false
    print(f"El numero {busqueda} existe en la lista y tiene como indice {serch}")
except:
    print("El numero no esta en la lista o a ingresado una cadena de texto, lo siento..")