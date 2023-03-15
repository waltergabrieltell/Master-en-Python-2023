
# un modulo en python son librerias reutilizables que se pueden instalar, hay muchos en internet y tambien podemos crear nuestro propio modulo
# https://docs.python.org/es/3/tutorial/modules.html#

############# import mimodulo #aqui importo mi modulo propio ###########
#import mimodulo

#print(mimodulo.holamundo("Walter"))  #llamo al modulo y elijo el metodo
#print(mimodulo.calculadora(3,5,True))

############# importar solo una funcion especifica del modulo ##########

#from mimodulo import holamundo  #si solo quiero importar un de las funciones de mi modulo

#print(holamundo('walter')) #ya no hace falta especificar antes la ruta mi modulo

############ importar todas las funciones dentro de un modulo ############

from mimodulo import *

print(holamundo('Walter'))
print(calculadora(2,5,True))