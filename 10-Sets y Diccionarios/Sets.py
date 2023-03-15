
# es un tipo de datos para tener una coleccion de valores que no tienen indice ni orden

personas = {
    "Victor",
    "Manolo",
    "Francisco"
}

print(personas)
print(type(personas)) #saber el tipo

personas.add("Paco") # agrega elemento
print(personas)
personas.remove("Francisco") # elimina elemento
print(personas)