import webbrowser as web
import grafico.recursos.variables as var
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.letras as letras
import grafico.pantalla.menu as p_menu

def contenido():
    color.background()
    p_menu.principal()

    #fig.borde(var.COLOR_TEXTO_INFO, (var.DX_MENU+var.GROSOR_BORDE_INFO)*var.SCALE, 0, var.WIDTH - var.DX_MENU*var.SCALE, var.HEIGHT, var.GROSOR_BORDE_INFO)
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = var.WIDTH - global_x
    padding_right = 70*var.SCALE

    size_titulo = 56*var.SCALE
    size_subtitulo = 42*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE
    txt.escribir_texto_izquierda('Créditos', size_letra, color.AMARILLO, x1, y1, dx1, dy1)

    letras.logo('CRIPTOGRAMA', ((var.WIDTH + global_x) - ((2*var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL)*len('CRIPTOGRAMA'))*0.6*var.SCALE)//2, 175*var.SCALE, 0.6)

    x2 = global_x
    y2 = 250*var.SCALE
    dx2 = global_centrado_x
    dy2 = 71*var.SCALE
    txt.escribir_texto_centrado(f'Versión {var.VERSION_MAJOR}.{var.VERSION_MINOR}.{var.VERSION_PATCH}', size_subtitulo, color.AMARILLO, x2, y2, dx2, dy2)

    x3 = global_x
    y3 = 400*var.SCALE
    dx3 = global_centrado_x
    dy3 = 71*var.SCALE
    txt.escribir_texto_centrado('Idea original', size_subtitulo, color.BLANCO, x3, y3, dx3, dy3)

    x4 = global_x
    y4 = 460*var.SCALE
    dx4 = global_centrado_x
    dy4 = 71*var.SCALE
    txt.escribir_texto_centrado('Joaquín Vásquez Jara', size_titulo, color.AMARILLO, x4, y4, dx4, dy4)

    x5 = global_x
    y5 = 550*var.SCALE
    dx5 = global_centrado_x
    dy5 = 71*var.SCALE
    txt.escribir_texto_centrado('Desarrollado por', size_subtitulo, color.BLANCO, x5, y5, dx5, dy5)

    x6 = global_x
    y6 = 610*var.SCALE
    dx6 = global_centrado_x
    dy6 = 71*var.SCALE
    txt.escribir_texto_centrado('@jookeez', size_titulo, color.AMARILLO, x6, y6, dx6, dy6)

    x7 = global_x
    y7 = 700*var.SCALE
    dx7 = global_centrado_x
    dy7 = 71*var.SCALE
    txt.escribir_texto_centrado('Sitio web', size_subtitulo, color.BLANCO, x7, y7, dx7, dy7)

    x8 = global_x
    y8 = 760*var.SCALE
    dx8 = global_centrado_x
    dy8 = 71*var.SCALE
    txt.escribir_texto_centrado('jookeez.com/criptograma', size_titulo, color.AMARILLO, x8, y8, dx8, dy8)

    x9 = global_x
    y9 = var.HEIGHT - 120*var.SCALE
    dx9 = global_centrado_x
    dy9 = 71*var.SCALE
    txt.escribir_texto_centrado('© 2023', size_subtitulo, color.AMARILLO, x9, y9, dx9, dy9)

def evento_botones(x, y):
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = var.WIDTH - global_x

    x4 = global_x
    y4 = 460*var.SCALE
    dx4 = global_centrado_x
    dy4 = 71*var.SCALE

    x6 = global_x
    y6 = 610*var.SCALE
    dx6 = global_centrado_x
    dy6 = 71*var.SCALE

    x8 = global_x
    y8 = 760*var.SCALE
    dx8 = global_centrado_x
    dy8 = 71*var.SCALE

    if (x4 < x < x4+dx4 and y4 < y < y4+dy4) or (x6 < x < x6+dx6 and y6 < y < y6+dy6):
        abrir_enlace("https://jookeez.com")

    if x8 < x < x8+dx8 and y8 < y < y8+dy8:
        abrir_enlace("https://jookeez.com/criptograma")


def abrir_enlace(enlace):
    web.open(enlace)