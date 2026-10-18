def contarDigitos(numero, digitos):
    if numero <= 0:
        return 0
    elif digitos < 0:
        return 0
    numeroFinal=numero % 10
    nuevoNumero=numero // 10
    coincidencia=contarDigitos(nuevoNumero, digitos)
    sumaSiNo=0
    if numeroFinal == digitos:
        sumaSiNo=1
    coincidencia = sumaSiNo + coincidencia
    return(coincidencia)