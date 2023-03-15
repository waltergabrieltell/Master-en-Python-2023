import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(f"fecha_completa es: {fecha_completa}")
print(f"El dia es: {fecha_completa.day}")
print(f"El mes es:{fecha_completa.month}")
print(f"El año es:{fecha_completa.year}")

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print(f"La fecha personalizada es: {fecha_personalizada}")
print("Mi fecha personalizada es:",fecha_personalizada)

print(datetime.datetime.now())
print(datetime.datetime.now().time())
print(datetime.datetime.now().timestamp())
