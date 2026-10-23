from ejercicio4.ComponenteCPU import ComponentesCPU
from ejercicio4.Computadora import Computadora

class CostoComputadora:
    def __init__():
        pass

    def main():
        marcaPC=input('ingrese la marca de la pc').capitalize()
        modeloPC=input('ingrese el modelo de la pc')
        claseComputadora=Computadora(marcaPC, modeloPC)
        while True:
            componenteIndividual=input('ingrese el tipo de componente correspondiente o Fin para salir:').title()
            if componenteIndividual == 'Fin':
                break
            marcaComponente=input('ingrese la marca del componente:')
            cantidad=input('ingrese la cantidad de este tipo de componente que tiene la pc:')
            try:
                cantidad=int(cantidad)
                precioComponente=input('ingrese el precio del componente de forma individual:')
                try:
                    precioComponente=float(precioComponente)

                    claseComponentes=ComponentesCPU(componenteIndividual,marcaComponente,cantidad,precioComponente)
                    claseComputadora.componentesCPU.append(claseComponentes)

                except ValueError:
                    print('el precio solo puede ser valor numerico')

            except ValueError:
                print('la cantidad solo puedes ser valor numerico')

        totalFinal=0
        print('---------COMPUTADORA----------')
        print('componente   Marca   Catnidad   precio x unidad   Subtotal')
        for producto in claseComputadora.componentesCPU:
            totalProductos= producto.precio * producto.cantidad
            print(f'producto.componente,    producto.marca,    producto.cantidad,    producto.precio,    ${totalProductos}\n')
            totalFinal= totalFinal+totalProductos
        print('subtotal:',totalFinal)