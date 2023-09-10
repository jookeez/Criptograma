import pygame as pg
import os
import grafico.recursos.variables as var
import grafico.recursos.figuras as fig
import grafico.tipografia.fuente as font

def escribir_titulo(texto, size, color_texto):
    porcentaje_desfase_x = 0.05*var.SCALE
    porcentaje_desfase_y = 0.03*var.SCALE
    renderizado = font.agregar_texto(texto, size, color_texto)
    x, y = (var.WIDTH*porcentaje_desfase_x), (var.WIDTH*porcentaje_desfase_y)
    var.SURFACE.blit(renderizado, (x, y))

def escribir_texto_centrado(texto, size, color, x, y, dx, dy):
    #fig.borde(var.COLOR_TEXTO_INFO, x, y, dx, dy, var.GROSOR_BORDE_INFO)
    renderizado = font.agregar_texto(texto, size, color)
    tx, ty = renderizado.get_width(), renderizado.get_height()
    x = ((x + dx//2) - (tx//2))
    y = ((y + dy//2) - (ty//2))
    var.SURFACE.blit(renderizado, (x, y))

def escribir_texto_izquierda(texto, size, color, x, y, dx, dy):
    #fig.borde(var.COLOR_TEXTO_INFO, x, y, dx, dy, var.GROSOR_BORDE_INFO)
    renderizado = font.agregar_texto(texto, size, color)
    var.SURFACE.blit(renderizado, (x, y))

def escribir_texto(texto, size, color, x, y):
    renderizado = font.agregar_texto(texto, size, color)
    var.SURFACE.blit(renderizado, (x, y))

def escribir_parrafo(texto, size, color, x, y, dx, dy):
    #fig.borde(color, x, y, dx, dy, var.GROSOR_BORDE_INFO)
    fuente = pg.font.Font(os.path.join('grafico/tipografia', f'{var.TIPOGRAFIA}'), int(size))
    lineas = texto.splitlines()

    x -= 30*var.SCALE
    y -= 35*var.SCALE
    for linea in lineas:
        texto_renderizado = fuente.render(linea, True, color)
        var.SURFACE.blit(texto_renderizado, (x, y))
        y += 35*var.SCALE