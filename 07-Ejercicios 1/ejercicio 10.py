
#pedir al usuario la nota de 15 alumno y mostrar cuantos estan aprobados y cuantos no.

######################################## MIO ###############################################
"""
aprobados=0
desaprobados=0

for cantidad in range(1,16):
    if cantidad <= 15:
        nota= int(input(f"\nIngrese Calificacion del {cantidad} alumno: "))
        if nota <=5:
            desaprobados +=1
        else:
            aprobados +=1
    cantidad+=1
else:
    print(f"\n Los Aprobados son: {aprobados}\n Los Desaprobados son {desaprobados}")
"""
######################################## PROFESOR ###############################################

aprobados=0
desaprobados=0
alumnos=int(input("\nIngrese cantidad de Alumnos: "))
contador=0

while contador < alumnos:
    nota = int(input(f"\nIngrese Nota para el {contador+1} alumno: "))
    if nota <5:
        desaprobados +=1
    else:
        aprobados+=1
    contador+=1
print(f"\n Aprobados {aprobados}\n Desaprobados {desaprobados}")