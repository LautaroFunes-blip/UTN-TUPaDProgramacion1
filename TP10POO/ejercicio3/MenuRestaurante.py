from ejercicio3.Ingrediente import Ingredientes
from ejercicio3.Plato import Plato
class MenuRestaurante:
    def __init__(self):
        self.platosMenu=[]


    def main(self):
        while True:
            platosnombre=input('ingrese el primer plato que quiere agregar').capitalize()
            if platosnombre == 'Fin':
                break
            precioPlato=input('inrgese el preciodel plato')
            esBebida=input('el plato es una bebida? si o no').capitalize()
            if esBebida == 'Si':
                esBebida=True
            else:
                esBebida=False
            try:
                precioPlato=float(precioPlato)
                Platosfinal=Plato(platosnombre,precioPlato,esBebida)
                if esBebida == False:
                    while True:
                        nombreIngrediente=input('ingrese el nombre del ingrediente o fin para salir').capitalize()
                        if nombreIngrediente == 'Fin':
                            tieneIngredientes=False
                            for i in Platosfinal.listaIngredientes:
                                tieneIngredientes=True
                            if tieneIngredientes == True:
                                self.platosMenu.append(Platosfinal)
                                break
                            else:
                                print('no se puede salir sin agregar ningun ingediente')
                                continue
                        cantidad=input('ingrese la cantidad del ingrediente')
                        try:
                            cantidad=float(cantidad)
                            unidadDeMedida=input('ingrese la unidad de medida del ingrediente')
                            claseIngrediente=Ingredientes(nombreIngrediente, cantidad, unidadDeMedida)
                            Platosfinal.listaIngredientes.append(claseIngrediente)
                        except ValueError:
                            print('ingrese un valor numerico')
                else:
                    self.platosMenu.append(Platosfinal)
                    print('el plato es una bebida')
            except ValueError:
                print('los precios solo pueden ser valores numericos')


        print('------MENÚ-------')
        for producto in self.platosMenu:
            print(f'{producto.nombreCompleto}\nPrecio:${producto.precio}\n')
            if producto.esBebida == True:
                print('bebida')
            else:
                print('Ingredientes \nNombre                   Cantidad     Unidad De Medida')
                for ingredientesmostrar in producto.listaIngredientes:
                    print(f'{ingredientesmostrar.nombre}          {ingredientesmostrar.cantidad}        {ingredientesmostrar.unidadDeMedida}')
            print('--------------------------------------------')