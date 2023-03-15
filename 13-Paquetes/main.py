
# un paquete nos permite agrupar varios modulos
# Para instalar paquetes en Python tenemos la web: https://pypi.org/

print("\nProbando paquetes:")

from mi_paquete import pruebas
from mi_paquete import herramientas

# tambien se puede importar de esta manera:
# from mi_paquete import pruebas, herramientas

pruebas.probando()
herramientas.nombre_completo("Walter","Tell")