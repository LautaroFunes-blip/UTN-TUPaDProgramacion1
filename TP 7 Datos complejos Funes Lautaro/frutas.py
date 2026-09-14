def agregarFrutas(precios_frutas):
    nuevasFrutas = {
        'Naranja': 1200,
        'Manzana': 1500,
        'Pera': 2300
    }
    precios_frutas.update(nuevasFrutas)
    return precios_frutas

def actualizarPrecios(precios_frutas):
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800
    return precios_frutas

def listarFrutas(precios_frutas):
    listaFrutas = list(precios_frutas.keys())
    return listaFrutas
