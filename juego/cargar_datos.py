import juego.archivo as file
import juego.funciones as func
from algoritmos.anagrama import Anagrama
from algoritmos.alfagrama import Alfagrama

def palabra_anagrama():
    listado = file.leer("palabra_anagrama")
    cantidad_lineas = 2
    largo_listado = len(listado)
    numero_random = func.numero_random(0, int(largo_listado/cantidad_lineas)-1)

    id = numero_random
    palabra_inicial = listado[cantidad_lineas*numero_random]
    palabra_oculta = listado[(cantidad_lineas*numero_random)+1]
    nuevo_anagrama = Anagrama(id, palabra_inicial, palabra_oculta, "")
    return nuevo_anagrama

def contrarreloj():
    listado_anagrama = []
    listado = file.leer("contrarreloj")
    cantidad_lineas = 3
    largo_listado = int(len(listado)/cantidad_lineas)

    for i in range(largo_listado):
        id = i
        palabra_inicial = listado[cantidad_lineas*i]
        palabra_oculta = listado[(cantidad_lineas*i)+1]
        pista_anagrama = listado[(cantidad_lineas*i)+2]
        listado_anagrama.append(Anagrama(id, palabra_inicial, palabra_oculta, pista_anagrama))
    return listado_anagrama

def frase_alfagrama():
    listado = file.leer("frase_alfagrama")
    cantidad_lineas = 2
    largo_listado = len(listado)
    numero_random = func.numero_random(0, int(largo_listado/cantidad_lineas)-1)

    '''
    print(largo_listado, cantidad_lineas, numero_random)
    for i in range(len(listado)):
        print(i, listado[i])
    '''

    id = numero_random
    frase = listado[cantidad_lineas*numero_random]
    pista_alfagrama = listado[(cantidad_lineas*numero_random)+1]
    nuevo_alfagrama = Alfagrama(id, frase, pista_alfagrama)
    return nuevo_alfagrama

def contrarreloj_multiple():
    listado_anagrama = []
    listado = file.leer("contrarreloj_multiple")
    posicion = 0
    cantidad_palabras = 0
    cantidad_listados = 0
    largo_listado = len(listado)
    listado_cantidad_palabras = []
    listado_cantidad_palabras.append(0)

    while((cantidad_palabras + cantidad_listados) < largo_listado):
        posicion = posicion + cantidad_palabras + cantidad_listados
        cantidad_palabras = int(listado[posicion])
        cantidad_listados += 1
        listado_cantidad_palabras.append(cantidad_palabras)

    numero_random = func.numero_random(0, int(cantidad_listados)-1)
    revisar_posicion = 0

    for i in range(numero_random):
        revisar_posicion += listado_cantidad_palabras[i]

    revisar_posicion += numero_random

    for i in range(listado_cantidad_palabras[numero_random+1]):
        id = listado_cantidad_palabras[numero_random+1] + i
        palabra_inicial = listado[revisar_posicion+1]
        palabra_oculta = listado[revisar_posicion+1+i]
        listado_anagrama.append(Anagrama(id, palabra_inicial, palabra_oculta, ""))
    return listado_anagrama

def criptocodigo():
    listado = file.leer("criptocodigo")
    cantidad_lineas = 5
    largo_listado = len(listado)
    numero_random = func.numero_random(0, int(largo_listado/cantidad_lineas)-1)

    id = numero_random
    frase = listado[cantidad_lineas*numero_random]
    pista_alfagrama = listado[(cantidad_lineas*numero_random)+3]
    nuevo_alfagrama = Alfagrama(id, frase, pista_alfagrama)

    id = numero_random
    palabra_inicial = listado[(cantidad_lineas*numero_random)+1]
    palabra_oculta = listado[(cantidad_lineas*numero_random)+2]
    pista_anagrama = listado[(cantidad_lineas*numero_random)+4]
    nuevo_anagrama = Anagrama(id, palabra_inicial, palabra_oculta, pista_anagrama)

    return nuevo_alfagrama, nuevo_anagrama
