from ferreteria.Producto import Producto
from ferreteria.Cliente import Cliente


def cargarDatosIniciales(inventario, clientes):
    inventario.append(Producto('A01', 'Martillo', 'Herramientas', 8500, 10))
    inventario.append(Producto('A02', 'Destornillador', 'Herramientas', 3200, 25))
    inventario.append(Producto('B01', 'Tornillos x100', 'Fijaciones', 4500, 40))
    inventario.append(Producto('C01', 'Pintura Blanca 4L', 'Pinturas', 18000, 8))
    clientes.append(Cliente('Juan Perez', 30111222, '221-5551234'))
    clientes.append(Cliente('Maria Gomez', 28999888, '221-5559876'))
    print('datos iniciales cargados')
