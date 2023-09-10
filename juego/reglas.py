import random
import juego.funciones as func

def letra_aleatoria(texto):
    return random.choice(texto)

def transformar_lista_a_texto(lista):
    return ''.join(lista)

def reemplazar_letras_por_guion(texto):
    lista_letras = list(texto)
    for i in range(len(texto)):
        if func.es_letra(lista_letras[i]):
            lista_letras[i] = '_'
    return lista_letras

def quitar_caracteres(texto):
    lista_letras = list(texto)
    caracteres_especiales = ['_', ' ']
    for i in range(len(texto)):
        for caracter in caracteres_especiales:
            lista_letras[i] = lista_letras[i].replace(caracter, '')
    return transformar_lista_a_texto(lista_letras)

def borrar_letra(texto, letra):
    lista_letras = list(texto)
    for i in range(len(texto)):
        if lista_letras[i] == letra:
            #lista_letras.remove(letra)
            lista_letras[i] = "_"
            break
    return lista_letras

def agregar_letra(texto, texto2, letra):
    lista_letras = list(texto)
    lista_letras_1 = list(texto2)
    for i in range(len(texto)):
        if lista_letras_1[i] == "_" and lista_letras[i] == letra:
            lista_letras_1[i] = letra
            break
    return lista_letras_1

def mover_letra(texto_inicial, texto_oculto, texto_inicial_muestra, texto_oculto_muestra):
    letra = letra_aleatoria(texto_inicial)
    texto = quitar_caracteres(borrar_letra(texto_inicial, letra))
    nuevo_texto_muestra = borrar_letra(texto_inicial_muestra, letra)
    nuevo_texto_oculto = agregar_letra(texto_oculto, texto_oculto_muestra, letra)
    return texto, nuevo_texto_muestra, nuevo_texto_oculto

def contar_palabras(texto):
    texto = texto.strip()
    palabras = texto.split()
    cantidad_palabras = len(palabras)
    return cantidad_palabras