#ejecuta un bucle mientras se cumpla una condicion, es importante tener un contador para controlar


#mostrar todos los numero de 1 al 100
print("\n****************** Mostrar todos los numero de 1 al 100 tipo lista ***********************\n")

contador = 1

while contador <= 100:
    print(f"estoy en el {contador}")
    contador +=1

print("\n****************** Mostrar todos los numero de 1 al 100 en secuencia ***********************\n")

contador = 1
muestrame = str(0)

while contador <=100:
    muestrame = muestrame + ", " + str(contador)
    contador +=1
print(muestrame)

#***************************************************************