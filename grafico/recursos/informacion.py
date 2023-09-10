import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.figuras as fig
import grafico.recursos.color as color

def iniciar_variables():
    var.CANTIDAD_FILAS_ANAGRAMA = 0
    if var.PANEL_MOSTRADO == "p_contrarreloj":
        var.SIZE_CANTIDAD = 85
        var.SIZE_CANTIDAD_PADDING = 1
    else:
        var.SIZE_CANTIDAD = 0
        var.SIZE_CANTIDAD_PADDING = 0

    var.SIZE_PISTA = var.WIDTH - ((((2+var.SIZE_CANTIDAD_PADDING)*var.PADDING_INFO) + var.SIZE_TIEMPO + var.SIZE_CANTIDAD + ((j_var.PARTICIPANTES + 1)*var.PADDING_RIGHT_INFO) + (j_var.PARTICIPANTES*var.SIZE_PUNTAJE_PARTICIPANTE))*var.SCALE)
    var.SIZE_TOTAL_INFO = ((var.WIDTH - (var.SIZE_TIEMPO*var.SCALE + var.SIZE_PISTA + var.SIZE_CANTIDAD + (j_var.PARTICIPANTES*var.SIZE_PUNTAJE_PARTICIPANTE*var.SCALE) + ((j_var.PARTICIPANTES + 1)*var.PADDING_RIGHT_INFO*var.SCALE)))//2)
    
def iniciar_variables_criptocodigo():
    var.CANTIDAD_FILAS_ANAGRAMA = 1
    var.SIZE_PISTA = var.WIDTH - (((2*var.PADDING_INFO) + var.SIZE_TIEMPO + 3*var.PADDING_RIGHT_INFO + 2*var.SIZE_PUNTAJE_PARTICIPANTE)*var.SCALE)
    var.SIZE_TOTAL_INFO = ((var.WIDTH - (var.SIZE_TIEMPO*var.SCALE + var.SIZE_PISTA + 2*var.SIZE_PUNTAJE_PARTICIPANTE*var.SCALE + (3*var.PADDING_RIGHT_INFO*var.SCALE)))//2)

def es_criptocodigo(valor):
    if valor:
        iniciar_variables_criptocodigo()
    else:
        iniciar_variables()

def tiempo(texto):
    x = var.SIZE_TOTAL_INFO
    y = var.HEIGHT - (var.DY_INFO*var.SCALE + var.PADDING_BOTTOM_INFO*var.SCALE)
    dx, dy = var.SIZE_TIEMPO*var.SCALE, var.DY_INFO*var.SCALE
    fig.rectangulo_redondeado_con_borde_y_texto(texto, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

def cantidad(texto):
    x = var.SIZE_TOTAL_INFO + var.SIZE_TIEMPO*var.SCALE + var.PADDING_RIGHT_INFO*var.SCALE
    y = var.HEIGHT - (var.DY_INFO*var.SCALE + var.PADDING_BOTTOM_INFO*var.SCALE)
    dx, dy = var.SIZE_CANTIDAD*var.SCALE, var.DY_INFO*var.SCALE
    fig.rectangulo_redondeado_con_borde_y_texto(texto, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

def pista(texto):
    x = var.SIZE_TOTAL_INFO + (var.SIZE_TIEMPO + (1+var.SIZE_CANTIDAD_PADDING)*var.PADDING_RIGHT_INFO)*var.SCALE + var.SIZE_CANTIDAD*var.SCALE
    y = var.HEIGHT - (var.DY_INFO + var.PADDING_BOTTOM_INFO)*var.SCALE
    dx, dy = var.SIZE_PISTA, var.DY_INFO*var.SCALE
    fig.rectangulo_redondeado_con_borde_y_texto(texto, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

def pista1(texto):
    x = var.SIZE_TOTAL_INFO + var.SIZE_TIEMPO*var.SCALE + var.PADDING_RIGHT_INFO*var.SCALE
    y = var.HEIGHT - (var.DY_INFO + var.PADDING_BOTTOM_INFO)*var.SCALE
    dx = (var.SIZE_PISTA - var.PADDING_RIGHT_INFO)//2
    dy = var.DY_INFO*var.SCALE
    fig.rectangulo_redondeado_con_borde_texto_y_circulo(texto, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_AMARILLO, color.FUCSIA, x, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

def pista2(texto):
    x = (var.SIZE_TOTAL_INFO + var.SIZE_TIEMPO*var.SCALE + var.PADDING_RIGHT_INFO*var.SCALE) + (var.SIZE_PISTA - var.PADDING_RIGHT_INFO)//2 + var.PADDING_RIGHT_INFO
    y = var.HEIGHT - (var.DY_INFO + var.PADDING_BOTTOM_INFO)*var.SCALE
    dx = (var.SIZE_PISTA - var.PADDING_RIGHT_INFO)//2
    dy = var.DY_INFO*var.SCALE
    fig.rectangulo_redondeado_con_borde_texto_y_circulo(texto, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_AMARILLO, color.CELESTE, x, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

def puntaje_participantes():
    x = var.SIZE_TOTAL_INFO + (var.SIZE_TIEMPO + (2+var.SIZE_CANTIDAD_PADDING)*var.PADDING_RIGHT_INFO)*var.SCALE + var.SIZE_CANTIDAD*var.SCALE + var.SIZE_PISTA
    y = var.HEIGHT - (var.DY_INFO + var.PADDING_BOTTOM_INFO)*var.SCALE
    dx, dy = var.SIZE_PUNTAJE_PARTICIPANTE*var.SCALE, var.DY_INFO*var.SCALE
    for i in range(j_var.PARTICIPANTES):
        fig.rectangulo_redondeado_con_borde_y_texto(j_var.PUNTAJE_PARTICIPANTES_PARCIAL[i], var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, var.COLOR_PARTICIPANTES[i], x+((dx+var.PADDING_RIGHT_INFO*var.SCALE)*i), y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

def letras_repetidas(mas_repetida, menos_repetida):
    x = var.SIZE_TOTAL_INFO + (var.SIZE_TIEMPO + 2*var.PADDING_RIGHT_INFO)*var.SCALE + var.SIZE_PISTA
    y = var.HEIGHT - (var.DY_INFO + var.PADDING_BOTTOM_INFO)*var.SCALE
    dx, dy = var.SIZE_PUNTAJE_PARTICIPANTE*var.SCALE, var.DY_INFO*var.SCALE
    fig.rectangulo_redondeado_con_borde_y_texto(mas_repetida, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_FUCSIA, x, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)
    fig.rectangulo_redondeado_con_borde_y_texto(menos_repetida, var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, color.BORDE_CELESTE, x+dx+var.PADDING_RIGHT_INFO*var.SCALE, y, dx, dy, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)
