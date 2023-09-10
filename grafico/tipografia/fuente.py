import pygame as pg
import os
import grafico.recursos.variables as var

def agregar_texto(texto, size, color):
    texto = str(texto)
    fuente = pg.font.Font(os.path.join('grafico/tipografia', f'{var.TIPOGRAFIA}'), int(size))
    texto_renderizado = fuente.render(texto, True, color)
    return texto_renderizado
