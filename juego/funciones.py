import pygame as pg
import os
import random
import sys
import threading
import time
from unidecode import unidecode
import juego.variables as j_var
import grafico.recursos.variables as var

def mayuscula(palabra):
    return palabra.upper()

def minuscula(palabra):
    return palabra.lower()

def cantidad_vocales(texto):
    vocales = "AÁEÉIÍOÓUÚ"
    cantidad = 0
    for letra in texto:
        if letra in vocales:
            cantidad += 1
    return cantidad

def quitar_tildes(palabra):
    return unidecode(palabra)

def cantidad_consonantes(texto):
    consonantes = "BCDFGHJKLMNPQRSTVWXYZ"
    cantidad = 0
    for letra in texto:
        if letra in consonantes:
            cantidad += 1
    return cantidad

def es_letra(letra):
    abc = "AÁBCDEÉFGHIÍJKLMNOÓPQRSTUÚVWXYZ"
    if letra in abc:
        return True
    else:
        return False

def salir():
    os.system('cls' if os.name == 'nt' else 'clear')
    sys.exit()

def limpiar_consola():
    os.system('cls' if os.name == 'nt' else 'clear')

def numero_random(limite_inferior, limite_superior):
    return random.randint(limite_inferior, limite_superior)

def separar_por_palabras(texto):
    palabras = texto.split()
    return palabras 

def sumar_puntaje_parcial():
    for i, valor in enumerate(j_var.PUNTAJE_PARTICIPANTES_PARCIAL):
        j_var.PUNTAJE_PARTICIPANTES[i] += valor

def paneles_por_defecto():
    var.ID_LISTADO_PANELES = ["13", "3", "1", "9", "2", "10", "2"]

def reiniciar_tiempo_jugado():
    j_var.TIEMPO_TOTAL_JUEGO_SEGUNDOS = 0

def reiniciar_puntaje_parcial():
    j_var.PUNTAJE_PARTICIPANTES_PARCIAL = [0, 0, 0, 0]

def reiniciar_puntaje_total():
    j_var.PUNTAJE_PARTICIPANTES = [0, 0, 0, 0]

def reiniciar_participantes():
    j_var.NOMBRE_PARTICIPANTES = ["", "", "", ""]

def segundos_a_minutos_segundos(total_segundos):
    minutos = total_segundos // 60
    segundos = total_segundos % 60
    return f'{minutos:01}:{segundos:02}'

def cronometro_iniciado():
    if j_var.CRONOMETRO_INICIADO:
        tiempo_transcurrido = pg.time.get_ticks() - j_var.CRONOMETRO_INICIO
        segundos = tiempo_transcurrido // 1000
        minutos = segundos // 60
        segundos %= 60
        j_var.TIEMPO_PARCIAL_JUEGO = f'{minutos:01}:{segundos:02}'
        if j_var.AUXILIAR_INICIO == segundos:
            j_var.AUXILIAR_INICIO += 1
            j_var.TIEMPO_TOTAL_JUEGO_SEGUNDOS += 1

def reiniciar_cronometro():
    j_var.TIEMPO_PARCIAL_JUEGO = "0:00"
    j_var.CRONOMETRO_INICIO = 0
    j_var.CRONOMETRO_INICIADO = False
    j_var.AUXILIAR_INICIO = 1

def iniciar_cronometro():
    j_var.CRONOMETRO_INICIADO = True
    j_var.CRONOMETRO_INICIO = pg.time.get_ticks()

def detener_cronometro():
    j_var.CRONOMETRO_INICIADO = False

