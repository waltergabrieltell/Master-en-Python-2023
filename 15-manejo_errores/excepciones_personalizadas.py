
# Excepciones personalizadas o Lanzar excepciones
try:
    nombre = input("Introduce el nombre: ")
    edad = int(input("Introduce la edad: "))

    if edad < 5 or edad > 110:
        raise ValueError("La edad introducida no es real")
    elif len(nombre)<= 1:
        raise ValueError("El nombre no esta completo")
    else:
        print(f"Bienvenido {nombre} al Master en Python")
except ValueError:
   print("Introduce los datos correctamente!") 
except Exception as error:
    print("Existe un error: ", error)