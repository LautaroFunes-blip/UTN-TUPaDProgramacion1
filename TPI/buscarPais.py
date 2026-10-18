def buscarPais(listaPaises, nombreBuscar):
    listaCoincidencias=[]
    for pais in listaPaises:
        nombreListado=(pais['Nombre']).lower()
        if nombreBuscar in nombreListado:
            (listaCoincidencias.append(pais))
    return(listaCoincidencias)
