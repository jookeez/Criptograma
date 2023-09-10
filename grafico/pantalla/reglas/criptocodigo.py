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
    En este panel de 10 minutos de tiempo se deberá resolver un anagrama 
    oculto dentro de una frase alfagrama. El panel cuenta con una frase 
    escrita en forma de alfagrama, la misma frase oculta con espacios 
    vacíos y un anagrama con signos de pregunta que nos dice cuantas 
    letra tiene, además de tener una pista para la frase alfagrama y 
    otra para el anagrama. Este panel deberá ser resuelto solo por el 
    participante que haya acumulado la mayor cantidad de puntos durante 
    todo el juego. El juego termina cuando el participante logre 
    resolver el anagrama oculto. Por cada letra posicionada de forma 
    incorrecta se penaliza con 2 segundos por intento.
    """
    txt.escribir_parrafo(texto, size, color.AMARILLO, x, y, dx, dy)
