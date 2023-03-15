"""

def mi_funcion():
    return "Hola que tal" + nombre  #puedo acceder a la variable "nombre" desde una funcion superior

def mi_funcion2():
    return "Hola que tal 2" + apellido #puedo acceder a la variable "apellido" desde una funcion superior

nombre = "Walter" # recien aqui estan definidas las variables que la funcion uso arriba para concatenar
apellido = "Tell"

print("Hola mundo")
print(f"Bienvenido {nombre}")

print(mi_funcion())  #puedo mostrar la funcion sin ningun problema
print(mi_funcion2()) # ATENCION, si las variables se definen despues de este print no se leeran y dara error
                     # es importante prestar atencion a eso
""" 
 ################################################################################################################

def mi_funcion(nombre):
    return "\nTu nombre es " + nombre  #puedo acceder a la variable "nombre" desde una funcion superior

def mi_funcion2(apellido):
    return "Tu apellido es " + apellido #puedo acceder a la variable "apellido" desde una funcion superior

nombre = input("Cual es tu nombre: ") # recien aqui estan definidas las variables que la funcion uso arriba para concatenar
apellido = input("Cual es tu apellido: ")

print(f"\nEn hora buena {nombre}")
print("Estas programando con Python :)")

print(mi_funcion(nombre))  #puedo mostrar la funcion sin ningun problema
print(mi_funcion2(apellido)) # ATENCION, si las variables se definen despues de este print no se leeran y dara error
                     # es importante prestar atencion a eso