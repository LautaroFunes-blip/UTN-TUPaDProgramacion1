from ferreteria.Producto import Producto
from ferreteria.buscarProducto import buscarProducto
from ferreteria.leerEntero import leerEntero
from ferreteria.leerDecimal import leerDecimal


def registrarProducto(inventario):
    codigo = input('ingrese el codigo del producto').strip()
    if buscarProducto(inventario, codigo) != None:
        print('ya existe un producto con ese codigo')
        return None
    nombre = input('ingrese el nombre del producto').title()
    categoria = input('ingrese la categoria del producto').title()
    precio = leerDecimal('ingrese el precio del producto')
    stock = leerEntero('ingrese el stock inicial del producto')
    nuevoProducto = Producto(codigo, nombre, categoria, precio, stock)
    inventario.append(nuevoProducto)
    print('producto registrado')
    return nuevoProducto
