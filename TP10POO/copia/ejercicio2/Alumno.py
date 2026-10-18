from ejercicio2.Nota import Nota


class Alumno:
    def __init__(self, nombreCompleto: str, legajo: int):
        self.nombreCompleto = nombreCompleto
        self.legajo = legajo
        self.notas = []

    def agregarNota(self, nota: Nota):
        self.notas.append(nota)

    def promedio(self):
        if len(self.notas) == 0:
            return 0
        return sum(nota.notaExamen for nota in self.notas) / len(self.notas)
