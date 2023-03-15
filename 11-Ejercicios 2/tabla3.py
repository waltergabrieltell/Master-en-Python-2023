tabla = [
    {
    'Categoria':'Accion',
    'Juegos': ["asd","asd","asd"]
    },

    {
    'Categoria':'Terror',
    'Juegos':["qwe","qwe","qwe"]
    },

    {
    'Categoria':'Aventura',
    'Juegos':["zxc","zxc","zxc"]
    }
    
]
# Para cada columna dentro de la tabla, mostrar la categoria de cada columna
for columna in tabla: 
    print(f" --- {columna['Categoria']} --- ")  
    
# Para cada lista dentro de la columna con el titulo juego mostrar el contenido de la lista    
    for lista in columna['Juegos']:
        print(lista)
       