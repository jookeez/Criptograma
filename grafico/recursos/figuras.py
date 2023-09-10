import pygame as pg
import grafico.recursos.variables as var
import grafico.tipografia.fuente as font

def rectangulo(color, x, y, dx, dy):
    x = int(x)
    y = int(y)
    dx = int(dx)
    dy = int(dy)
    pg.draw.rect(var.SURFACE, color, (x, y, dx, dy))

def borde(color, x, y, dx, dy, grosor):
    x = int(x)
    y = int(y)
    dx = int(dx)
    dy = int(dy)
    grosor = int(max(1, grosor))
    pg.draw.rect(var.SURFACE, color, (x, y, dx, dy), grosor)

def linea(color, x, y, dx, dy):
    x = int(x)
    y = int(y)
    dx = int(dx)
    pg.draw.line(var.SURFACE, color, (x, y), (dx, dy))

def circulo(color, x, y, radio):
    x = int(x)
    y = int(y)
    radio = int(radio)
    pg.draw.circle(var.SURFACE, color, (x, y), radio)

def rectangulo_redondeado(color, x, y, dx, dy, radio):
    x = int(x)
    y = int(y)
    dx = int(dx)
    dy = int(dy)
    radio = int(radio)
    pg.draw.circle(var.SURFACE, color, (x + radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color, (x + dx - radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color, (x + radio, y + dy - radio), radio)
    pg.draw.circle(var.SURFACE, color, (x + dx - radio, y + dy - radio), radio)
    pg.draw.rect(var.SURFACE, color, (x, y + radio, dx, dy - radio * 2))
    pg.draw.rect(var.SURFACE, color, (x + radio, y, dx - radio * 2, dy))

def rectangulo_redondeado_con_borde(color_fondo, color_borde, x, y, dx, dy, radio, grosor):
    x = int(x)
    y = int(y)
    dx = int(dx)
    dy = int(dy)
    radio = int(radio)
    grosor = int(max(1, grosor))

    pg.draw.circle(var.SURFACE, color_borde, (x + radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + dx - radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + radio, y + dy - radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + dx - radio, y + dy - radio), radio)
    pg.draw.rect(var.SURFACE, color_borde, (x, y + radio, dx, dy - radio * 2))
    pg.draw.rect(var.SURFACE, color_borde, (x + radio, y, dx - radio * 2, dy))

    pg.draw.circle(var.SURFACE, color_fondo, (x + radio + grosor, y + radio + grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + dx - radio - grosor, y + radio + grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + radio + grosor, y + dy - radio - grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + dx - radio - grosor, y + dy - radio - grosor), radio)
    pg.draw.rect(var.SURFACE, color_fondo, (x + grosor, y + radio + grosor, dx - 2 * grosor, dy - radio * 2 - grosor))
    pg.draw.rect(var.SURFACE, color_fondo, (x + grosor + radio + grosor, y + grosor, dx - radio * 2 - grosor, dy - 2 * grosor))

def rectangulo_redondeado_con_borde_y_texto(texto, size, color, color_fondo, color_borde, x, y, dx, dy, radio, grosor):
    x = int(x)
    y = int(y)
    dx = int(dx)
    dy = int(dy)
    size = int(size)
    radio = int(radio)
    grosor = int(max(1, grosor))

    pg.draw.circle(var.SURFACE, color_borde, (x + radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + dx - radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + radio, y + dy - radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + dx - radio, y + dy - radio), radio)
    pg.draw.rect(var.SURFACE, color_borde, (x, y + radio, dx, dy - radio * 2))
    pg.draw.rect(var.SURFACE, color_borde, (x + radio, y, dx - radio * 2, dy))

    pg.draw.circle(var.SURFACE, color_fondo, (x + radio + grosor, y + radio + grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + dx - radio - grosor, y + radio + grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + radio + grosor, y + dy - radio - grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + dx - radio - grosor, y + dy - radio - grosor), radio)
    pg.draw.rect(var.SURFACE, color_fondo, (x + grosor, y + radio + grosor, dx - 2 * grosor, dy - radio * 2 - grosor))
    pg.draw.rect(var.SURFACE, color_fondo, (x + grosor + radio + grosor, y + grosor, dx - radio * 2 - grosor, dy - 2 * grosor))

    renderizado = font.agregar_texto(texto, size, color)
    tx, ty = renderizado.get_width(), renderizado.get_height()
    x = ((x + dx//2) - (tx//2))
    y = ((y + dy//2) - (ty//2)) + 5*var.SCALE
    var.SURFACE.blit(renderizado, (x, y))

def rectangulo_redondeado_con_borde_texto_y_circulo(texto, size, color, color_fondo, color_borde, color_circulo, x, y, dx, dy, radio, grosor):
    x = int(x)
    y = int(y)
    dx = int(dx)
    dy = int(dy)
    radio = int(radio)
    grosor = int(max(1, grosor))

    pg.draw.circle(var.SURFACE, color_borde, (x + radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + dx - radio, y + radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + radio, y + dy - radio), radio)
    pg.draw.circle(var.SURFACE, color_borde, (x + dx - radio, y + dy - radio), radio)
    pg.draw.rect(var.SURFACE, color_borde, (x, y + radio, dx, dy - radio * 2))
    pg.draw.rect(var.SURFACE, color_borde, (x + radio, y, dx - radio * 2, dy))

    pg.draw.circle(var.SURFACE, color_fondo, (x + radio + grosor, y + radio + grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + dx - radio - grosor, y + radio + grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + radio + grosor, y + dy - radio - grosor), radio)
    pg.draw.circle(var.SURFACE, color_fondo, (x + dx - radio - grosor, y + dy - radio - grosor), radio)
    pg.draw.rect(var.SURFACE, color_fondo, (x + grosor, y + radio + grosor, dx - 2 * grosor, dy - radio * 2 - grosor))
    pg.draw.rect(var.SURFACE, color_fondo, (x + grosor + radio + grosor, y + grosor, dx - radio * 2 - grosor, dy - 2 * grosor))
    
    padding_circulo = 4
    radio_circulo = 21
    pg.draw.circle(var.SURFACE, color_circulo, (x + radio + padding_circulo*var.SCALE, y + radio + padding_circulo*var.SCALE), radio_circulo*var.SCALE)

    renderizado = font.agregar_texto(texto, size, color)
    tx, ty = renderizado.get_width(), renderizado.get_height()
    x = ((x + (dx + 2*padding_circulo + radio_circulo)//2) - (tx//2))
    y = ((y + dy//2) - (ty//2)) + 5*var.SCALE
    var.SURFACE.blit(renderizado, (x, y))