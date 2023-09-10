import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.color as color
import grafico.recursos.informacion as info
import grafico.recursos.letras as letras

def contenido():
    color.background()
    info.es_criptocodigo(False)
    info.puntaje_participantes()
    palabra_mostrar = var.CONTENIDO_DATOS_PANEL[0]
    palabra_oculta = var.CONTENIDO_DATOS_PANEL[1]
    if j_var.MOSTRAR_PANEL:
        letras.palabra_anagrama(palabra_mostrar)
        letras.palabra_oculta(palabra_oculta)