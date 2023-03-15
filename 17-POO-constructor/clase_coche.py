class Coche:

# Atributos o propiedads ( variables) en la programacion estandar

    marca = "Ferrari"
    modelo = "Aventador"
    color =  "Rojo"
    velocidad = 300
    caballaje = 500
    plazas = 2

    soy_publico = "Soy un atributo publico"
    __soy_privado = "Soy un atributo privado"

    def __init__(self, color,marca,modelo,velocidad,caballaje,plazas):
        self.color=color
        self.marca=marca
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas

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

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def getPrivado(self):
        return self.__soy_privado
    
    
    def getInfo(self):
        info = "\n --- Informacion del coche ---\n "

        info += "\n Marca: " + self.getMarca()
        info += "\n Modelo: " + self.getModelo()
        info += "\n Color: " + self.getColor()
        info += "\n Velocidad: " + str(self.getVelocidad()) + " km/h"

        return info

# Fin definicion clase