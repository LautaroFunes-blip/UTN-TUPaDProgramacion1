from ejercicio2.Alumno import Alumno
from ejercicio2.Nota import Nota


class CargarNotas:
    def __init__(self):
        self.alumnos = []

    def cargarAlumnosNotas(self):
        while True:
            nombreAlumno = input('ingrese el nombre del alumno que quiere cargar (o "fin" para terminar)').title()

            if nombreAlumno == 'Fin':
                print('carga finalizada')
                break

            legajo = input('ingrese el legajo del alumno')

            try:
                legajo = int(legajo)
            except ValueError:
                print('el legajo debe ser un valor numerico')
                continue

            if any(alumno.legajo == legajo for alumno in self.alumnos):
                print(f'ya existe un alumno con el legajo {legajo}, no se puede repetir')
                continue

            nuevoAlumno = Alumno(nombreAlumno, legajo)

            while True:
                catedra = input('ingrese la catedra correspondiente')
                notaExamen = input('ingrese la nota del examen')

                try:
                    notaExamen = float(notaExamen)
                except ValueError:
                    print('las notas solo pueden ser valores numericos')
                    continue

                nuevoAlumno.agregarNota(Nota(catedra, notaExamen))

                seguirSumandoNotas = input('quiere agregar mas notas?').capitalize()
                if seguirSumandoNotas == 'No':
                    break

            self.alumnos.append(nuevoAlumno)

        return self.alumnos
