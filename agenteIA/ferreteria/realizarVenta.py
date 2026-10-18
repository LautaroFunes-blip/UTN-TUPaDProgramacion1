from ferreteria.Venta import Venta
from ferreteria.ItemVenta import ItemVenta
from ferreteria.buscarProducto import buscarProducto
from ferreteria.buscarCliente import buscarCliente
from ferreteria.calcularDescuento import calcularDescuento
from ferreteria.calcularVuelto import calcularVuelto
from ferreteria.leerEntero import leerEntero
from ferreteria.leerDecimal import leerDecimal


def realizarVenta(inventario, clientes, ventas):
    print('--- nueva venta ---')
    dni = leerEntero('ingrese el dni del cliente (0 si es ocasional)')
    if dni == 0:
        cliente = None
    else:
        cliente = buscarCliente(clientes, dni)
        if cliente == None:
            print('el cliente no esta registrado, se toma como ocasional')
    nuevaVenta = Venta(cliente)
    while True:
        codigo = input('ingrese el codigo del producto (fin para terminar)').strip()
        if codigo.lower() == 'fin':
            break
        producto = buscarProducto(inventario, codigo)
        if producto == None:
            print('no existe un producto con ese codigo')
            continue
        cantidad = leerEntero('ingrese la cantidad que quiere llevar')
        if cantidad <= 0:
            print('la cantidad debe ser mayor a cero')
            continue
        if producto.hayStock(cantidad) == False:
            print(f'solo hay {producto.stock} unidades disponibles')
            continue
        item = ItemVenta(producto, cantidad)
        nuevaVenta.agregarItem(item)
        producto.reducirStock(cantidad)
        print(f'se agrego {cantidad} de {producto.nombre}')
    if len(nuevaVenta.items) == 0:
        print('la venta quedo vacia, no se registra')
        return None
    nuevaVenta.descuento = calcularDescuento(nuevaVenta.calcularTotal())
    print(nuevaVenta)
    pago = leerDecimal('ingrese con cuanto paga el cliente')
    print(f'el vuelto es de ${calcularVuelto(nuevaVenta.calcularTotal(), pago)}')
    ventas.append(nuevaVenta)
    return nuevaVenta
