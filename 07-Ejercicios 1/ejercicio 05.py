
#mostrar todos los numero entre dos numero que el usuario diga


num1= int(input("\nPrimer Numero: "))
num2= int(input("Segundo Numero: "))

print(f"\nA continuacion mostraremos los numero contenidos dentro del rango del {num1} al {num2}\n")

for contador in range(num1,num2+1):
    print(f"»» {contador} ««")
    contador +=1
else:
    print("\n*** FIN *** ")
