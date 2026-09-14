def gestionarStock(productos):
    while True:
        opcion = input('ingrese la opcion que quiere realizar' \
        '\n 1=Consultar stock \n 2=Agregar unidades a un producto existente' \
        '\n 3=Agregar producto nuevo \n 4=Salir \n')
        try:
            opcion = int(opcion)
            if opcion == 1:
                nombre = input('ingrese el producto que quiere consultar: ')
                if nombre in productos:
                    print(f'stock de {nombre}: {productos[nombre]}')
                else:
                    print('ese producto no existe')
            elif opcion == 2:
                nombre = input('ingrese el producto al que quiere agregar stock: ')
                if nombre in productos:
                    cantidad = int(input('ingrese la cantidad a agregar: '))
                    productos[nombre] = productos[nombre] + cantidad
                else:
                    print('ese producto no existe, use la opcion 3 para agregarlo')
            elif opcion == 3:
                nombre = input('ingrese el nombre del nuevo producto: ')
                if nombre not in productos:
                    cantidad = int(input('ingrese el stock inicial: '))
                    productos[nombre] = cantidad
                else:
                    print('ese producto ya existe')
            elif opcion == 4:
                break
            else:
                print('ingrese una opcion valida')
        except ValueError:
            print('ingrese un valor numerico valido')
    return productos
