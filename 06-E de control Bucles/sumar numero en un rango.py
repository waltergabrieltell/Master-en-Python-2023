contador = 0
resultado = 0

for contador in range (0,5):
    print("voy por el "+ str(contador))
    resultado=resultado+contador

print(f"La suma de todos los numeros es: {resultado}")

contador = 0
resultado = 0

for contador in range (0,5):
    print("voy por el "+ str(contador))
    resultado += contador

print(f"La suma de todos los numeros es: {resultado}")