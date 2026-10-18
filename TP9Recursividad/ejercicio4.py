def TraspasoBinario(Decimal):
    if Decimal < 2:
        return str(Decimal)
    resto=TraspasoBinario(Decimal // 2)
    texto=resto+ str(Decimal % 2)
    return texto