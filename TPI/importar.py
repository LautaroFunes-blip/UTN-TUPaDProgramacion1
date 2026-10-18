"""esta funcion se encarga de verificar si el archivo existe y lo convierte y formatea para su manejo
y lo guarda en una lista con diccionarios anidados, para facilitar el trabajo con cada dato
si el archivo no existe lo crea y escribe sobre el para luego realizar el mismo procedimiento sobre si mismo"""

def importar(listaPaises):
    try:
        with open('dataset.csv', 'r', encoding='utf-8') as archivo:
            listaPaises.clear()
            for lineas in archivo:
                lienasViejas=lineas.strip()
                lineasNuevas=lienasViejas.split(',')
                nombre=lineasNuevas[0]
                try:
                    poblacion=int(lineasNuevas[1])
                    superficie=int(lineasNuevas[2])
                    continente=lineasNuevas[3]
                    lineasGuardar={'Nombre':nombre, 'Poblacion':poblacion, 'Superficie':superficie, 'Continente':continente}
                    listaPaises.append(lineasGuardar)
                except (ValueError, IndexError):
                    print('El CSV presenta un error, de una linea incompleta o una linea vacia')
                    continue    
    except FileNotFoundError:
        with open('dataset.csv', 'a', encoding='utf-8') as archivo: 
            datos='nombre,poblacion,superficie,continente \nArgentina,45376763,2780400,América \nJapón,125800000,377975,Asia \nBrasil,213993437,8515767,América \nAlemania,83149300,357022,Europa'
            archivo.write(datos)
        importar(listaPaises)