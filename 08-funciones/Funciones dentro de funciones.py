
def getNombre(nombre):
    texto=f"El nombre es {nombre}"
    return texto

def getApellido(apellido):
    texto=f"El apellido es {apellido}"
    return texto

############# defino una funcion que traera las 2 anteriores

def todo(nombre, apellido):
    texto= getNombre(nombre) + "\n" + getApellido(apellido)
    return texto

print(todo(input("Nombre: "), input("Apellido: ")))         #en el print pido que ingrese los parametros y muestro la funcion "todo" completada que reutiliza las funciones anteriores
