
# una lista multidimensional es una lista dentro de otra lista
print("\n### Lista de contactos ###\n")

contactos = [
    [
        'Lorenzo',
        'lorenzobenjamintell@gmail.com'
    ],
    
    [
        'Walter',
        'Walterdjv@gmail.com'
    ],
    
    [
        'Flavia',
        'flaviagrana14@gmail.com'
    ],
    
    [
        'Naiara',
        'tellnaiara2006@gmail.com'
    ],
    [
        'Olga',
        'olgazurita65@gmail.com'
    ]
]

####################################################################

print(contactos) #imprime en una sola linea seguida

####################################################################

print(f"\n{contactos[1][1]}\n") # imprime el contacto 1 y dentro de ese contacto nuevamente la posicion 1, 
                       # teniendo en cuenta que las posiciones comienzan en 0. en este caso solo muestra el EMAIL

#################################################################### recorrer todos los contactos y crea una variable por cada uno

for contacto in contactos:
    print(f"{contactos.index(contacto)+1} - {contacto} \n") #uso index para que me los muestre numerados comenzando desde 1 por eso le pongo +1

#################################################################### mostrar el nombre e Email por cada elemento de la lista

for contacto in contactos:
    for elemento in contacto:  
        print(elemento)
    print("\n")

#################################################################### 

for contacto in contactos:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print("Nombre: " + elemento)
        else:
            print("Email: " + elemento)
    print("\n")
else:
    print("Fin de lista de contactos")