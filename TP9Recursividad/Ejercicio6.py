def sumaDigitos(n):
    if n < 10:
        return n
    ultimodigito=n % 10
    print(ultimodigito)
    resto= n // 10
    print(resto)
    ultimodigito2=sumaDigitos(resto)
    resultado=(ultimodigito + ultimodigito2)
    return resultado