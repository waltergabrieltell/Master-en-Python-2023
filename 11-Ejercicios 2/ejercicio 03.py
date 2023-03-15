
# programa q compruebe si una variable esta vacia
# si esta vacia rellenarla con texto en minuscula y mostrarlo en mayuscula

variable = str(input("Escriba algo: "))

if len(variable.strip()) <= 0:
    variable = str(input("Escriba algo en minusculas: "))
    print(variable.upper())
else:
    print(variable.upper(  ))