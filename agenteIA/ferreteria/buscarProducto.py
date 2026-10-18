def buscarProducto(inventario, codigo):
    for producto in inventario:
        if producto.codigo == codigo:
            return producto
    return None
