import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.color as color
import grafico.recursos.informacion as info
import grafico.recursos.letras as letras

def contenido():
    color.background()
    info.es_criptocodigo(False)
    palabra_a_mostrar = var.CONTENIDO_CONTRARRELOJ[var.ID_CONTRARRELOJ][1]
    anagrama_oculto = var.CONTENIDO_CONTRARRELOJ[var.ID_CONTRARRELOJ][2]
    pista = var.CONTENIDO_CONTRARRELOJ[var.ID_CONTRARRELOJ][3]

    info.tiempo(j_var.TIEMPO_PARCIAL_JUEGO)
    info.cantidad(var.ID_CONTRARRELOJ+1)
    info.puntaje_participantes()
    if j_var.MOSTRAR_PANEL:
        info.pista(pista)
        letras.palabra_anagrama(palabra_a_mostrar)
        letras.palabra_oculta(anagrama_oculto)