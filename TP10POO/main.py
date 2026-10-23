from ejercicio1 import funcionActividad1
from ejercicio2 import CargarNotas
from ejercicio3 import MenuRestaurante
from ejercicio4.CostoComputadora import CostoComputadora

while True:
    actividad=input('ingrese el numero de la actividad que quiere ejecutar')
    try:
        actividad=int(actividad)
        if actividad == 0:
            break
        elif actividad==1:
            practica1=funcionActividad1.actividad1()
            for celda in practica1.celdasMatriz:
                print(celda.fila, celda.columna, celda.valor)
        elif actividad==2:
            cargar=CargarNotas.CargarNotas()
            cargar.main()
            print('false')
        elif actividad ==3:
            devolucion=MenuRestaurante.MenuRestaurante()
            devolucion.main()
        elif actividad == 4:
            CostoComputadora.main()

    except ValueError:
        print('ingrese solo el nmero de la actividad')