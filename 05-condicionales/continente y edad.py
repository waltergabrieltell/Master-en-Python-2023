nombre = "walter"
ciudad = "Esposende"
continente = input("ingrese continente: ")
edad = input("ingrese edad: ")
mayoria_edad = 18

if int(edad) >= mayoria_edad:
    print(f"{nombre} es mayor de edad")

    if continente == "Europa":
        print(f"{nombre} si es europeo y vive en {ciudad}")
    else:
        print(f"{nombre} no es europeo")
else:
    print(f"{nombre} No es mayor de edad")