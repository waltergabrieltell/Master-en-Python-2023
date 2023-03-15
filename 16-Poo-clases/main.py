
# La Programacion orientada a objetos es una forma de programar en la cual todo lo vamos a ver como objetos.

#
# clases: 
#   molde para crear objetos 

# Definir una clase (molde para crear mas objetos de ese tipo)
# (coche) con caracteristicas similares

class Coche:

    # Atributos o propiedads ( variables) en la programacion estandar
    marca = "Ferrari"
    modelo = "Aventador"
    color =  "Rojo"
    velocidad = 300
    caballaje = 500
    plazas = 2

    # Metodos, son acciones que hace el objeto (funciones)


    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def getVelocidad(self):
        return self.velocidad
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color
    
    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

# Fin definicion clase

# Crear objetos / Instanciar la clase
print("-------------------------")
coche = Coche()

print("Coche 1: \n")

coche.setColor("Amarillo")
coche.setModelo("Murcielago")

print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print(coche.velocidad)

coche.frenar()

print(coche.velocidad)

print(coche.getVelocidad()) # usando el metodo getter para velocidad

# Crear mas objetos
print("----------------------------")
print("Coche 2 \n")

coche2 = Coche()

coche2.setColor("Verde")
coche2.setModelo("Gallardo")

print(coche2.getColor())
print(coche2.marca, coche2.getModelo(), coche2.getColor())

print(type(coche2))