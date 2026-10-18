class Producto:
    def __init__(self, codigo, nombre, categoria, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.stock = stock

    def hayStock(self, cantidad):
        if cantidad <= self.stock:
            return True
        else:
            return False

    def reducirStock(self, cantidad):
        self.stock = self.stock - cantidad

    def aumentarStock(self, cantidad):
        self.stock = self.stock + cantidad

    def __str__(self):
        return f'[{self.codigo}] {self.nombre} - {self.categoria} - precio: ${self.precio} - stock: {self.stock}'
