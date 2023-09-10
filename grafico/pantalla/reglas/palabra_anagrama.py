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
    En este panel se muestra una palabra y lo que se debe resolver es el 
    anagrama oculto en la parte inferior de este. Cada 2 segundos se 
    descubre una letra al azar del anagrama. El panel se resuelve cuando 
    un participante con ayuda del pulsador logra acertar la palabra 
    correctamente, por esta razón este panel no tiene pista. El pulsador 
    sirve para pedir el turno y responder, este panel no tiene tiempo 
    límite. Si resuelve correctamente, se le asignan 5 puntos y se 
    termina el panel, de lo contrario, el turno se libera y continua el 
    juego hasta que algún participante logre adivinar la palabra 
    correctamente. En el peor de los casos la palabra oculta se muestra 
    completamente y basta con que un participante logre responder 
    correctamente para llevarse el puntaje.
    """
    txt.escribir_parrafo(texto, size, color.AMARILLO, x, y, dx, dy)
