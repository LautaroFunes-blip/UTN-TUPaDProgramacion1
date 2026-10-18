def leerDecimal(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print('ingrese solo un numero')
