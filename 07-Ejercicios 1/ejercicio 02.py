# Numeros pares de 1 al 100
print("\nNumeros pares del 1 al 100\n")

contador = 1

while contador <=100:
    if contador % 2 == 0:
        print (f"El numero {contador} es par. ")
    contador +=1

print("\nNumeros impares del 1 al 100\n")

contador = 1

while contador <=100:
    if contador % 2 == 1:
        print (f"El numero {contador} es impar. ")
    contador +=1

else:
    print("\nLlegaste al final")