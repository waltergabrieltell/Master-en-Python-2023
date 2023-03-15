
table = [
    {
    "categoria":"accion",
    "juego": ["a","b","c"]
    },

    {
    "categoria":"aventura",
    "juego": ["c","d","e"]
    },

    {
    "categoria":"deportes",
    "juego": ["f","g","h"]
    }
]

print("\n### TABLA ###\n")
for columna in table:
    print(f" - - - {columna['categoria']} ")

    for lista in columna ['juego']:
        print(lista)
