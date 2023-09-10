import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.color as color
import grafico.recursos.informacion as info
import grafico.recursos.letras as letras

def contenido():
    color.background()
    info.es_criptocodigo(False)
    info.tiempo(j_var.TIEMPO_PARCIAL_JUEGO)
    info.puntaje_participantes()
    palabra_mostrar = var.CONTENIDO_DATOS_PANEL[0]
    listado_anagrama_oculto = var.CONTENIDO_DATOS_PANEL[1].split(", ")
    var.CANTIDAD_CONTRARRELOJ_MULTIPLE = len(listado_anagrama_oculto)

    if j_var.MOSTRAR_PANEL:
        letras.anagrama_multiple(palabra_mostrar, listado_anagrama_oculto)