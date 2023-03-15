
#aqui podemos programar nuestras funciones, clases o lo que sea que querramos exportar como modulo


def holamundo(nombre):
    return f"Hola que tal estas, {nombre}"

def calculadora(n1,n2,basicas = False):

    suma= n1 + n2
    resta=n1 - n2
    multi=n1 * n2
    divi= n1 / n2

    cadenaDeTexto= ""

    if basicas != False:
        cadenaDeTexto += "Suma: " + str(suma)
        cadenaDeTexto += "\n"
        cadenaDeTexto += "Resta: " + str(resta)
        cadenaDeTexto += "\n"
    else:
        cadenaDeTexto += "Multiplicacion: " + str(multi)
        cadenaDeTexto += "\n"
        cadenaDeTexto += "Division: " + str(divi)
        cadenaDeTexto += "\n"

    return cadenaDeTexto

    # print(calculadora(int(input("N1: ")),int(input("N2: ")),   ))