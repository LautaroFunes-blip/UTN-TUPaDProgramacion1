def analizarFrase():
    frase = input('ingrese una frase: ')
    listaPalabras = frase.lower().split()

    palabrasUnicas = set(listaPalabras)

    recuento = {}
    for palabra in listaPalabras:
        if palabra in recuento:
            recuento[palabra] = recuento[palabra] + 1
        else:
            recuento[palabra] = 1

    print(f'palabras unicas: {palabrasUnicas}')
    print(f'recuento: {recuento}')
