from ejercicio5.Vivienda import Vivienda

class Barrio:
    def __init__(self, nombre: str, empresa_constructora: str):
        self.nombre = nombre
        self.empresa_constructora = empresa_constructora
        self.viviendas: list[Vivienda] = []

    def agregar_vivienda(self, vivienda: Vivienda):
        self.viviendas.append(vivienda)

    # a) Suma de superficieTerreno de todas las viviendas asociadas
    def get_superficie_total_terreno(self) -> float:
        return sum(v.superficie_terreno for v in self.viviendas)

    # b) Suma de superficieTerreno filtrando por manzana
    def get_superficie_total_terreno_x_manzana(self, manzana: str) -> float:
        return sum(
            v.superficie_terreno 
            for v in self.viviendas 
            if v.manzana.upper() == manzana.upper()
        )

    # d) Suma de metros cubiertos reutilizando get_metros_cuadrados_cubiertos()
    def get_superficie_total_cubierta(self) -> float:
        return sum(v.get_metros_cuadrados_cubiertos() for v in self.viviendas)