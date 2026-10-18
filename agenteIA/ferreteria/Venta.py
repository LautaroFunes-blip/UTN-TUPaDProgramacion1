class Venta:
    def __init__(self, cliente):
        self.cliente = cliente
        self.items = []
        self.descuento = 0

    def agregarItem(self, item):
        self.items.append(item)

    def calcularTotal(self):
        total = 0
        for item in self.items:
            total = total + item.calcularSubtotal()
        return total - self.descuento

    def __str__(self):
        if self.cliente == None:
            nombreCliente = 'cliente ocasional'
        else:
            nombreCliente = self.cliente.nombre
        detalle = f'venta de {nombreCliente}\n'
        for item in self.items:
            detalle = detalle + f'   {item}\n'
        detalle = detalle + f'   descuento: ${self.descuento}\n'
        detalle = detalle + f'   total a pagar: ${self.calcularTotal()}'
        return detalle
