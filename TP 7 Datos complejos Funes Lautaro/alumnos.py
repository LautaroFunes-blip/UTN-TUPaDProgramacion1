def cargarAlumnos():
    alumnos = {}
    for i in range(3):
        nombre = input(f'ingrese el nombre del alumno {i + 1}: ')
        while True:
            try:
                nota1 = float(input(f'ingrese la primer nota de {nombre}: '))
                nota2 = float(input(f'ingrese la segunda nota de {nombre}: '))
                nota3 = float(input(f'ingrese la tercer nota de {nombre}: '))
                break
            except ValueError:
                print('ingrese valores numericos validos para las notas')
        alumnos[nombre] = (nota1, nota2, nota3)
    return alumnos

def calcularPromedios(alumnos):
    for nombre, notas in alumnos.items():
        promedio = sum(notas) / len(notas)
        print(f'{nombre} tiene un promedio de {promedio:.2f}')
