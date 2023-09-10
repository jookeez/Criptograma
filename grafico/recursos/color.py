import pygame as pg
import grafico.recursos.variables as var

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
AMARILLO = (250, 226, 72)
CELESTE = (0, 129, 166)
MORADO = (41, 23, 57)
FUCSIA = (120, 24, 81)
BORDE_AMARILLO = AMARILLO
BORDE_CELESTE = CELESTE
BORDE_ROJO = ROJO
BORDE_FUCSIA = (231, 29, 104)
BORDE_VERDE = (31, 166, 55)
BORDE_NARANJO = (200, 116, 19)

def background():
    color_inicio = FUCSIA
    color_final = MORADO

    for y in range(var.HEIGHT):
        color_intermedio = (
            color_inicio[0] + (y * (color_final[0] - color_inicio[0])) // var.HEIGHT,
            color_inicio[1] + (y * (color_final[1] - color_inicio[1])) // var.HEIGHT,
            color_inicio[2] + (y * (color_final[2] - color_inicio[2])) // var.HEIGHT
        )
        pg.draw.line(var.SURFACE, color_intermedio, (0, y), (var.WIDTH, y))