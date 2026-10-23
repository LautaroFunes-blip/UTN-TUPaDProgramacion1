from ejercicio5.Habitacion import Habitacion

class Vivienda:
    def __init__(self,calle:str,numero:int,manzana:str,nroCasa:int, superficieTerreno:float):
        self.calle=calle
        self.numero=numero
        self.manzana=manzana
        self.nroCasa=nroCasa
        self.superficieTerreno=superficieTerreno
        self.habitacionLista=[]


    def agregar_habitacion(self, habitacion: Habitacion):
        self.habitaciones.append(habitacion)

    def get_metros_cuadrados_cubiertos(self) -> float:
        
        total_cubierto = sum(h.metros_cuadrados for h in self.habitaciones)
        
        if total_cubierto > self.superficie_terreno:
            raise Exception("La superficie cubierta no puede ser mayor a la superficie del terreno")
        
        return total_cubierto