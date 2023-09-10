import pygame as pg
import os
import grafico.recursos.variables as var
import grafico.recursos.funciones as func

def general(archivo):
    img = pg.image.load(os.path.join('grafico/imagenes', f'{archivo}.png'))
    x, y = img.get_width()*var.SCALE, img.get_height()*var.SCALE
    img = pg.transform.scale(img, (x, y))
    var.SURFACE.blit(img, (func.centrar(x, y)))

