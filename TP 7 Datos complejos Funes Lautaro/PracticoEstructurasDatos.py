import frutas, contactos, palabras, alumnos, parciales, stock, agenda, paises

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

productosStock = {}

paisesCapitales = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Brasil': 'Brasilia', 'Uruguay': 'Montevideo'}

parcial1 = {101, 102, 103, 104, 105}
parcial2 = {103, 104, 106, 107}

opcion = None
while True:
    opcion = input('ingrese el numero del ejercicio que quiere ejecutar' \
    '\n 1=Frutas (agregar, actualizar y listar)' \
    '\n 2=Contactos' \
    '\n 3=Analizar frase' \
    '\n 4=Alumnos y promedios' \
    '\n 5=Comparar parciales' \
    '\n 6=Gestionar stock' \
    '\n 7=Agenda' \
    '\n 8=Invertir diccionario de paises' \
    '\n 9=Salir \n')
    try:
        opcion = int(opcion)
        if opcion == 1:
            precios_frutas = frutas.agregarFrutas(precios_frutas)
            precios_frutas = frutas.actualizarPrecios(precios_frutas)
            listaFrutas = frutas.listarFrutas(precios_frutas)
            print(f'diccionario final: {precios_frutas}')
            print(f'lista de frutas: {listaFrutas}')
        elif opcion == 2:
            contactosCargados = contactos.cargarContactos()
            contactos.consultarContacto(contactosCargados)
        elif opcion == 3:
            palabras.analizarFrase()
        elif opcion == 4:
            alumnosCargados = alumnos.cargarAlumnos()
            alumnos.calcularPromedios(alumnosCargados)
        elif opcion == 5:
            parciales.compararParciales(parcial1, parcial2)
        elif opcion == 6:
            productosStock = stock.gestionarStock(productosStock)
        elif opcion == 7:
            agenda.crearAgenda()
        elif opcion == 8:
            invertido = paises.invertirDiccionario(paisesCapitales)
            print(f'diccionario invertido: {invertido}')
        elif opcion == 9:
            print('adios')
            break
        else:
            print('ingrese una opcion valida dentro de las opciones del menu')
    except ValueError:
        print('ingrese una opcion valida dentro de las opciones del menu')
