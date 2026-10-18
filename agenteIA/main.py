from ferreteria.cargarDatosIniciales import cargarDatosIniciales
from ferreteria.mostrarMenu import mostrarMenu
from ferreteria.leerEntero import leerEntero
from ferreteria.leerDecimal import leerDecimal
from ferreteria.registrarProducto import registrarProducto
from ferreteria.buscarProducto import buscarProducto
from ferreteria.listarProductos import listarProductos
from ferreteria.registrarCliente import registrarCliente
from ferreteria.buscarCliente import buscarCliente
from ferreteria.listarClientes import listarClientes
from ferreteria.realizarVenta import realizarVenta
from ferreteria.listarVentas import listarVentas
from ferreteria.calcularDescuento import calcularDescuento
from ferreteria.calcularVuelto import calcularVuelto


def main():
    inventario = []
    clientes = []
    ventas = []
    cargarDatosIniciales(inventario, clientes)
    print('bienvenido a la ferreteria')
    listarProductos(inventario)

    while True:
        mostrarMenu()
        opcion = leerEntero('ingrese el numero de la opcion que quiere ejecutar')

        if opcion == 1:
            registrarProducto(inventario)
        elif opcion == 2:
            listarProductos(inventario)
        elif opcion == 3:
            codigo = input('ingrese el codigo del producto a buscar').strip()
            producto = buscarProducto(inventario, codigo)
            if producto == None:
                print('no se encontro ningun producto con ese codigo')
            else:
                print(producto)
        elif opcion == 4:
            registrarCliente(clientes)
        elif opcion == 5:
            listarClientes(clientes)
        elif opcion == 6:
            dni = leerEntero('ingrese el dni del cliente a buscar')
            cliente = buscarCliente(clientes, dni)
            if cliente == None:
                print('no se encontro ningun cliente con ese dni')
            else:
                print(cliente)
        elif opcion == 7:
            realizarVenta(inventario, clientes, ventas)
        elif opcion == 8:
            listarVentas(ventas)
        elif opcion == 9:
            monto = leerDecimal('ingrese el monto para calcular el descuento')
            print(f'el descuento es de ${calcularDescuento(monto)}')
        elif opcion == 10:
            total = leerDecimal('ingrese el total a pagar')
            pago = leerDecimal('ingrese con cuanto paga el cliente')
            print(f'el vuelto es de ${calcularVuelto(total, pago)}')
        elif opcion == 0:
            print('hasta luego')
            break
        else:
            print('opcion invalida')


if __name__ == '__main__':
    main()
