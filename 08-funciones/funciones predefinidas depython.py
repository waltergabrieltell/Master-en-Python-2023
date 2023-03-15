
######################################################################################################################################

nombre = "Mi nombre es Walter Gabriel Tell" #Defino una variable simple y con el = le asigno un valor

################################# Funcion general print(), sirve para mostrar por pantalla un contenido/resultado

print(nombre)

################################# Funcion para mostrar el tipo de dato (type)

print(type(nombre))

################################# Funcion para detectar/comparar que tipado tiene (ininstance)

comprobar = isinstance(nombre,str)  #el segundo parametro es donde definimos el "tipo" con el que vamos a comparar el contenido del primer parametro
if comprobar:                       # ponemos la condicion IF para que se haga la comparacion, no hace falta escribir nada mas, python ya interpreta la orden
    print("Esta variable es un string") #si la comparacion es verdadera y el primer parametro es = a un "str" imprime esta linea
else:
    print("No es un Str")   #si la comparacion es falsa, o sea que no es un "str" imprime esta linea.

if not isinstance(nombre, float): #misma logica para otro ejemplo ;) »» si NO es un FLOAT entonces imprime.
    print("No es un numero decimal")

################################# Funcion para limpiar cadenas de Strings y borrarle los espacios (.strip())

frase = "       Mi contenido    "
print(frase)        # Mostrara el la frase tal y como se escribio
print(frase.strip())# Mostrara el la frase sin los espacios de mas tanto al comienzo como al final

################################ Funcion para eliminar Variables

year = 2023
print(year)

del year # este comando elimina la variable year
#print(year) # NameError: name 'year' is not defined

################################ Funcion para comprobar Variables vacias o longitud del contenido de una variable ('len()')

texto = "walter"

if len(texto)<=0:   #si el 'len' de texto es menor o igual a 0, significa VACIA
    print("La variable esta vacia")
else:
    print("La variable 'texto = walter' tiene contenido y su longitud es de", len(texto), "caracteres.")

################################ Funcion para encontrar caracteres (.find)

frase = "La vida es bella"
print(frase)
print(frase.find("vida"), "<-- Muestra la posicion desde donde encontro la palabra 'vida'") # Sabremos a partir de "que posicion comenzando de 0" se encuentra el caracter o palabra que buscamos

################################ Funcion para reemplazar palabras en un string (.replace)

nueva_frase = frase.replace("vida", "moto")
print(nueva_frase + " - Nueva frase con palabra reemplazada")

################################ Funcion para mayusculas y minusculas (.lower()) y (.upper())
nombre = "Naiara Tell"
print(nombre + " - Normal")
print(nombre.lower()+ " - Metodo .lower()")
print(nombre.upper()+ " - Metodo .upper()") 

