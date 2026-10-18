import importar, buscarPais, ingresoTexto, Coincidencias, mostrarLista, impresionLimpiaBusqeuda

listaPaises=[]


importar.importar(listaPaises)
while True:
    opcion=(input('ingrese una de las opciones a realizar \n0:Salir \n1:buscar/actualizar lista paises \n2:imprimir lista paises \n3:Buscar país \n:'))
    try:
        opcion=int(opcion)
    except ValueError:
        print('ingrese solo valores validos')
        continue
    if opcion==0:
        print('adios')
        break
    elif opcion == 1:
        importar.importar(listaPaises)
    elif opcion==2:
        lineaFinal=mostrarLista.mostrarLista(listaPaises)
        for elemento in lineaFinal:
            print(f'{elemento}')
    elif opcion==3:
        nombreBuscar=ingresoTexto.ingresarTexto()
        resultadoDeBusqueda=buscarPais.buscarPais(listaPaises, nombreBuscar)
        paisEncontradoONo=Coincidencias.hayCoincidencias(resultadoDeBusqueda)
        if paisEncontradoONo:
            impresionLimpiaBusqeuda.impresionLimpia(resultadoDeBusqueda)

        else:
            print(f'no se encontraron coincidencias con {nombreBuscar}')
    else:
        print('ingrese una opcion valida')