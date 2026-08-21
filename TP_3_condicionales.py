actividad_a_ejecutar=int(input('ingrese la actividad que quiere ejcutar'))
if actividad_a_ejecutar== 1:
    edad=int(input('ingrese su edad'))
    if edad >= 18:
        print('usted es mayor de edad')
    else:
        print('usted es menor de edad')
elif actividad_a_ejecutar == 2:
        nota=float(input('ingrese su nota final'))
        if nota >= 6:
            print('aprobado')
        else:
            print('usted ah desaprobado')
elif actividad_a_ejecutar == 3:
    numero=int(input('ingrese un numero'))
    numero= numero/2
    if numero == 0:
        print('el numero ingresado es par')
    else:
        print('el numero ingresado es impar')
elif actividad_a_ejecutar == 4:
    edad=int(input('ingrese su edad actual'))
    if edad < 12:
        print('la edad se corresponde a un niño')
    elif edad >= 12 and edad < 18:
        print('su edad corresponde a un adoelscente')
    elif edad >= 18 and edad <30:
        print('la edad se corresponde a un joven adulto')
    elif edad >= 30:
        print('usted es un adulto')
elif actividad_a_ejecutar == 5:
    contraseña = input('ingrese su contraseña')
    if 8<= len(contraseña) <=14:
        print('su contraseña en valida')
    else:
        print('pórfavor ingrese una contraseña valida entre 8 y 14 caracteres')

elif actividad_a_ejecutar == 6:
    from statistics import mode, median, mean
    import random
    mi_lista=[random.randint(1,100) for i in range(50)]
    print(mi_lista)
    media=(mean(mi_lista))
    moda=(mode(mi_lista))
    mediana=(median(mi_lista))
    if media < mediana > moda:
        print('sesgo positivo')
    elif moda >mediana > media:
        print('sesgo negativo')
    elif moda == mediana == media:
        print('la lista no presenta sesgo')

elif actividad_a_ejecutar == 7:
    frase=input('inrgese una frase o palabra')
    vocales=['a', 'e', 'i', 'o', 'u']
    ultima_letra=frase.lower()[-1]
    if ultima_letra in vocales:
        print(f'{frase}!')
    else:
        print(frase)
elif actividad_a_ejecutar == 8:
    nombre=input('ingrese su nombre')
    opciones=int(input('ingrese una de las opciones \n 1=nombre completo en mayusculas \n 2=nombre en minusculas \n 3=nombre solo con la primera letra en mayuscula '))

    if opciones == 1:
        nombre=nombre.upper()
        print(nombre)
    elif opciones== 2:
        nombre=nombre.lower()
        print(nombre)
    elif opciones == 3:
        nombre=nombre.capitalize()
        print(nombre)
    else:
        print('ingrese una opcion valida')

elif actividad_a_ejecutar == 9:
        magnitud=int(input('ingrese la magnitud del terremoto'))
        if magnitud < 3:
            print('el temblor fue muy leve')
        elif 3 <= magnitud < 4:
            print('el temblor fue leve')
        elif 4 <= magnitud < 5:
            print('el temblor fue moderado')
        elif 5 <= magnitud < 6:
            print('el temblor fue fuerte')
        elif 6 <= magnitud < 7:
            print('el temblor fue muy fuerte')
        elif magnitud > 7:
            print('terremoto de magnitud extrema')
# elif actividad_a_ejecutar == 10:
    