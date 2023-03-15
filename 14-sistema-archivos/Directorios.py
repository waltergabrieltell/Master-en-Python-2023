import os
import shutil
# Crear carpeta

#if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
#    os.mkdir("./14-sistema-archivos/mi_carpeta")
#else:
#    print("YA EXISTE")



# Copiar carpeta

ruta_original = "./14-sistema-archivos/mi_carpeta"
ruta_nueva = "./14-sistema-archivos/mi_carpeta_COPY"

#shutil.copytree(ruta_original, ruta_nueva)

# Eliminar

#os.rmdir("./14-sistema-archivos/mi_carpeta")

print("\nEl contenido de mi carpeta es: \n")
contenido = os.listdir("./14-sistema-archivos/mi_carpeta_COPY")

for fichero in contenido:
    print(f"*Fichero: "+fichero)
