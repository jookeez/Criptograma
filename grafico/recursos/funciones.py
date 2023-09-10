import pygame as pg
import re
import sys
import generador as generate
import pyperclip as portapapeles
import grafico.recursos.variables as var

def salir():
    pg.quit()
    sys.exit()

def mayuscula(palabra):
    return palabra.upper()

def minuscula(palabra):
    return palabra.lower()

def copiar_texto_portapapeles(palabra):
    portapapeles.copy(palabra)

def pegar_texto_portapapeles():
    return portapapeles.paste()

def centrar(width, height):
    return ((var.WIDTH//2)-(width//2)), ((var.HEIGHT//2)-(height//2))

def centrar_x(width):
    return (var.WIDTH//2)-(width//2)

def centrar_y(height):
    return (var.HEIGHT//2)-(height//2)

def centrar_objetos(x, y, dx, dy):
    return ((x//2)-(dx//2)), ((y//2)-(dy//2))

def eliminar_espacios(texto):
    return texto.replace(" ", "")

def eliminar_comas(texto):
    return texto.replace(",", "")

def cambiar_espacios_por_underscore(texto):
    return texto.replace(" ", "_")

def cambiar_caracter_por_asterisco(texto):
    return texto.replace(texto, "*")

def contador_espacios_blancos(texto):
    cantidad_espacios = texto.count(' ')
    return cantidad_espacios

def palabras_en_texto(texto):
    palabras = texto.split()
    largo_palabra = []
    for palabra in palabras:
        largo_palabra.append(len(palabra))
    return palabras, largo_palabra, len(palabras)

def preajustes(texto):
    texto = eliminar_comas(texto)
    if len(texto) > 35:
        var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO = 3
        var.X_LETRAS_SMALL = 75
        var.Y_LETRAS_SMALL = 99
        var.SIZE_LETRA_SMALL = 70
    else:
        var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO = 2
        var.X_LETRAS_SMALL = 90
        var.Y_LETRAS_SMALL = 120
        var.SIZE_LETRA_SMALL = 86

def separar_frase(texto):
    palabras, largo_palabra, cantidad_palabras = palabras_en_texto(texto)
    #print(palabras, largo_palabra, cantidad_palabras)
    texto = eliminar_espacios(texto)
    frase = []
    largo_fila = []
    contador = 0
    largo = 0
    frase.append([])
    largo_fila.append(contador)

    for i in range(cantidad_palabras):
        if largo < min(len(texto)//var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO, var.MAXIMO_LETRAS_FILA):
            largo += largo_palabra[i]
            largo_fila[contador] = largo
            frase[contador].append(palabras[i])
        else:
            largo = largo_palabra[i]
            largo_fila.append(largo)
            contador += 1
            frase.append([])
            frase[contador].append(palabras[i])
    return frase, largo_fila

def solo_letras(texto):
    patron = re.compile(r'^[a-zA-Z]+$')
    letras = patron.findall(texto)
    resultado = ''.join(letras)
    return resultado

def solo_numeros(texto):
    patron = re.compile(r'^[0-9]+$')
    letras = patron.findall(texto)
    resultado = ''.join(letras)
    return resultado

def letras_y_numeros(texto):
    patron = re.compile(r'^[a-zA-Z0-9]+$')
    letras = patron.findall(texto)
    resultado = ''.join(letras)
    return resultado

def letras_y_espacios(texto):
    patron = re.compile(r'^[a-zA-Z\s]+$')
    letras = patron.findall(texto)
    resultado = ''.join(letras)
    return resultado

def segundos_a_minutos_y_segundos(segundos):
    minutos = int(segundos // 60)
    segundos_restantes = int(segundos % 60)
    return f"{minutos}:{segundos_restantes}"

def abrir_2da_pantalla():
    print("abriendo 2da pantalla")