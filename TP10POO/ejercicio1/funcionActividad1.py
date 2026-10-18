from ejercicio1.Celda import Celda
from ejercicio1.Matriz import Matriz

def actividad1():
    instanciaMatriz=Matriz()
    while True:
        valor=input('ingrese el valor de la celda').capitalize()
        if valor != 'Fin':
            
            fila=input('ingrese la fila donde quiere guardar el valor')
            columna=input('ingrese el valor de la columna donde guardar el valor')
            try:
                fila=int(fila)
                columna=int(columna)
                existe=False
                for valores in instanciaMatriz.celdasMatriz:
                    if fila == valores.fila and columna == valores.columna:
                        print('la ubicacion de la celda ya se enceuntra ocupada')
                        existe=True
                if existe == False:
                    instanciaCelda=Celda(fila, columna, valor)
                    instanciaMatriz.celdasMatriz.append(instanciaCelda)
            except ValueError:
                print('las filas  columnas solo pueden ser valores numericos')
        else:
            break
    return instanciaMatriz