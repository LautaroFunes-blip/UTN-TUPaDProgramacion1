def listarClientes(clientes):
    if len(clientes) == 0:
        print('no hay clientes cargados')
        return
    print('--- clientes registrados ---')
    for cliente in clientes:
        print(cliente)
