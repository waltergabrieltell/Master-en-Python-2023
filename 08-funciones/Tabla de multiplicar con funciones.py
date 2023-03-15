""""
numero=int(input("\nElija un numero: "))

def tablaMultiplicar(numero):
    print(f"\nLa tabla del numero {numero} es: \n")

    for contador in range(1,11):
        operacion=numero*contador
        print(f"{numero}x{contador}={operacion}")

tablaMultiplicar(numero)

######################################################
numero=int(input("\nIngrese un numero: "))

def tabla(numero):
    for x in range(1,11):
        operacion=numero*x
        print(f"{numero}x{x}={operacion}")

tabla(numero)
##########################################################
numero=int(input("\nIngrese un numero: "))

def tabla(numero):
    for x in range(1,11):
        operacion=numero*x
        print(f"{numero}x{x}={operacion}")

tabla(numero)
"""

#############################################################

numero=int(input("\nElija un numero: "))

def tablaMultiplicar(numero):
    print(f"\nLa tabla del numero {numero} es: \n")

    for contador in range(1,11):
        operacion=numero*contador
        print(f"{numero}x{contador}={operacion}")

tablaMultiplicar(numero)


print("-----------------------------")

for numero_tabla in range(numero+1,11):
    tablaMultiplicar(numero_tabla)

