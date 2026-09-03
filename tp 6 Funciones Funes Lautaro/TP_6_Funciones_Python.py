from math import pi
def hola():
    print('hola mundo')

def saludar_usuario(nombre):
    print(f'hola {nombre}')

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'hola soy {nombre}, {apellido}, tengo {edad}, y vivo en {residencia}')

def calcular_area(radio):
    area= pi * radio**2
    print(area)

def calcular_perimetro(radio):
    diametro= radio *2
    perimetro= pi *diametro
    print(perimetro)

def segundos_a_hora(segundos):
    conversion=segundos/3600
    print(f'tiempo en horas {conversion}')


def tabla_de_multiplicar(numero):
    multiplicador=1
    for i in range(10):
        resultado=numero * multiplicador
        print(f'{numero} x {multiplicador} = {resultado}')
        multiplicador += 1


def operaciones_basicas(a,b):
    suma= a+b
    resta =a-b
    multiplicacion=a *b
    if b == 0:
        division='imposible dividir en cero'
        print('imposible dividir en cero')
    else:
        division=a/b
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    imc=peso/altura
    return imc
def celcius_a_fahrenheit(celcius):
    farhenheit=(celcius*1.8) + 32

    return farhenheit

def calcular_promedio(a,b,c):
    suma=a+b+c
    promedio=suma/3
    return promedio
eleccion=None
while True:
    eleccion=int(input('ingrese el numero del ejercicio que quiere ejecutar o 0 para finalizar la revision'))

    if eleccion == 1:
        hola()
    elif eleccion ==2:
        nombre=input('ingrese su nombre').capitalize()
        saludar_usuario(nombre)
    elif eleccion ==3:
        nombre=input('ingrese su nombre').capitalize()
        apellido=input('ingrese su apellido').capitalize()
        edad=int(input('ingrese su edad'))
        residencia=input('ingrese su lugar de residencia').capitalize()
        informacion_personal(nombre, apellido, edad, residencia)
    elif eleccion ==4:
        radio=float(input('ingrese el radio'))
        area=calcular_area(radio)
        perimetro=calcular_perimetro(radio)
        print(area, perimetro)
    elif eleccion ==5:
        segundos=int(input('ingrese el tiempo en segundos'))
        horas=segundos_a_hora(segundos)
        print(horas)
    elif eleccion ==6:
        numero=int(input('ingrse el numero para hacer la tabla'))
        tabla_de_multiplicar(numero)
    elif eleccion ==7:
        a=int(input('ingrese el primero numero'))
        b=int(input('ingrese el segundo numero'))
        resultados=operaciones_basicas(a,b)
        print(f"Suma: {resultados[0]}, Resta: {resultados[1]}, Multiplicación: {resultados[2]}, División: {resultados[3]}")
    elif eleccion ==8:
        altura=int(input('ingrese su altura en metros'))
        peso=int(input('ingrese su peso en kg'))
        imc=calcular_imc(peso, altura)
        print(imc)
    elif eleccion ==9:
        celcius=int(input('ingrese la temperatura en celcius'))
        celcius_a_fahrenheit(celcius)
    elif eleccion ==10:
        a=int(input('ingrese el primer numero'))
        b=int(input('ingrese el segundo numero'))
        c=int(input('ingrese el tercer numero'))
        promedio=calcular_promedio(a,b,c)
        print(promedio)
    elif eleccion== 0:
        break

    else:
        print('ingrese un ejercicio valido')