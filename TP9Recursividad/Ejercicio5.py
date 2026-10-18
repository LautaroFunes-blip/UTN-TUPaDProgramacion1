def esPalindromo(palabra):
    if len(palabra) <= 1:
        return 0
    elif palabra[0] != palabra[-1]:
        return False
    centros=palabra[1:-1]
    palindromo=esPalindromo(centros)
    return palindromo