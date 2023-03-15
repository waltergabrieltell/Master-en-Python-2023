#entrada

nombre = input("Cual es su nombre?")
edad = input("Cual es tu edad?")

#salida

print("su nombre es " + nombre)

print(f"me alegro de conocerte, bienvenido {nombre}, veo que tienes {edad} anos")
print(f"tu edad en china es de {int(edad) + 2} anos.") #aqui  convertimos el dato edad a un entero para que me permita hacer la operacion de suma, sino lo tomaria con string y daria error