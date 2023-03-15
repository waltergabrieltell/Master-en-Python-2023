
# Crear una lista con el contenido de esta tabla de juegos:

# Accion        Aventura        Deportes
# GTA           ASSINS          FIFA
# COD           CRASH           PRO
# PUGB          PRINCE          MOTO GP

# Mostrar esta informacion ordenada

print("\n «« Tabla »» \n")

tablaDeJuegos = [
    
    {
    "Categoria" : "Accion",
    "Juegos" : ['GTA','COD','PUGB']
    },

    {
    "Categoria" : "Aventura",
    "Juegos" : ['ASSINS','CRASH','PRINCE']
    },

    {
    "Categoria" : "Deportes",
    "Juegos" : ['FIFA', 'PRO', 'MOTO GP']
    }
]

for columna in tablaDeJuegos:
    print(f"-------- {columna['Categoria']} -------- ")
    
    for listaDeJuego in columna['Juegos']:
        print(listaDeJuego)
        


