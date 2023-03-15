
#Parametros Opcionales

def getEmpleado(nombre,dni = None): #en la funcion pedimos el parametro dni pero si el usuario no lo ingresa asignamos un parametro opcional "None" para que no frene la ejecucion
    print("\nEmpleado")
    print(f"Nombre: {nombre}")
    
    if dni != None: #
        print(f"D.N.I: {dni}")

getEmpleado("walter")