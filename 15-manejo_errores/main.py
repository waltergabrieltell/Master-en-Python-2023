
# Capturar excepciones y manejar errores en codigo 
# suceptibles a fallos/errores

try:
    nombre = input("Ingresa nombre: ")

    if len(nombre)>1:
        nombre_usuario = "El nombre es " + nombre

    print(nombre_usuario)

except:
    print("Ha ocurrido un error, ingresa bien el nombre: ")
else:
    print("Todo ok")
finally:
    print("Fin de la iteracion!!")