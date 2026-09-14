def invertirDiccionario(paises):
    invertido = {}
    for pais, capital in paises.items():
        invertido[capital] = pais
    return invertido
