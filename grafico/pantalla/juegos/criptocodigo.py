import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.color as color
import grafico.recursos.informacion as info
import grafico.recursos.letras as letras

def contenido():
    color.background()
    info.es_criptocodigo(True)
    frase_oculta = var.CONTENIDO_DATOS_PANEL[0]
    texto_alfagrama = var.CONTENIDO_DATOS_PANEL[1]
    pista_alfagrama = var.CONTENIDO_DATOS_PANEL[2]
    anagrama_de_la_frase = var.CONTENIDO_DATOS_PANEL[3]
    anagrama_oculto = var.CONTENIDO_DATOS_PANEL[4]
    pista_anagrama = var.CONTENIDO_DATOS_PANEL[5]
    letra_mas_repetida = var.CONTENIDO_DATOS_PANEL[6]
    letra_menos_repetida = var.CONTENIDO_DATOS_PANEL[7]
    info.tiempo(j_var.TIEMPO_PARCIAL_JUEGO)
    info.pista1(pista_alfagrama)
    info.pista2(pista_anagrama)
    info.letras_repetidas(letra_menos_repetida, letra_mas_repetida)
    letras.frase_alfagrama(texto_alfagrama)
    letras.frase_oculta(frase_oculta)
    letras.palabra_oculta_criptocodigo(frase_oculta, anagrama_oculto)
