
print("*************************")

num_usuario = int(input("Ingrese un numero: "))

if num_usuario <1:
    num_usuario=1

print(f"\n*** tabla del {num_usuario} ***\n ")

contador = 1
while contador <= 10:
    print(f"{num_usuario} x {contador} = {num_usuario*contador}")
    contador +=1
else:
    print(f"\n*** tabla finalizada ***\n ")
