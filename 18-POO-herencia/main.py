# Importo mi clase creada

import clases


# Creo una persona basica y general

persona = clases.persona()

# Ingreso los datos llamano a los metodos creados en mi archivo clases.py

persona.setNombre("Walter")
persona.setApellidos("Tell")
persona.setEdad("38")
persona.setAltura("185 cm")

# Muestra la persona
print("-------------------------------------")

print(f"La persona es: {persona.getNombre()} {persona.getApellidos()}, tiene {persona.getEdad()} años y mide {persona.getAltura()} de alto.") 

# Llamo un metodo

print(persona.hablar())
print(persona.caminar())

print("-------------------------------------")

# Ahora voy a crear otra persona pero sera un informatico

informatico = clases.informatico()

informatico.setNombre("Raul")
informatico.setApellidos("Barros")

print(f"El informatico es: {informatico.getNombre()} {informatico.getApellidos()}")
print(informatico.getLenguajes())  # Estos son metodos solo de esta persona 
print(informatico.caminar())        # Esto es un metodo heredado de la clase padre

print("-------------------------------------")

tecnico = clases.tecnicoDeRedes()

tecnico.setNombre("Pocho")
tecnico.setApellidos("Garcia")

print(f"El Tecnico es: {tecnico.getNombre()} {tecnico.getApellidos()}")
print(tecnico.auditarRedes)
print(tecnico.getLenguajes())