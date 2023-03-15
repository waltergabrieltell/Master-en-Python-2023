nada = None
cadena = "HOla soy Walter"
entero = 99
flotante = 4.2
booleano = True
lista = [10,20,30,100,200]
listaString = [44,"treinta",30,"cuarenta"]
tuplaNoCambia = ("master", "en", "Python")
diccionario = {
    "nombre": "victor",
    "apellido": "robles",
    "Curso": "Python"
}

rango = range(9)
dato_byte = b"probando"

#imprimo
print(nada)
print(cadena)

#mostrar tipo de dato
print(type(nada), type(cadena), type(entero), type(flotante), type(booleano), type(lista), type(listaString), type(tuplaNoCambia), type(diccionario), type(rango), type(dato_byte))

print("*************************************************************************")

#concatenacion

texto = "Hola soy texto"
numero = str(776)    #se escribe str para que convierta de numero a string y lo pueda concatenar correctamente
print(texto + " " + numero)