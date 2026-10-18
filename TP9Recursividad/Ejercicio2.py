def fibonacci(posicion):
    if posicion == 0:
        return 0
    if posicion == 1:
        return 1

    primerNumero= fibonacci(posicion - 1)
    segundoNumero= fibonacci(posicion - 2)
    resultado=(primerNumero + segundoNumero)
    return(resultado)