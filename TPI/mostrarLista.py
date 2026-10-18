"""esta funcion se encarga de imprimir de forma prolija y limpia los textos"""
def mostrarLista(listaPaises):
    listaImprimir=[]
    for linea in listaPaises:
        nombre=linea['Nombre'].strip("'")
        poblacion=linea['Poblacion']
        superficie=linea['Superficie']
        continente=linea['Continente'].strip("'")
        cadenaGuardar=f'{nombre},{poblacion},{superficie},{continente}'
        listaImprimir.append(cadenaGuardar)
    return(listaImprimir)
