def listarProductos(inventario):
    if len(inventario) == 0:
        print('no hay productos cargados')
        return
    print('--- productos en stock ---')
    for producto in inventario:
        print(producto)
