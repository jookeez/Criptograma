import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.color as color
import grafico.recursos.informacion as info
import grafico.recursos.letras as letras

def contenido():
    color.background()
    info.es_criptocodigo(False)
    info.puntaje_participantes()
    frase_oculta = var.CONTENIDO_DATOS_PANEL[0]
    texto_alfagrama = var.CONTENIDO_DATOS_PANEL[1]
    pista = var.CONTENIDO_DATOS_PANEL[2]
    info.tiempo(j_var.TIEMPO_PARCIAL_JUEGO)
    if j_var.MOSTRAR_PANEL:
        info.pista(pista)
        letras.frase_alfagrama(texto_alfagrama)
        letras.frase_oculta(frase_oculta)