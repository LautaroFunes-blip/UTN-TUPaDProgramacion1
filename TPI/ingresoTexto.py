def ingresarTexto():

    while True:
        nombreBuscar=input('ingrese el nombre del pais que quiere buscar:').lower().strip()
        if nombreBuscar != '':
            return(nombreBuscar)
        else:
            print('el campo no puede estar vacio')