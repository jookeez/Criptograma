def generar_listado(anagrama):
    listado = generar_combinaciones(anagrama.get_palabra_inicial())
    listado = eliminar_innecesarias(listado, anagrama.get_palabra_inicial(), anagrama.get_largo_anagrama())
    anagrama.set_listado(listado)
    cantidad = anagrama.get_cantidad_anagramas()
    return listado, cantidad

def generar_combinaciones(palabra_inicial):
    listado = combinacion(palabra_inicial)
    listado = ordenar(listado)
    return listado

def combinacion(texto):
    # Caso base: si la palabra tiene solo una letra, retorna una lista con esa letra
    if len(texto) == 1:
        return [texto]

    # Caso recursivo: obtiene la primera letra de la palabra y
    # genera todas las posibles combinaciones de las letras restantes
    primera = texto[0]
    restantes = texto[1:]
    subcombinaciones = generar_combinaciones(restantes)

    # Combina la primera letra con cada una de las subcombinaciones obtenidas
    resultado = []
    for subcomb in subcombinaciones:
        for i in range(len(subcomb) + 1):
            palabra = subcomb[:i] + primera + subcomb[i:]
            resultado.append(palabra)
            
    # La cantidad de combinaciones de palabras es n!-1 letras
    return resultado

def eliminar_innecesarias(listado, palabra_anagrama, size):
    nuevo_listado = []
    for palabra in listado:
        if len(palabra) == size and palabra != palabra_anagrama:
            nuevo_listado.append(palabra)
    return nuevo_listado

def ordenar(listado):
    return sorted(listado)