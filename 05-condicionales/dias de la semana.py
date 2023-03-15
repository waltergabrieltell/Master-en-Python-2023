# misma tarea pero con elif, mucho mas limpio

dia = int(input("introduce un numero del 1 al 7: "))

if dia == 1:
    print("Es Lunes")
elif dia == 2:
    print("Es Martes")
elif dia == 3:
    print("Es Miercoles")
elif dia == 4:
    print("Es Jueves")
elif dia == 5:
    print("Es Viernes")
elif dia == 6:
    print("Es Sabado")
elif dia == 7:
    print("Es Domingo")
elif dia >=8:
    print("El numero de dia esta fuera de rango")

# if dia == 1:
#     print("Es Lunes")
# else:
#     if dia == 2:
#         print("Es Martes")
#     else:
#         if dia == 3:
#             print("Es Miercoles")
#         else:
#             if dia == 4:
#                 print("Es Jueves")
#             else:
#                 if dia == 5:
#                     print("Es Viernes")
#                 else:
#                     if dia == 6:
#                         print("Es Sabado")
#                     else:
#                         if dia == 7:
#                             print("Es Domingo")