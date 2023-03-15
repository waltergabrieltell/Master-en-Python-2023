# contador = 0
# resultado = 0

# for contador in range (0,5):
#     print("voy por el "+ str(contador))
#     resultado=resultado+contador

# print(f"La suma de todos los numeros es: {resultado}")

# contador = 0
# resultado = 0

# for contador in range (0,5):
#     print("voy por el "+ str(contador))
#     resultado += contador

# print(f"La suma de todos los numeros es: {resultado}")

#*********************************************************************

numeroElegido = int(input("de que num quieres saber la tabla de multiplicar: "))

if numeroElegido <1:
    numeroElegido = 1

print (f" Tabla del numero {numeroElegido}")

for numero_tabla in range(1,11):

    if numeroElegido > 100:
        print("100 es el numero limite")
        break
    
    print(f"{numeroElegido} x {numero_tabla} = {numeroElegido*numero_tabla}")

else:
    print("Tabla finalizada !!")
