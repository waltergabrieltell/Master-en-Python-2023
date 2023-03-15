# Mover

from io import open
import pathlib
import shutil


rutaOriginal = str(pathlib.Path().absolute()) + "./14 - Sistema-archivos/fichero_copiado.txt"

ruta_Nueva = str(pathlib.Path().absolute()) + "./fichero_copiado_MOVE.txt"

ruta_afuera = str(pathlib.Path().absolute()) + "./fichero_copiado_MOVE_2.txt"

#print(ruta_Nueva)
#print(ruta_afuera)

#shutil.move(rutaOriginal,ruta_Nueva)
shutil.move(ruta_Nueva,ruta_afuera)