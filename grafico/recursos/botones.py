import pygame as pg
import os
import grafico.recursos.variables as var
import grafico.recursos.funciones as func
import grafico.tipografia.fuente as font
import grafico.recursos.color as color

def boton_inicio(nombre, imagen, desfase_x, desfase_y):
    ajuste_y = 130*var.SCALE
    desfase_x *= var.SCALE
    desfase_y *= var.SCALE

    img = pg.image.load(os.path.join('grafico/imagenes/botones', f'{imagen}.png'))
    x, y = img.get_width()*var.SCALE, img.get_height()*var.SCALE
    img = pg.transform.scale(img, (x, y))
    x, y = func.centrar(x, y)
    x, y = (x+desfase_x), (y+desfase_y+ajuste_y)
    var.SURFACE.blit(img, (x, y))
    
    texto = nombre
    size = 56
    color_texto = color.AMARILLO
    renderizado = font.agregar_texto(texto, size, color_texto)

    x, y = renderizado.get_width(), renderizado.get_height()
    x, y = func.centrar(x, y)
    x, y = (x+desfase_x), (y+desfase_y+ajuste_y)
    var.SURFACE.blit(renderizado, (x, y))