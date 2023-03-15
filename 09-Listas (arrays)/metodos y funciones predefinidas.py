
cantantes = ['Tupak','Dan Sanger','Julio Iglesias','Bad Bunny',]
numeros = [1,2,5,8,3,4]

# ordenar lista

print(numeros)
numeros.sort()
print(numeros)

# Invertir una lista

numeros.reverse()
print(numeros)

# agregar elementos dentro de una lista

cantantes.append('TIni')  #agrega al fianl de la lista
print(cantantes)

cantantes.insert(1,'David Bisbal') #agrega en la posicion que le especifiquemos
print(cantantes)

# Eliminar elementos por indice

cantantes.pop(1)
print(cantantes)

# Eliminar por nombre

cantantes.remove('Bad Bunny')
print(cantantes)

# buscar dentro de una lista

print('Dan Sanger' in cantantes) # devuelve TRUE or FALSE

# Contar elementos

print(cantantes) #esta es la lista basica

for nombre in cantantes:  # este metodo para ponerle indice
    print(f"{cantantes.index(nombre)+1} - {nombre}")

print(f"Esta lista tiene {len(cantantes)} elementos" ) # este metodo muestra la cantidad dentro de la lista

# cuantas veces aparece un elemento especifico

print(numeros.count(8))
numeros.append(8)
print(numeros.count(8))

# Averiguar el indice de un objero en la lista

print(cantantes)
print(cantantes.index('Dan Sanger'))
print(cantantes.index('Tupak'))

# unir varias listas

cantantes.extend(numeros)
print(cantantes)