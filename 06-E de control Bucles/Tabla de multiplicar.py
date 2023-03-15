numeroElegido = int(input("de que num quieres saber la tabla de multiplicar: "))

if numeroElegido <1:
    numeroElegido = 1

print (f" \n Usted Escogio ver la tabla del {numeroElegido}\n")

for numero_tabla in range(1,11):

    if numeroElegido >= 100: # aqui insertamos una condicion dentro del bucle
        print("Lo siento solo se multiplicar hasta la tabla del 100 ... ")
        break #corta el bucle

    print(f"{numeroElegido} x {numero_tabla} = {numeroElegido*numero_tabla}")

else:
    print("\n Tabla finalizada !!")
