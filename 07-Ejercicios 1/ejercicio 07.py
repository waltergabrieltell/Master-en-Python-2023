
# impares entre un rango definido por usuario


num1=int(input("Ingrese Num 1: "))
num2=int(input("Ingrese Num 2: "))

if num1<num2:
    print(f"\nLos numeros impares contenidos entre el numero {num1} y el {num2} son:\n")

    for numeros in range(num1,num2+1):
        if numeros%2 == 1:
            print(f"»» {numeros}")
    else:
        print("Fin de lista")
else:
    print("\n ATENCION!, No se puede procesar este rango.") 