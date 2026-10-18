try:
    from ejercicio1 import funcionActividad1
except ImportError:
    funcionActividad1 = None

from ejercicio2 import CargarNotas

while True:
    actividad = input('ingrese el numero de la actividad que quiere ejecutar')

    try:
        actividad = int(actividad)
    except ValueError:
        print('ingrese solo el numero de la actividad')
        continue

    if actividad == 1:
        if funcionActividad1 is None:
            print('la actividad 1 no esta disponible en esta copia')
            continue
        practica1 = funcionActividad1.actividad1()
        for celda in practica1.celdasMatriz:
            print(celda.fila, celda.columna, celda.valor)

    elif actividad == 2:
        funcion2 = CargarNotas.CargarNotas()
        alumnos = funcion2.cargarAlumnosNotas()

        print('lista de alumnos con sus notas y promedios:')
        for alumno in alumnos:
            print(f'alumno: {alumno.nombreCompleto} (legajo {alumno.legajo})')
            for nota in alumno.notas:
                print(f'  catedra: {nota.catedra} - nota: {nota.notaExamen}')
            print(f'  promedio: {alumno.promedio()}')
