productosDic=[]
def leerMostrar():
    with open('Productos.txt', 'r') as archivo:
        for productos in archivo:
            """actividad N2"""
            archivoImprimir=productos.strip()
            archivoMostrar=archivoImprimir.split(',')
            print(f'Producto:{archivoMostrar[0]} | Precio:{archivoMostrar[1]} | Cantidad:{archivoMostrar[2]}')
            precio=float(archivoMostrar[1])
            cantidad=int(archivoMostrar[2])
            diccionario={'nombre':archivoMostrar[0], 'precio':precio, 'cantidad':cantidad}
            productosDic.append(diccionario)


"""actividad N3"""
def agregarProductoIndividual():
    with open ('Productos.txt', 'a') as archivo:
        nombre=input('ingresee el nombre del producto').capitalize()
        precio=input('ingrese el precio del producto')
        try:
            precio=float(precio)
            cantidad=input('ingrese la cantidad en stock actual')
            try:
                cantidad=int(cantidad)
                textoAgregar=(f'\n{nombre},{precio},{cantidad}')
                archivo.write(textoAgregar)
                diccionario={'nombre':nombre, 'precio':precio, 'cantidad':cantidad}
                productosDic.append(diccionario)
            except ValueError:
                print('ingrese solo valores numericos')
        except ValueError:
            print('ingrese valores numericos')

def buscarProducto():
    nombreBuscar=input('ingrese el nombre del producto que quiere buscar').capitalize()
    for diccionarios in productosDic:
        if nombreBuscar == diccionarios['nombre']:
            print(diccionarios)
            break
    else:
        print('producto no encontrado')

def salir():
    with open('Productos.txt', 'w') as archivo:
        for diccionario in productosDic:
            textoNuevo=(f"{diccionario['nombre']},{diccionario['precio']},{diccionario['cantidad']}\n")
            archivo.write(textoNuevo)



funcion=None
leerMostrar()
while True:
    funcion=input('ingrese el numero de la funcion que desea realizar \n' \
    '1:agregar producto, \n2:buscar productos \n3:salir')
    try:
        funcion=(int(funcion))
        if funcion == 1:
            agregarProductoIndividual()
        elif funcion == 2:
            buscarProducto()
        elif funcion == 3:
            salir()
    except ValueError:
        print('ingrese un valor numerico')