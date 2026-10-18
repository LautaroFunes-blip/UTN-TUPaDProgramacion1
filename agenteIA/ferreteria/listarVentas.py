def listarVentas(ventas):
    if len(ventas) == 0:
        print('todavia no se registraron ventas')
        return
    for numero, venta in enumerate(ventas, start=1):
        print(f'--- venta {numero} ---')
        print(venta)
