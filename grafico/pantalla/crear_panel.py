import grafico.recursos.variables as var
import grafico.recursos.imagenes as img
import grafico.recursos.botones as boton
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.letras as letras
import grafico.recursos.figuras as fig
import grafico.pantalla.menu as p_menu

def contenido():
    color.background()
    p_menu.principal()

    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = base_x
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    dx3 = 626*var.SCALE
    dy3 = 71*var.SCALE
    x3 = (var.WIDTH + global_x - dx3)//2
    y3 = 245*var.SCALE

    dx4 = 626*var.SCALE
    dy4 = 71*var.SCALE
    x4 = (var.WIDTH + global_x - dx4)//2
    y4 = 345*var.SCALE

    dx5 = 626*var.SCALE
    dy5 = 71*var.SCALE
    x5 = (var.WIDTH + global_x - dx5)//2
    y5 = 445*var.SCALE

    dx6 = 626*var.SCALE
    dy6 = 71*var.SCALE
    x6 = (var.WIDTH + global_x - dx6)//2
    y6 = 545*var.SCALE

    dx7 = 626*var.SCALE
    dy7 = 71*var.SCALE
    x7 = (var.WIDTH + global_x - dx7)//2
    y7 = 645*var.SCALE

    txt.escribir_texto_izquierda('Creador de paneles', size_letra, color.AMARILLO, x1, y1, dx1, dy1)
    txt.escribir_texto_izquierda('Selecciona el panel que quieres crear:', size_subtitulo, color.AMARILLO, x2, y2, dx2, dy2)
    
    fig.rectangulo_redondeado_con_borde_y_texto("Palabra anagrana", size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x3, y3, dx3, dy3, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Contrarreloj", size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x4, y4, dx4, dy4, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Frase alfagrama", size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x5, y5, dx5, dy5, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Contrarreloj múltiple", size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x6, y6, dx6, dy6, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Criptocódigo", size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x7, y7, dx7, dy7, radio, grosor)
    
def evento_botones(x, y):
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = base_x
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    dx = 626*var.SCALE
    dy = 71*var.SCALE

    dx3 = 626*var.SCALE
    dy3 = 71*var.SCALE
    x3 = (var.WIDTH + global_x - dx3)//2
    y3 = 245*var.SCALE

    dx4 = 626*var.SCALE
    dy4 = 71*var.SCALE
    x4 = (var.WIDTH + global_x - dx4)//2
    y4 = 345*var.SCALE

    dx5 = 626*var.SCALE
    dy5 = 71*var.SCALE
    x5 = (var.WIDTH + global_x - dx5)//2
    y5 = 445*var.SCALE

    dx6 = 626*var.SCALE
    dy6 = 71*var.SCALE
    x6 = (var.WIDTH + global_x - dx6)//2
    y6 = 545*var.SCALE

    dx7 = 626*var.SCALE
    dy7 = 71*var.SCALE
    x7 = (var.WIDTH + global_x - dx7)//2
    y7 = 645*var.SCALE

    if x3 < x < x3+dx and y3 < y < y3+dy:
        var.PANEL_CREAR = "cp_palabra_anagrama"

    elif x4 < x < x4+dx and y4 < y < y4+dy:
        var.PANEL_CREAR = "cp_contrarreloj"

    elif x5 < x < x5+dx and y5 < y < y5+dy:
        var.PANEL_CREAR = "cp_frase_alfagrama"

    elif x6 < x < x6+dx and y6 < y < y6+dy:
        var.PANEL_CREAR = "cp_contrarreloj_multiple"

    elif x7 < x < x7+dx and y7 < y < y7+dy:
        var.PANEL_CREAR = "cp_criptocodigo"