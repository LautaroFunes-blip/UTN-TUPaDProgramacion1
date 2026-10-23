class Barrio:
    def __init__(self, nombre: str, empresaConstructora: str):
        self.nombre = nombre
        self.empresaConstructora = empresaConstructora
        self.viviendas = []

    def agregarVivienda(self, vivienda):
        self.viviendas.append(vivienda)

    def getSuperficieTotalTerreno(self):
        total = 0
        for vivienda in self.viviendas:
            total += vivienda.superficieTerreno
        return total

    def getSuperficieTotalTerrenoXManzana(self, manzana: str):
        total = 0
        for vivienda in self.viviendas:
            if vivienda.manzana == manzana:
                total += vivienda.superficieTerreno
        return total

    def getSuperficieTotalCubierta(self):
        total = 0
        for vivienda in self.viviendas:
            total += vivienda.getMetrosCuadradosCubiertos()
        return total
