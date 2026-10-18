from ferreteria.Cliente import Cliente
from ferreteria.buscarCliente import buscarCliente
from ferreteria.leerEntero import leerEntero


def registrarCliente(clientes):
    dni = leerEntero('ingrese el dni del cliente')
    if buscarCliente(clientes, dni) != None:
        print('ya existe un cliente con ese dni')
        return None
    nombre = input('ingrese el nombre y apellido del cliente').title()
    telefono = input('ingrese el telefono del cliente')
    nuevoCliente = Cliente(nombre, dni, telefono)
    clientes.append(nuevoCliente)
    print('cliente registrado')
    return nuevoCliente
