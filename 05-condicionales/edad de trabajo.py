edad = int(input("ingrese edad para saber si le corresponde trabajar o ya debe jubilarse: "))

edad_min = 18
edad_max = 65
edad_oficial = 17

if edad >= edad_min and edad <= edad_max:
    print(f"esta en edad de trabajar, todavia le faltan {edad_max-edad} aços para jubilarse ")
elif edad <= edad_oficial:
    print("Es menor de edad")
else:
    print(f"debio jubilarse hace {edad-edad_max} anos atras...")
    