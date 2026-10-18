def contarBloques(n):
    if n <= 0:
        return 0
    cantidadMenor=contarBloques(n-1)
    sumaBloques=(n+cantidadMenor)
    return sumaBloques