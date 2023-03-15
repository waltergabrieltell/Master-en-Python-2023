
# Una funcion Lambda es una funcion anonima, 
# significa que "no tiene un nombre"
# por lo tanto no hace falta definirla con "def" ni ponerle parametros (a,b,c)
# Sirven para tareas simples pero repetitivas, por lo que todo su contenido es una sola linea de codigo
# la palabra lambda es "reservada"

# ej: Funcion para mostrar un año

dime_el_year = lambda year: f"El año es {year}"  #esta es la funcion lambda, 

print(dime_el_year(2023)) #este print es para mostrar el contenido de la ejecucion de la funcion cuando le pasamos por parametro el año
print(dime_el_year(input("Ingrese el año: "))) #este print es para mostrar el contenido de la ejecucion de la funcion cuando el usuario ingresa el dato por input

# en resumen, tiene que ser una funcion corta y concreta y en una sola linea continua de codigo