def cargarContactos():
    contactos = {}
    for i in range(5):
        nombre = input(f'ingrese el nombre del contacto {i + 1}: ')
        numero = input(f'ingrese el numero de {nombre}: ')
        contactos[nombre] = numero
    return contactos

def consultarContacto(contactos):
    nombre = input('ingrese el nombre que quiere consultar: ')
    if nombre in contactos:
        print(f'{nombre}: {contactos[nombre]}')
    else:
        print('ese contacto no existe en la agenda')
