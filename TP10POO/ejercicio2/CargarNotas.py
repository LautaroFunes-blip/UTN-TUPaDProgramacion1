from ejercicio2.Alumno import Alumno
from ejercicio2.Nota import Nota

class CargarNotas:
    def __init__(self):
        self.alumnos=[]



    def cargarAlumnosNotas(self):


        while True:
            nombreAlumno=input('ingrees el nombre del alumno que quiere cargar').title()
        
            if nombreAlumno == 'Fin':
                print('carga finalizada')
                break
            else:
                legajo=input('ingrese el legajo del alumno')
        
        
                try:
                    legajo=int(legajo)
                    iniciacionAlumnos=Alumno(nombreAlumno, legajo)
        
        
                    while True:
                        catedra=input('ingrese la catedra correpondiente')
                        notaExamen=input('ingrese la nota del examen')
        
        
                        try:
                            notaExamen=float(notaExamen)
                            inicialicacionNota=Nota(catedra, notaExamen)
                            self.alumnos.append(inicialicacionNota)
                        except ValueError:
                            print('las notas solo pueden ser valores numericos')
                            continue
        
        
                        seguirSumandoNotas=input('quiere agregar mas notas?').capitalize()
                        if seguirSumandoNotas == 'No':
                            break
                    self.alumnos.append(iniciacionAlumnos)
                except ValueError:
                    print('el legajo debe ser un valor numerico')


        