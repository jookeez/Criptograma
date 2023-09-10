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
    En este panel tenemos 5 minutos para responder una frase que se 
    muestra en forma de alfagrama y en su versión original con los 
    espacios vacíos. La forma alfagrama que se muestra son todas las 
    letras que deberán completar la frase oculta, además de una pista 
    que ayuda al participante a entender que es lo que podría decir 
    dicha frase. Comienza este panel el participante ganador del panel 
    Palabra Anagrama. Este panel se juega por turnos cíclicos, esto 
    quiere decir que quien pierda su turno, su contrincante de la 
    derecha continuará jugando el panel. Por cada letra acertada se 
    obtiene 1 punto, y quien resuelva el panel completo correctamente 
    se lleva la cantidad de puntos equivalente a las letras disponibles 
    hasta ese momento multiplicado por 2. Por cada letra posicionada de 
    forma incorrecta se penaliza con 2 segundos por intento.
    """
    txt.escribir_parrafo(texto, size, color.AMARILLO, x, y, dx, dy)
