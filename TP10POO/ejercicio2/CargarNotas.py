from ejercicio2.Alumno import Alumno
from ejercicio2.Nota import Notas

class CargarNotas:
    def __init__(self):
        self.alumnosLista=[]
    def main(self):
        while True:
            nombreAlumnos=input('ingrese el nombre del alumno').title()
            if nombreAlumnos == 'Fin':
                break
            legajoAlumnos=input('ingrese el legajo de alumno')
            try:
                legajoAlumnos=int(legajoAlumnos)
                banderaAlumnos=False
                for alumno in self.alumnosLista:
                    if alumno.legajo == legajoAlumnos:
                        banderaAlumnos=True
                        alumnoClase=alumno
                        break
                if banderaAlumnos == False:
                    alumnoClase=Alumno(nombreAlumnos, legajoAlumnos)
                    self.alumnosLista.append(alumnoClase)
                while True:
                    materia=input('ingrese el nombre de la catedra')    
                    nota=input('ingrese la nota de la materia')
                    try:
                        nota=float(nota)
                        notaClase=Notas(materia, nota)
                        alumnoClase.notas.append(notaClase)
                            
                    except ValueError:
                        print('las notas deben ser valores numericos') 
                        continue
                    agregarMasNotas=input('quiere agregar mas notas? si o no').capitalize()
                    if agregarMasNotas == 'No':
                        break

            except ValueError:
                print('el legajo debe ser un valor entero')

        for alumnosNotas in self.alumnosLista:
            print(alumnosNotas.nombreCompleto)
            for notaFinal in alumnosNotas.notas:
                print(notaFinal.catedra)
            print(alumnosNotas.promedio())