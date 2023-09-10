import re

def generar_listado(anagrama):
    listado = generar_combinaciones(anagrama.get_palabra_inicial())
    listado = eliminar_innecesarias(listado, anagrama.get_palabra_inicial(), anagrama.get_largo_anagrama())
    anagrama.set_listado(listado)
    cantidad = anagrama.get_cantidad_anagramas()
    return listado, cantidad

def mostrar_listado(anagrama):
    for palabra in anagrama.get_listado():
        print(palabra)

def generar_combinaciones(palabra_inicial):
    listado = combinacion(palabra_inicial)
    listado = no_repetir(listado)
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
            if filtro_consonantes_consecutivas(palabra) and filtro_vocales_consecutivas(palabra) and filtro_consonantes_inicio_fin(palabra) and filtro_mismas_3_vocales_repetidas(palabra) and filtro_mismas_2_vocales_repetidas_mas_vocal_cualquiera(palabra):
                resultado.append(palabra)
            
    # La cantidad de combinaciones de palabras es n! letras
    return resultado

def eliminar_innecesarias(listado, palabra_anagrama, size):
    nuevo_listado = []
    for palabra in listado:
        if len(palabra) == size and palabra != palabra_anagrama:
            nuevo_listado.append(palabra)
    return nuevo_listado

def ordenar(listado):
    return sorted(listado)

def no_repetir(listado):
    return list(set(listado))

# Eliminamos las palabras que tengan 5 o más consonantes consecutivas
def filtro_consonantes_consecutivas(texto):
    regex = r'[aeiouAEIOU]{5}'
    if re.search(regex, texto):
        return False
    else:
        return True

# Eliminamos las palabras que tengan 5 o más vocales consecutivas
def filtro_vocales_consecutivas(texto):
    regex = r'[^aeiouAEIOU]{5}'
    if re.search(regex, texto):
        return False
    else:
        return True

# Eliminamos las palabras que no comiencen o terminen con 3 o más vocales consecutivas
def filtro_consonantes_inicio_fin(texto):
    regex_inicio = r'^[^aeiouAEIOU]{3}'
    regex_fin = r'[^aeiouAEIOU]{3}$'
    if re.search(regex_inicio, texto) or re.search(regex_fin, texto):
        return False
    else:
        return True

# Eliminamos las palabras que contengan la misma vocal 3 o más veces consecutivas
def filtro_mismas_3_vocales_repetidas(texto):
    regex = r'\b\w*([aeiou])\1{2,}\w*\b'
    if re.search(regex, texto):
        return False
    else:
        return True

# Eliminamos las palabras que contengan la misma vocal 2 o más veces consecutivas seguida de otra vocal
def filtro_mismas_2_vocales_repetidas_mas_vocal_cualquiera(texto):
    regex = r'\b\w*([aeiou])\1[aeiou]\w*\b'
    if re.search(regex, texto):
        return False
    else:
        return True