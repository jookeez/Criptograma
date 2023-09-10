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
    En este panel tenemos 2 minutos de tiempo para resolver las 
    distintas formas que tiene un anagrama de resolverse. Cuenta con 
    una palabra y los anagramas válidos con espacios vacíos. No tiene 
    pista este panel, ya que cada anagrama tiene otros anagramas que 
    pueden tener significados completamente distintos entre sí. El 
    participante deberá presionar el pulsador para responder uno de los 
    anagramas ocultos, cada respuesta correcta equivale a 5 puntos. El 
    panel termina cuando se resuelven correctamente todas las palabras 
    ocultas.
    """
    txt.escribir_parrafo(texto, size, color.AMARILLO, x, y, dx, dy)
