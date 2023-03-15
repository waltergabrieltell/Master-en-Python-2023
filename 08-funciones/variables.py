
"""
Variables Locales: se definen dentro de la funcion y no se puede usar fuera de ella.
Solo esta disponible dentro de la funcion a no ser que hagamos un RETURN.

Variables Globales: son las que se declaran fuera de un funcion
Estan disponibles dentro y fuera de ellas.

############### Variable Golbal ##################
# Ej. 1

frase = "\nNi los genios son tan genios - (Global)"

print(frase)


def holaMundo():
    frase = "Hola Mundo!! - (Local)"
    print(frase)

holaMundo()

"""
# Ej. 2

frase = "\nNi los genios son tan genios - (Global)"

print(frase)


def holaMundo():
    frase = "Hola Mundo!! - (Local)"
    print(frase)

    year = 2023
    print(year)

    algo = "Perro"
    print(algo)

    global website #Otro metodo para hacer una variable GLOBAL :)
    website = "www.waltertell.com - (variable Global tambien)"

    return "Datos devueltos = " + algo + " y " + str(year) 

print(holaMundo()) #aqui llama a la funcion ==> def holaMundo() -> Literal[2023]
print(website)
