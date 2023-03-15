
#lista con diccionarioo

contactos = [
    {
        'nombre': 'Antonio',
        'email': 'antonio@gmail.com'
    },
    {
        'nombre': 'Walter',
        'email': 'walter@gmail.com'
    },
    {
        'nombre': 'Flavia',
        'email': 'flavia@gmail.com'
    }
]

print(contactos)
print(contactos[0]['nombre']) #muestra por clave valor los datos segun solicitado
print(contactos[0]['email'])
contactos[0]['email']='antonitorobles@gmail.com' # puedo actualizar el valor a la propiedad
print(contactos[0]['email'])

print("\nListado de Emails")

for contacto in contactos:
    print(f"Nombre de contacto: {contacto['email']}")
    print(f"Nombre de contacto: {contacto['nombre']}")
    print("******************************************")
