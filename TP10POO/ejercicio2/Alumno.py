class Alumno:
    def __init__(self, nombrecompleto:str, legajo:int):
        self.nombreCompleto=nombrecompleto
        self.legajo=legajo
        self.notas=[]


    def promedio(self):
        totalSuma=0
        for notasvariable in self.notas:
            totalSuma += notasvariable.nota
        promedioFinal=totalSuma / len(self.notas)
        return promedioFinal