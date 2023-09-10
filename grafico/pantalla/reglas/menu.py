import grafico.recursos.variables as var
import grafico.recursos.imagenes as img
import grafico.recursos.botones as boton
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.letras as letras
import grafico.recursos.figuras as fig
import grafico.pantalla.menu as p_menu
import grafico.pantalla.reglas.palabra_anagrama as r_palabra_anagrama
import grafico.pantalla.reglas.contrarreloj as r_contrarreloj
import grafico.pantalla.reglas.frase_alfagrama as r_frase_alfagrama
import grafico.pantalla.reglas.contrarreloj_multiple as r_contrarreloj_multiple
import grafico.pantalla.reglas.criptocodigo as r_criptocodigo

def principal():
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 42*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    desfase_y = 75*var.SCALE
    y_inicial = 150*var.SCALE
    dx = 370*var.SCALE
    dy = 71*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    x2 = base_x
    y2 = y_inicial
    x3 = base_x
    y3 = y_inicial + desfase_y
    x4 = base_x
    y4 = y_inicial + 2*desfase_y
    x5 = base_x
    y5 = y_inicial + 3*desfase_y
    x6 = base_x
    y6 = y_inicial + 4*desfase_y

    #fig.borde(var.COLOR_TEXTO_INFO, var.DX_MENU*var.SCALE, 0, 420*var.SCALE, var.HEIGHT, var.GROSOR_BORDE_INFO)
    
    txt.escribir_texto_izquierda('Reglas', size_letra, color.AMARILLO, x1, y1, dx, dy)

    menu = var.PANEL_REGLAS
    color_otro = color.AMARILLO
    color_seleccionado = color.BLANCO

    if menu == "r_palabra_anagrama":
        txt.escribir_texto_izquierda('Palabra anagrama', size_subtitulo, color_seleccionado, x2, y2, dx, dy)
    else:
        txt.escribir_texto_izquierda('Palabra anagrama', size_subtitulo, color_otro, x2, y2, dx, dy)

    if menu == "r_contrarreloj":
        txt.escribir_texto_izquierda('Contrarreloj', size_subtitulo, color_seleccionado, x3, y3, dx, dy)
    else:
        txt.escribir_texto_izquierda('Contrarreloj', size_subtitulo, color_otro, x3, y3, dx, dy)

    if menu == "r_frase_alfagrama":
        txt.escribir_texto_izquierda('Frase alfagrama', size_subtitulo, color_seleccionado, x4, y4, dx, dy)
    else:
        txt.escribir_texto_izquierda('Frase alfagrama', size_subtitulo, color_otro, x4, y4, dx, dy)

    if menu == "r_contrarreloj_multiple":
        txt.escribir_texto_izquierda('Contrarreloj múltiple', size_subtitulo, color_seleccionado, x5, y5, dx, dy)
    else:
        txt.escribir_texto_izquierda('Contrarreloj múltiple', size_subtitulo, color_otro, x5, y5, dx, dy)

    if menu == "r_criptocodigo":
        txt.escribir_texto_izquierda('Criptocódigo', size_subtitulo, color_seleccionado, x6, y6, dx, dy)
    else:
        txt.escribir_texto_izquierda('Criptocódigo', size_subtitulo, color_otro, x6, y6, dx, dy)


def evento_botones(x, y):
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 42*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    desfase_y = 75*var.SCALE
    y_inicial = 150*var.SCALE
    dx = 370*var.SCALE
    dy = 71*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    x2 = base_x
    y2 = y_inicial
    x3 = base_x
    y3 = y_inicial + desfase_y
    x4 = base_x
    y4 = y_inicial + 2*desfase_y
    x5 = base_x
    y5 = y_inicial + 3*desfase_y
    x6 = base_x
    y6 = y_inicial + 4*desfase_y

    if x2 < x < x2+dx and y2 < y < y2+dy:
        var.PANEL_REGLAS = "r_palabra_anagrama"

    elif x3 < x < x3+dx and y3 < y < y3+dy:
        var.PANEL_REGLAS = "r_contrarreloj"

    elif x4 < x < x4+dx and y4 < y < y4+dy:
        var.PANEL_REGLAS = "r_frase_alfagrama"

    elif x5 < x < x5+dx and y5 < y < y5+dy:
        var.PANEL_REGLAS = "r_contrarreloj_multiple"

    elif x6 < x < x6+dx and y6 < y < y6+dy:
        var.PANEL_REGLAS = "r_criptocodigo"
