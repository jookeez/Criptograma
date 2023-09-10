import juego.funciones as func

def leer_diccionario(cantidad):
    nombre_archivo = f"archivos/diccionario/{cantidad}.txt"
    contenido = []
    with open(nombre_archivo, encoding='utf8') as archivo:
        for linea in archivo:
            linea = linea.replace("\n", "")
            contenido.append(linea)
    return contenido

def revisar(palabra, listado):
    nuevo_listado = []
    largo_palabra = len(palabra)
    diccionario = leer_diccionario(largo_palabra)
    
    i, j = 0, 0
    while i < len(diccionario) and j < len(listado):
        diccionario[i] = func.mayuscula(diccionario[i])
        diccionario[i] = func.quitar_tildes(diccionario[i])
        listado[j] = func.mayuscula(listado[j])
        listado[j] = func.quitar_tildes(listado[j])

        #print(f'{diccionario[i]} {listado[j]}')
        if diccionario[i] == listado[j]:
            nuevo_listado.append(diccionario[i])
            i += 1
            j += 1
        elif diccionario[i] < listado[j]:
            i += 1
        else:
            j += 1

    return nuevo_listado, len(nuevo_listado)