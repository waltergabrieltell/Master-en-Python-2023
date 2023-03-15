
#Escribir un programa que añada valores a una lista
#mientras que su longitud sea menor a 120 y luego mostra la lista

#usar While y for
print("\n Blucle WHILE\n")

lista = []
contador = 0

while len(lista) < 120:
    contador+=1
    lista.append(contador)

print(lista)

##########################
print("\n Blucle FOR\n")

coleccion =[]

for contador in range(1,121):
    coleccion.append(contador)
   
print(coleccion)

