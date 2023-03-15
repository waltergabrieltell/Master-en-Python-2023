#importar mi modulo

from clase_coche import Coche

carro1 = Coche("Naranja","Chevrolet","Chevy",150,200,4)
carro2 = Coche("Blanco","Peugeot","408",280,200,5)
carro3 = Coche("Gris","Mercedes Benz","C220",320,200,4)
carro4 = Coche("Gris","VW","Vento",320,200,4)

print(carro1.getInfo())
print(carro2.getInfo())
print(carro3.getInfo())
print(carro4.getInfo())

# Detectar Tipado

carro3= "Aleatorio"

if type(carro3) == Coche:
    print("Es un objeto correcto")
else:
    print(f"\n'{carro3}' No es un objeto de tipo {Coche}")

# Visibilidad

print(carro1.soy_publico)
#print(carro1.__soy_privado) #llamando solo el atributo no funciona por que esta protegido
print(carro1.getPrivado()) #llamandolo desde un metodo si