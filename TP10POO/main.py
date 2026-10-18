from ejercicio1 import funcionActividad1
from ejercicio2 import CargarNotas

while True:
    actividad=input('ingrese el numero de la actividad que quiere ejecutar')
    try:
        actividad=int(actividad)
        if actividad==1:
            practica1=funcionActividad1.actividad1()
            for celda in practica1.celdasMatriz:
                print(celda.fila, celda.columna, celda.valor)
        elif actividad==2:
            funcion2=CargarNotas.CargarNotas()
            funcionFinal=funcion2.cargarAlumnosNotas()
            print(funcionFinal)

    except ValueError:
        print('ingrese solo el nmero de la actividad')