import os
import pathlib
import os.path

#ruta_afuera = str(pathlib.Path().absolute()) + "./fichero_copiado_MOVE_2.txt"

#os.remove(ruta_afuera)

# comprobar si un archivo existe o no

ruta_comprobar = os.path.abspath("./") + "/fichero_texto.txt"
ruta_comprobar = "fichero_texto3.txt"
print(ruta_comprobar)

if os.path.isfile(ruta_comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")