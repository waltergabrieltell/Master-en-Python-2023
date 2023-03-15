
#Escribir un programa que imprima los cuadrados de los 60 primeros numeros naturales


print("\nBucle FOR\n")

contador = 1

for contardor in range(1, 61):
    cuadrado = contador * contador
    print(f"El cuadrado de {contador} es: {cuadrado}")
    contador +=1

print("\nBucle WHILE\n")

contador = 1
posicion = 0

while contador in range(1,61):
    print(f"El cuadrado de {contador} es: {contador*contador}")
    contador +=1
else:
    print("\nFinal del Ejercicio\n")