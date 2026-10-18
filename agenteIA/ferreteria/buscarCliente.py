def buscarCliente(clientes, dni):
    for cliente in clientes:
        if cliente.dni == dni:
            return cliente
    return None
