
#pedir numeros hasta que el usuario ingrese el numero 111, 

numeros=int(input("\nIngrese un numero: "))

while numeros != 111:
    print("\n»» Prueba de nuevo ««")
    numeros=int(input("  Ingrese el numero: "))
else:
    print("\n      CORRECTO!!! \n Este si es el numero!!")

#################################################################
#segun el profesor puede ser asi tambien....
"""
contador = 1

while contador <100:
    numeros = int(input("ingrese numero: "))

    if numeros == 111:
        print("Correcto")
        break
    else:
        print(f"Has introducido el {numeros}")
"""