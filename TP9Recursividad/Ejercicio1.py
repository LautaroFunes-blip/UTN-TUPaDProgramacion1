def factorial(n):
    if n<=1:
        return 1
    reduccion= n -1
    respuesta= factorial(reduccion)
    resultado= n * respuesta
    return resultado