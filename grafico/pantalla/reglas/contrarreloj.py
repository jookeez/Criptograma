import grafico.recursos.variables as var
import grafico.recursos.imagenes as img
import grafico.recursos.botones as boton
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.letras as letras
import grafico.recursos.figuras as fig
import grafico.pantalla.menu as p_menu
import grafico.pantalla.reglas.menu as r_menu

def contenido():
    color.background()
    p_menu.principal()
    r_menu.principal()

    size = 34*var.SCALE
    padding_x = 50*var.SCALE
    g_x = (var.DX_MENU+420)*var.SCALE
    g_dx = var.WIDTH - (var.DX_MENU + 420)*var.SCALE
    x = g_x + padding_x
    y = 130*var.SCALE
    dx = g_dx - 2*padding_x
    dy = 400*var.SCALE

    #fig.borde(var.COLOR_TEXTO_INFO, g_x, 0, g_dx, var.HEIGHT, var.GROSOR_BORDE_INFO)

    texto = """
    En este panel tenemos 2 minutos para responder un máximo de 25 
    anagramas correctamente con ayuda del pulsador. El panel cuenta con 
    una pista que ayuda al participante a entender el anagrama oculto. 
    El participante deberá presionar el pulsador y responder 
    correctamente para llevarse 5 puntos por cada respuesta correcta, 
    de lo contrario libera el turno y el juego continua. Solo se cambia 
    de anagrama cuando se ha intentado responder más de 3 veces. El 
    panel puede terminar de 2 maneras, cuando se acabe el tiempo o 
    cuando se agoten los anagramas.
    """
    txt.escribir_parrafo(texto, size, color.AMARILLO, x, y, dx, dy)