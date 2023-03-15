# multiples excepciones

try:
    numero = int(input("Dime un numero para elevarlo al cuadrado: "))
    print("El cuadrado es: " + str(numero*numero))

except TypeError:
    print("Debes convertir tus cadenas a enteros 'int' en el codigo")

# except ValueError:
#     print("Introduce un numero correcto ")

except Exception as error:
    print("Ha ocurrido un error de tipo » ", type(error).__name__)
    print(type(error))

# try:
#     numero = int(input("Dime un numero para elevarlo al cuadrado: "))
#     print("El cuadrado es: " + str(numero*numero))
# except TypeError:
#     print("Debes convertir tus cadenas a enteros 'int' en el codigo")