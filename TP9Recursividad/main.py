import Ejercicio1, Ejercicio2, Ejercicio3, ejercicio4, Ejercicio5, Ejercicio6, Ejercicio7, Ejercicio8

while True:
    actividad=int(input('ingrese el numero de ejercicio que quiere ejecutar o 0 para salir'))

    if actividad == 0:
        break
    elif actividad == 1:
        n=int(input('ingrese un valor para calcular el factorial'))
        for i in range(1, n + 1):
            print(i, Ejercicio1.factorial(i))
    elif actividad ==2:
        posicion=int(input('ingrese la posicion de la serie fibonacci'))
        for a in range(posicion + 1):
            resultadoFibo=Ejercicio2.fibonacci(a)
            print(resultadoFibo)

    elif actividad == 3:
        numero=int(input('ingrese un valor para la potencia'))
        exponente=int(input('ingrese un valor para el exponente'))
        resultadopotencia=Ejercicio3.potencias(numero, exponente)
        print(resultadopotencia)


    elif actividad == 4:
        Decimal=int(input('ingrese el valor decimal que quiere pasar a decimal'))
        binario=ejercicio4.TraspasoBinario(Decimal)
        print(binario)


    elif actividad == 5:
        palabra=input('ingrese una palabra')
        palindromo=Ejercicio5.esPalindromo(palabra)
        if palindromo == True:
            print('la palabra es un palidromo')
        else:
            print('esta palabra no es un palindromo')



    elif actividad == 6:
        n=int(input('ignrese un numero'))
        resultado=Ejercicio6.sumaDigitos(n)
        print(resultado)


    elif actividad == 7:
        n=int(input('ingrese la cantidad de bloques en el nivel mas bajo'))
        totalBloques=Ejercicio7.contarBloques(n)
        print(totalBloques)



    elif actividad == 8:
        numero=int(input('ingrese el numero a comprobar'))
        digitos=int(input('ingrese el digito que quiere contar dentro del numero'))
        cantidadCoincidencias=Ejercicio8.contarDigitos(numero, digitos)
        print(cantidadCoincidencias)