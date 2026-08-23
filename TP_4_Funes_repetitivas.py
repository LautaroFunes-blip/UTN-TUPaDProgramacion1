while True:
    ejecricio_a_ejecutar=int(input('ingrese el numero de ejercicio que desea ejecutar o 0 para finalizar la ejecucion'))

    if ejecricio_a_ejecutar == 1:
        contador=0
        for i in range(0,101):
            print(contador)
            contador+=1
    if ejecricio_a_ejecutar == 2:
        numero_entero=(input('ingrese un numero entero'))
        cantidad=len(numero_entero)
        print(cantidad)
    if ejecricio_a_ejecutar == 3:
        valor_1=int(input('ingrese el primer valor'))
        valor_2=int(input('ingrese el segundo valor'))
        suma=0
        if valor_1 < valor_2:
            contador=valor_1
            for i in range(valor_1+1, valor_2):
                contador+=1
                suma=suma+contador
            print(suma)
        elif valor_1>valor_2:
            contador=valor_2
            for i in range(valor_2+1, valor_1):
                contador+=1
                suma=suma+contador
            print(suma)
    if ejecricio_a_ejecutar == 4:
        valor=None
        total=0
        while valor!= 0:
            valor=int(input('ingrese una secuencia de numeros'))
            total+=valor
        print(total)
    if ejecricio_a_ejecutar == 5:
        import random
        numero=random.randint(0,10)
        numero_usuario=None
        intentos=0

        while numero != numero_usuario:
            numero_usuario=int(input('intente adivinar el numero'))
            if numero_usuario == numero:
                print('felicidades usted gana')
                break
            else:
                print('intentelo otra vez')
                intentos=intentos+1
    if ejecricio_a_ejecutar == 6:
        numero_random=0
        for i in range(0,101):
            numero_random+=1
            if numero_random %2 == 0:
                print(numero_random)
            
    if ejecricio_a_ejecutar == 7:
        numero_usuario=int(input('ingrese un numero entero'))
        suma=0
        for i in range(numero_usuario + 1):
            suma=suma + i
        print(suma)
    if ejecricio_a_ejecutar == 8:
        numeros_pares=[]
        numeros_impares=[]
        numeros_positivos=[]
        numeros_negativos=[]
        cantidad_de_vuetlas=5 #con cambiar esta variable ya se puede elegir la cantidad de veces que se quiera ejecutar el codigo sin limiet

        for i in range(cantidad_de_vuetlas):
            numero_usuario=int(input('ingrese los numeros que desee'))
            if numero_usuario % 2 == 0:
                numeros_pares.append(numero_usuario)
                if numero_usuario > 0:
                    numeros_positivos.append(numero_usuario)
                elif numero_usuario<0:
                    numeros_negativos.append(numero_usuario)
            elif numero_usuario % 2!= 0:
                numeros_impares.append(numero_usuario)
                if numero_usuario > 0:
                    numeros_positivos.append(numero_usuario)
                elif numero_usuario<0:
                    numeros_negativos.append(numero_usuario)
        print(f'numeros pares {numeros_pares}')
        print(f'numeros impares {numeros_impares}')
        print(f'numeros positivos {numeros_positivos}')
        print(f'numeros negativos {numeros_negativos}')

    if ejecricio_a_ejecutar == 9:
        cantidad_valores=6
        suma=0
        for i in range(cantidad_valores):
            numero_usuario=int(input('ingrese un numero'))
            suma+=numero_usuario
        media=suma/cantidad_valores
        print(media)
    if ejecricio_a_ejecutar == 10:
        cadena_a_invertir=input('ingrese la cadena que quiere invertir')
        texto_invertido=cadena_a_invertir[::-1]
        print(texto_invertido)
    elif ejecricio_a_ejecutar == 0:
        break
    else:
        print('ingrese un valor valido')