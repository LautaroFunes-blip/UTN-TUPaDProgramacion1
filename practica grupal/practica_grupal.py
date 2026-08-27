ejercicio_ejecutar=None
parte=int(input('desea revisar la primera o la segunda parte del trabajo'))
while ejercicio_ejecutar != 0:
    if parte == 1:
        ejercicio_ejecutar=int(input('ingrese el numero de actividad a ejecutar'))
        if ejercicio_ejecutar==1:
            numeros=[]
            cantidad=int(input('ingrese la cantidad de numeros quequiere sumar'))
            for i in range(cantidad):
                numeros_usuario=int(input('ingrese los numeros de la lista'))
                numeros.append(numeros_usuario)
            resultado= sum(numeros)
            print(resultado)
            print(numeros)
        elif ejercicio_ejecutar == 2:
            numeros=[]
            for i in range(5):
                numeros_usuario=int(input('ingrese la lista de 5 numeros'))
                numeros.append(numeros_usuario)
            minimo=min(numeros)
            maximo=max(numeros)
            print(minimo, maximo)
        elif ejercicio_ejecutar == 3:
            lista=[]
            for i in range(5):
                lista_usuario=input('ingrese los valores de la lista')
                lista.append(lista_usuario)
            print(lista[::-1])
        elif ejercicio_ejecutar == 4:
            lista_numeros=[]
            numeros_pares=[]
            numeros_impares=[]
            for i in range(10):
                numeros=int(input('ingrese los numeros pertenecientes a la lista'))
                lista_numeros.append(numeros)
            for numeros in lista_numeros:
                if numeros %2 == 0:
                    numeros_pares.append(numeros)
                else:
                    numeros_impares.append(numeros)
            canitada_impares=len(numeros_impares)
            cantidad_pares=len(numeros_pares)
            print(numeros_pares, numeros_impares)
            print(canitada_impares, cantidad_pares)
        elif ejercicio_ejecutar == 5:
            lista_multiplicar=[2,4,6]
            multiplicador=int(input('ingrese el numero por el que desea multiplicar la lista'))
            cantidad=len(lista_multiplicar)
            lista_resultado=[]
            for i in range(cantidad):
                resultado=lista_multiplicar[i] * multiplicador
                lista_resultado.append(resultado)
            print(lista_resultado)
        elif ejercicio_ejecutar == 6:
            lista=[]
            cantidad_numeros=int(input('ingrese la cantidad de numeros que quiere ingresar a la lista'))
            for i in range(cantidad_numeros):
                numeros_ingresar=int(input('ingrese la lista de numeros'))
                lista.append(numeros_ingresar)
            lista_limpia=list(set(lista))
            print(lista_limpia)
        elif ejercicio_ejecutar == 7:
            notas=[]
            cantidad_notas=int(input('ingrese la cantidad de notas que quiere ingresar'))
            for i in range(cantidad_notas):
                notas_usuario=float(input('ingrese la notas correspondientes'))
                notas.append(notas_usuario)
            suma=sum(notas)
            promedio=suma/cantidad_notas
            print(promedio)
        elif ejercicio_ejecutar == 8:
            lista=[]
            for i in range(5):
                elementos=input('ingrese los elementos que deseba ingresar a la lista')
                lista.append(elementos)
            vistos=set()
            repetidos=set()

            for elementos in lista:
                if elementos in vistos:
                    repetidos.add(elementos)
                else:
                    vistos.add(elementos)
            print(repetidos)
        elif ejercicio_ejecutar == 9:
            numeros_primos = []
            numeros_simples = []
            cantidad_numeros = int(input('ingrese la cantidad de numeros que quiere probar: '))

            for i in range(cantidad_numeros):
                numeros = int(input('ingrese los valores a ingresar: '))
                numeros_simples.append(numeros)

            for numeros in numeros_simples:
                if numeros < 2:
                    continue
                es_primo = True
                for divisor in range(2, numeros):
                    if numeros % divisor == 0:
                        es_primo = False
                        break
                if es_primo:
                    numeros_primos.append(numeros)

            print(numeros_primos)

        elif ejercicio_ejecutar == 10:
            lista=[]
            cantidad=int(input('ingree la cantidad de numeros que desea ingresar a la lista'))
            if cantidad > 2:
                for i in range(cantidad):
                    numeros=int(input('ingrese los numeros a ingresar en la lista'))
                    lista.append(numeros)
                lista.pop(2)
                print(lista)
            else:
                print('ingrese una cantidada mayor a 2')

        elif ejercicio_ejecutar == 11:
            numeros_repetidos=[]
            cantidad=int(input('ingrese la cantidad de numeros dentro de la lista'))
            for i in range(cantidad):
                numeros=input('ingrese los objetos de la lista')
                numeros_repetidos.append(numeros)
            repetidos=0
            numero_buscar=input('ingrese el dato que desea buscar')
            for datos in numeros_repetidos:
                if datos == numero_buscar:
                    repetidos+=1
                else:
                    continue
            print('el dato buscado aparece un total de:')
            print(repetidos)

        elif ejercicio_ejecutar == 12:
            lista_1=[1,4,2,5]
            lista_2=[2,6,4,7]
            resultados=[]
            for numeros in range(len(lista_1)):
                numero_1=lista_1[numeros]
                numero_2=lista_2[numeros]
                suma=numero_1 + numero_2
                resultados.append(suma)
            print(resultados)

        elif ejercicio_ejecutar == 13:
            print('Numpy es una libreria que ayud a hacer calculos cientificos de forma mas sensilla, pensada para manejar muchos datos, y la funcion ndarray es una forma mas rapida de usar una lista')
        elif ejercicio_ejecutar == 0:
            break
        else:
            print('ingrese un ejercicio valido')
    if parte == 2:
        ejercicio_ejecutar=int(input('ingrese el numero de actividad a ejecutar'))
        if ejercicio_ejecutar == 1:
            matriz=[]
            contador = 1
            filas=int(input('ingrese la cantidad de filas'))
            columnas=int(input('ingrese la cantidad de columnas'))
            for i in range(filas):
                fila_actual=[]
                for j in range(columnas):
                    fila_actual.append(contador)
                    contador += 1
                matriz.append(fila_actual)
            print(matriz)

        elif ejercicio_ejecutar == 2:
            lista_bidimencional=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
            total_1=sum(lista_bidimencional[0])
            total_2=sum(lista_bidimencional[1])
            total_3=sum(lista_bidimencional[2])
            total_final=total_1+total_2+total_3
            print(total_final)
        elif ejercicio_ejecutar == 3:
            lista_bidimencional=[[1,2,3,4],[1,2,3,4],[1,2,3,4]]
            total_1=sum(lista_bidimencional[0])
            total_2=sum(lista_bidimencional[1])
            total_3=sum(lista_bidimencional[2])
            print(total_1, total_2, total_3)

        elif ejercicio_ejecutar == 4:
            matriz=[[1,2,3],[1,2,3]]
            traspuesta=[]
            for columna in range (len(matriz[0])):
                fila_nueva=[]
                for fila in range(len(matriz)):
                    fila_nueva.append(matriz[fila][columna])
                traspuesta.append(fila_nueva)
            print(traspuesta)

        elif ejercicio_ejecutar == 5:
            matriz=[[9,6,7],[2,5,3],[1,4,7]]
            mayor=[]
            for numero in matriz:
                mayor_1=max(matriz[0])
                mayor_2=max(matriz[1])
                mayor_3=max(matriz[2])
                mayor.append(mayor_1)
                mayor.append(mayor_2)
                mayor.append(mayor_3)
                mayor_final=max(mayor)

            print(mayor_final)

        elif ejercicio_ejecutar == 6:
            lista=[[5,9,6],[2,7,4],[1,5,2]]
            lista_resultados=[]
            valor_escalar=int(input('ingrese el valro a multiplicar'))

            for filas in lista:
                fila_nueva=[]
                for elemento in filas:
                    fila_nueva.append(elemento * valor_escalar)
                lista_resultados.append(fila_nueva)
            print(lista_resultados)

        elif ejercicio_ejecutar == 7:
            lista_cuadrada=[
                [1,2,3],
                [4,5,6],
                [7,8,9]
                ]
            diagonal= []
            for i in range(len(lista_cuadrada )):
                diagonal.append(lista_cuadrada [i][i])
            print(diagonal)

        elif ejercicio_ejecutar == 8:
            matriz=[]
            tamaño_matriz=int(input('ingrese el tamaño de la matriz que quiere realizar'))
            for fila in range(tamaño_matriz):
                fila_nueva=[]
                for columna in range(tamaño_matriz):
                    if fila== columna:
                        fila_nueva.append(1)

                    else:
                        fila_nueva.append(0)
                matriz.append(fila_nueva)
            print(matriz)

        elif ejercicio_ejecutar == 9:
            matriz = []
            tamaño_matriz = int(input('ingrese el tamaño de la matriz que quiere realizar: '))
            for fila in range(tamaño_matriz):
                fila_nueva = []
                for columna in range(tamaño_matriz):
                    if columna == (tamaño_matriz - 1 - fila):
                        fila_nueva.append(1)
                    else:
                        fila_nueva.append(0)
                matriz.append(fila_nueva)

            print(matriz)

        elif ejercicio_ejecutar == 10:
            matriz=[[1,1],[1,1]]
            traspuesta=[]
            for columna in range (len(matriz[0])):
                fila_nueva=[]
                for fila in range(len(matriz)):
                    fila_nueva.append(matriz[fila][columna])
                traspuesta.append(fila_nueva)
            print(traspuesta)
            if matriz == traspuesta:
                print('la matriz es simetrica')
            else:
                print('la matriz no es simetrica')

        elif ejercicio_ejecutar == 11:
            matriz=[
                [1,2,3],
                [1,2,3],
                [1,2,3],
            ]
            resultado=[]
            tamaño_matriz=len(matriz)
            for fila in range(tamaño_matriz):
                fila_nueva=[]
                for columna in range(tamaño_matriz):
                    fila_nueva.append(matriz[tamaño_matriz -1-columna][fila])
                resultado.append(fila_nueva)
            print(resultado)

        elif ejercicio_ejecutar == 12:
            notas=("45, 88, -5, 92, 30, 110, 75, 60, 15")
            lista_notas=notas.split(",")
            print(lista_notas)
            notas_reprobadas=[]
            notas_aprobadas=[]
            for notas in lista_notas:
                notas=int(notas)
                if  notas >= 0 and notas <= 100:
                    if notas >= 60:
                        notas_aprobadas.append(notas)
                    elif notas < 60:
                        notas_reprobadas.append(notas)
                else:
                    continue
            print(f'notas aprobadas {notas_aprobadas}, notas reprobadas {notas_reprobadas}')


        elif ejercicio_ejecutar == 13:
            tareas=[]

            while True:
                print("1. Agregar tarea")
                print("2. Eliminar tarea")
                print("3. Ver resumen")
                print("4. Salir")
                opcion= input('elija una opcion: ')

                if opcion == '1':
                    tarea=input('inrgese la tarea que desea agregar: ')
                    if tarea in tareas:
                        print('error, la actividad ya esta en la lista')
                    
                    else:
                        tareas.append(tarea)
                        print('tarea agregada de forma correcta')
                elif opcion == '2':
                    eliminar_tarea=input('ingrese la tarea qeu desea eliminar: ')
                    if eliminar_tarea in tareas:
                        tareas.remove(eliminar_tarea)
                    else:
                        print('la tarea no existe en la lista')
      
                elif opcion =='3':
                    print(f'total de tareas {len(tareas)}')
                    print(tareas[:3])

                elif opcion == '4':
                    break