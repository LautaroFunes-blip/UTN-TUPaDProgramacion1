# tp_1 secuenciales
#actividad N1
actividad_ejecutar=int(input('ingrese el numero de actividad que quiere ejecutar'))
if actividad_ejecutar == 1:

    print('hola mundo')

#actividad N2
elif actividad_ejecutar == 2:
        
    nombre=input('ingrese su nombre').capitalize()
    print(f'hola {nombre}')

#actividad N3 
elif actividad_ejecutar == 3:
        
    nombre=input('ingrese su nombre').capitalize()
    apellido=input('ingrese su apellido').capitalize()
    ciudad=input('ingrese el pais donde reside').capitalize()
    edad=int(input('ingrese su edad'))
    print(f'hola soy {nombre} {apellido}, tengo {edad} años y vivo en {ciudad}')

elif actividad_ejecutar==4:
    from math import pi
    radio=float(input('ingrese el radio del circulo'))
    perimetro= 2*pi*radio
    print(perimetro)
    area= pi *radio**2
    print(area)

elif actividad_ejecutar == 5:
    segundos=int(input('ingrese el tiempo en segundos'))
    horas= segundos/3600
    print(horas)
elif actividad_ejecutar == 6:
    numero=float(input('ingrese el numero de la tabla que quier generar'))
    multiplicador=10
    for i in range(multiplicador):
        resultado=numero*multiplicador
        print(resultado)
        multiplicador-=1

elif actividad_ejecutar == 7:
    while True:
        numero_1=float(input('ingrese el primer valor'))
        numero_2=float(input('ingrese el segundo valor'))
        if numero_1 > 0 and numero_2 >= 0:
            suma=numero_1+numero_2
            multiplicacion=numero_1*numero_2
            resta=numero_1-numero_2
            divicion=numero_1/numero_2
            print(f'suma={suma} \n multiplicacion={multiplicacion} \n resta={resta} \n divicion={divicion}')
            break
        else:
            print('el valor no puede ser igual a cero')

elif actividad_ejecutar == 8:
    altura=float(input('ingrese su altura, en metros'))
    peso=float(input('ingrese su peso'))

    imc=peso/altura**2

    print(imc)

elif actividad_ejecutar == 9:
    temperatura_celcius=float(input('ingrese la temperatura en grados celcius'))
    temperatura_fahrenheit=(9/5)*temperatura_celcius +32
    print(temperatura_fahrenheit)

elif actividad_ejecutar == 10:
    while True:
        numeros=[]
        cantidad=int(input('ingrese la catidad de numeros que quiere ingresar'))
        if cantidad > 0:
            for i in range(cantidad):
                numeros_input=float(input('ingrese los numeros para calcular el promedio'))
                numeros.append(numeros_input)
            suma=sum(numeros)
            promedio=suma/cantidad
            print(promedio)
            break
        else:
            print('ingrese un valor valido para el sistema')
