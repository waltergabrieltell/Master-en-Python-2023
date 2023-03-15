
##############################################################

#Defino una funcion
"""
def muestraNombre():
    print("\nWalter")
    print("Flavia")
    print("Lolo")
    print("Nai")

#invocar Funcion

muestraNombre()


#Parametros######################################################

nombre=input("\nIngresa el nombre de Tu Familia: ")

def mostrarTuNombre(nombre):
    print(f"Tu nombre es {nombre}")

mostrarTuNombre("Walter")
mostrarTuNombre("Flavia")
mostrarTuNombre("Naiara")
mostrarTuNombre("Lorenzo")

#################################################################
def mostrarTuNombre(nombre):
    print(f"\nTu nombre es {nombre}")

nombre=input("\nIntroduce tu Nombre: ")
mostrarTuNombre(nombre)

##########################################

def mostrarTuNombre(nombre, edad):
    print(f"\nTu nombre es {nombre}")

    if edad > 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

nombre=input("\nIntroduce tu Nombre: ")
edad=int(input("\nIntroduce tu Edad: "))
mostrarTuNombre(nombre, edad)

###############################################
"""
#Parametros Opcionales

def getEmpleado(nombre,dni = None):
    print("\nEmpleado")
    print(f"Nombre: {nombre}")
    
    if dni != None: #
        print(f"D.N.I: {dni}")

getEmpleado("walter")