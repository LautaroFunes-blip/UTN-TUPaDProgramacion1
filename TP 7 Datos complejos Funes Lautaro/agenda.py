def crearAgenda():
    agenda = {}
    while True:
        opcion = input('ingrese la opcion que quiere realizar' \
        '\n 1=Agregar evento \n 2=Consultar evento \n 3=Salir \n')
        try:
            opcion = int(opcion)
            if opcion == 1:
                dia = input('ingrese el dia: ')
                hora = input('ingrese la hora: ')
                evento = input('ingrese el evento: ')
                agenda[(dia, hora)] = evento
            elif opcion == 2:
                dia = input('ingrese el dia a consultar: ')
                hora = input('ingrese la hora a consultar: ')
                if (dia, hora) in agenda:
                    print(f'actividad: {agenda[(dia, hora)]}')
                else:
                    print('no hay ninguna actividad registrada en ese dia y hora')
            elif opcion == 3:
                break
            else:
                print('ingrese una opcion valida')
        except ValueError:
            print('ingrese una opcion valida')
    return agenda
