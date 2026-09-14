def compararParciales(parcial1, parcial2):
    aprobaronAmbos = parcial1 & parcial2
    aprobaronSoloUno = parcial1 ^ parcial2
    aprobaronAlMenosUno = parcial1 | parcial2

    print(f'aprobaron ambos parciales: {aprobaronAmbos}')
    print(f'aprobaron solo uno de los dos: {aprobaronSoloUno}')
    print(f'aprobaron al menos un parcial: {aprobaronAlMenosUno}')
