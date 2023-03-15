
#mostrar todas las tablas de multiplicar del 1 al 10, debe mostrar el titulo.

#########################################################################################################

for cabecera in range(1,11):
    print("\n···················")
    print(f":: Tabla del {cabecera}")
    print("···················\n")    
    for numero in range(1,11):
        print(f"{cabecera} x {numero}= {cabecera*numero}")
else:
    print("\n*** FIN ***")

#**********************************************************

