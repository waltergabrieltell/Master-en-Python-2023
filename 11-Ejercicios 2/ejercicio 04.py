## crear un script con 4 variables:
#lista
#string
#entero
#booleano

#imprima un mensaje segun el tipo de dato de cada variable, creando una funcion que lo compruebe

# Desarrollo de una 2 segunda funcion mas amigable para el usuario

def traducirTipo(tipoDeDato):
    
    result=None
    
    if tipoDeDato == list:
        result = "Lista"
    
    elif tipoDeDato == str:
        result = "Cadena de texto"
    
    elif tipoDeDato == int:
        result = "Numero Entero"

    elif tipoDeDato == bool:
        result = "Booleano"

    return result

# Utilizo el Desarrollo de la 1 primera funcion para ingresar como datos a comprobar los resultados de la segunda funcion

def comprobarTipado(dato, tipoDeDato):

    test = isinstance(dato, tipoDeDato)     # En esta variable se verifica el tipo de dato ingresado
    
    resultado = ""                          # Esta es una variable vacia para que guarde informacion

    if test:
        resultado = f"\n Este dato es tipo: {traducirTipo(tipoDeDato)}" # if Test es Verdadero se asigna el valor a la variable resultado
                      
    else:
        resultado = "El tipo de dato no es correcto "
    return resultado

#
"""
# Desarrollo de una 1 primera funcion, seria mas tecnica

def comprobarTipado(dato, tipo):
    
    test = isinstance(dato, tipo)
    
    resultado = "" #esta es una variable vacia para que guarde informacion

    if test:
        resultado = f"\n Este dato es tipo: {type(dato)}" # if Test es Verdadero se asigna el valor a la variable resultado
                      
    else:
        resultado = "El tipo de dato no es correcto "
    
    return resultado

"""

# Se declaran las variables con sus respetivos tipos de datos segun consigna y se colocan siempre despues de crear la funcion aunque la ubiesemos declarado antes
lista=["LOLO","NAI","FLAVIA","WALTER"]
string="FAMILIA "
entero=4
booleano=True

# Muestra los resultados de la funcion llamada

print(comprobarTipado(lista,list))
print(comprobarTipado(string,str))
print(comprobarTipado(entero,int))
print(comprobarTipado(booleano,bool))

