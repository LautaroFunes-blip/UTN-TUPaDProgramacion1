def potencias(numero, exponente):
    if exponente == 0:
        return 1
    resultado= numero * potencias(numero, exponente-1)
    return resultado