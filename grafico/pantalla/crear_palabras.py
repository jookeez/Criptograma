import pygame as pg
import generador as generate
import juego.funciones as j_func
import grafico.recursos.funciones as func
import grafico.recursos.variables as var
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.figuras as fig
import grafico.pantalla.menu as p_menu

def contenido():
    color.background()
    p_menu.principal()
    
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = base_x
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    x3 = base_x
    y3 = 250*var.SCALE
    dx3 = 340*var.SCALE
    dy3 = 71*var.SCALE
    if var.CANTIDAD_LETRAS_PALABRA_BUSCADA == 1:
        ese = ''
    else:
        ese = 's'

    x4 = base_x
    y4 = 300*var.SCALE
    dx4 = 340*var.SCALE
    dy4 = 71*var.SCALE

    x5 = base_x + 380*var.SCALE
    y5 = 140*var.SCALE
    dx5 = var.WIDTH - (x5 + padding_right)
    dy5 = 130*var.SCALE

    dx6 = 185*var.SCALE
    dy6 = 42*var.SCALE
    x6 = var.WIDTH - (dx6 + padding_right)
    y6 = 280*var.SCALE

    x7 = global_x + 25*var.SCALE
    y7 = 400*var.SCALE
    dx7 = 340*var.SCALE
    dy7 = 71*var.SCALE

    x8 = base_x
    y8 = 530*var.SCALE
    dx8 = 340*var.SCALE
    dy8 = 71*var.SCALE

    x9 = base_x + 380*var.SCALE
    y9 = 500*var.SCALE
    dx9 = var.WIDTH - (x9 + padding_right)
    dy9 = 150*var.SCALE

    x10 = base_x
    y10 = 700*var.SCALE
    dx10 = 340*var.SCALE
    dy10 = 71*var.SCALE

    x11 = base_x
    y11 = 790*var.SCALE
    dx11 = 340*var.SCALE
    dy11 = 71*var.SCALE

    x12 = base_x
    y12 = 840*var.SCALE
    dx12 = 340*var.SCALE
    dy12 = 71*var.SCALE

    x13 = base_x + 380*var.SCALE
    y13 = 680*var.SCALE
    dx13 = var.WIDTH - (x13 + padding_right)
    dy13 = 290*var.SCALE

    dx14 = 800*var.SCALE
    dy14 = 71*var.SCALE
    x14 = var.WIDTH - (dx14 + 0.6*padding_right)
    y14 = 980*var.SCALE

    if var.CANTIDAD_COINCIDENCIAS == 1:
        ese2 = ''
    else:
        ese2 = 's'

    txt.escribir_texto_izquierda('Creador de palabras y frases', size_letra, color.AMARILLO, x1, y1, dx1, dy1)
    txt.escribir_texto_izquierda('Palabra o frase', size_titulo, color.AMARILLO, x2, y2, dx2, dy2)
    txt.escribir_texto_izquierda(f'{var.CANTIDAD_LETRAS_PALABRA_BUSCADA} letra{ese}', size_subtitulo, color.BLANCO, x3, y3, dx3, dy3)
    txt.escribir_texto_izquierda(f'Tiempo estimado de búsqueda de anagramas: {var.TIEMPO_ESTIMADO_BUSQUEDA}', size_subtitulo, color.BLANCO, x4, y4, dx4, dy4)
    fig.rectangulo_redondeado_con_borde_y_texto(var.PALABRA_BUSCADA, size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x5, y5, dx5, dy5, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Buscar", size_subtitulo, color.AMARILLO, color.FUCSIA, color.AMARILLO, x6, y6, dx6, dy6, radio, grosor)
    txt.escribir_texto_izquierda('Resultados de búsqueda', size_letra, color.AMARILLO, x7, y7, dx7, dy7)
    txt.escribir_texto_izquierda('Alfagrama', size_titulo, color.AMARILLO, x8, y8, dx8, dy8)
    fig.rectangulo_redondeado_con_borde_y_texto(var.ALFAGRAMA_GENERADO, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x9, y9, dx9, dy9, radio, grosor)
    txt.escribir_texto_izquierda('Anagramas', size_titulo, color.AMARILLO, x10, y10, dx10, dy10)
    txt.escribir_texto_izquierda(f'{var.CANTIDAD_COINCIDENCIAS} coincidencia{ese2}', size_subtitulo, color.BLANCO, x11, y11, dx11, dy11)
    txt.escribir_texto_izquierda(f'{var.TIEMPO_BUSQUEDA:.2f} segundos', size_subtitulo, color.BLANCO, x12, y12, dx12, dy12)
    fig.rectangulo_redondeado_con_borde_y_texto(var.ANAGRAMAS_ENCONTRADOS, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x13, y13, dx13, dy13, radio, grosor)
    txt.escribir_texto_izquierda(var.EXCEPCION_TEXTO_CREAR_PALABRA, size_subtitulo, color.ROJO, x14, y14, dx14, dy14)


def evento_botones(x, y):
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = base_x
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    x3 = base_x
    y3 = 250*var.SCALE
    dx3 = 340*var.SCALE
    dy3 = 71*var.SCALE
    
    x4 = base_x
    y4 = 300*var.SCALE
    dx4 = 340*var.SCALE
    dy4 = 71*var.SCALE

    x5 = base_x + 380*var.SCALE
    y5 = 140*var.SCALE
    dx5 = var.WIDTH - (x5 + padding_right)
    dy5 = 130*var.SCALE

    dx6 = 185*var.SCALE
    dy6 = 42*var.SCALE
    x6 = var.WIDTH - (dx6 + padding_right)
    y6 = 280*var.SCALE

    x7 = global_x + 25*var.SCALE
    y7 = 400*var.SCALE
    dx7 = 340*var.SCALE
    dy7 = 71*var.SCALE

    x8 = base_x
    y8 = 530*var.SCALE
    dx8 = 340*var.SCALE
    dy8 = 71*var.SCALE

    x9 = base_x + 380*var.SCALE
    y9 = 500*var.SCALE
    dx9 = var.WIDTH - (x9 + padding_right)
    dy9 = 150*var.SCALE

    x10 = base_x
    y10 = 700*var.SCALE
    dx10 = 340*var.SCALE
    dy10 = 71*var.SCALE

    x11 = base_x
    y11 = 790*var.SCALE
    dx11 = 340*var.SCALE
    dy11 = 71*var.SCALE

    x12 = base_x
    y12 = 840*var.SCALE
    dx12 = 340*var.SCALE
    dy12 = 71*var.SCALE

    x13 = base_x + 380*var.SCALE
    y13 = 680*var.SCALE
    dx13 = var.WIDTH - (x13 + padding_right)
    dy13 = 290*var.SCALE

    dx14 = 800*var.SCALE
    dy14 = 71*var.SCALE
    x14 = var.WIDTH - (dx14 + 0.6*padding_right)
    y14 = 980*var.SCALE

    if x5 < x < x5+dx5 and y5 < y < y5+dy5:
        var.TEXTO_ACTIVO = var.PALABRA_BUSCADA
        func.copiar_texto_portapapeles(var.PALABRA_BUSCADA)
        fig.rectangulo_redondeado_con_borde_y_texto(var.PALABRA_BUSCADA, size_letra, color.AMARILLO, color.MORADO, color.BLANCO, x5, y5, dx5, dy5, radio, grosor)

    if x6 < x < x6+dx6 and y6 < y < y6+dy6 and var.PALABRA_BUSCADA:
        buscar_palabras(var.PALABRA_BUSCADA)

    if x9 < x < x9+dx9 and y9 < y < y9+dy9:
        func.copiar_texto_portapapeles(var.ALFAGRAMA_GENERADO)
        fig.rectangulo_redondeado_con_borde_y_texto(var.ALFAGRAMA_GENERADO, size_letra, color.AMARILLO, color.FUCSIA, color.BLANCO, x9, y9, dx9, dy9, radio, grosor)

    if x13 < x < x13+dx13 and y13 < y < y13+dy13:
        func.copiar_texto_portapapeles(var.ANAGRAMAS_ENCONTRADOS)
        fig.rectangulo_redondeado_con_borde_y_texto(var.ANAGRAMAS_ENCONTRADOS, size_letra, color.AMARILLO, color.FUCSIA, color.BLANCO, x13, y13, dx13, dy13, radio, grosor)

def estimar_tiempo_busqueda(palabra):
    var.CANTIDAD_LETRAS_PALABRA_BUSCADA = len(func.eliminar_espacios(palabra))
    if var.CANTIDAD_LETRAS_PALABRA_BUSCADA < 4:
        var.TIEMPO_ESTIMADO_BUSQUEDA = "< 0.01 segundos."
        var.EXCEPCION_TEXTO_CREAR_PALABRA = "*El largo mínimo para buscar anagramas es de 4 letras"

    elif 4 <= var.CANTIDAD_LETRAS_PALABRA_BUSCADA <= 11:
        var.TIEMPO_ESTIMADO_BUSQUEDA = f"{var.ESTIMADO_BUSQUEDA[var.CANTIDAD_LETRAS_PALABRA_BUSCADA-4]} segundos."
        var.EXCEPCION_TEXTO_CREAR_PALABRA = ""

    elif var.CANTIDAD_LETRAS_PALABRA_BUSCADA == 12:
        var.TIEMPO_ESTIMADO_BUSQUEDA = f"{func.segundos_a_minutos_y_segundos(var.ESTIMADO_BUSQUEDA[var.CANTIDAD_LETRAS_PALABRA_BUSCADA-4])} minutos."
        var.EXCEPCION_TEXTO_CREAR_PALABRA = ""

    else:
        var.TIEMPO_ESTIMADO_BUSQUEDA = "> 20 minutos."
        var.EXCEPCION_TEXTO_CREAR_PALABRA = "*No es posible buscar anagramas con más de 12 letras."

def buscar_palabras(palabra):
    var.CANTIDAD_LETRAS_PALABRA_BUSCADA = len(palabra)

    var.ALFAGRAMA_GENERADO = ""
    var.ANAGRAMAS_ENCONTRADOS = ""

    lista_alfagrama = generate.buscar_alfagrama(palabra)
    for letra in lista_alfagrama:
        var.ALFAGRAMA_GENERADO += f"{letra}"

    if 4 <= var.CANTIDAD_LETRAS_PALABRA_BUSCADA <= 12:
        cantidad_palabras, listado, tiempo = generate.buscar_anagrama(palabra)
        if cantidad_palabras:
            for palabra in listado:
                var.ANAGRAMAS_ENCONTRADOS += f"{palabra}, "
            var.ANAGRAMAS_ENCONTRADOS = var.ANAGRAMAS_ENCONTRADOS[:-2]
        else:
            var.ANAGRAMAS_ENCONTRADOS = "Sin resultados."
        var.CANTIDAD_COINCIDENCIAS = cantidad_palabras
        var.TIEMPO_BUSQUEDA = tiempo
    else:
        var.CANTIDAD_COINCIDENCIAS = 0
        var.TIEMPO_BUSQUEDA = 0.00

def evento_teclado(evento, tecla):
    global_x = var.DX_MENU*var.SCALE
    global_centrado_x = 0
    padding_right = 70*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = base_x
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    x3 = base_x
    y3 = 250*var.SCALE
    dx3 = 340*var.SCALE
    dy3 = 71*var.SCALE
    
    x4 = base_x
    y4 = 300*var.SCALE
    dx4 = 340*var.SCALE
    dy4 = 71*var.SCALE

    x5 = base_x + 380*var.SCALE
    y5 = 140*var.SCALE
    dx5 = var.WIDTH - (x5 + padding_right)
    dy5 = 130*var.SCALE

    dx6 = 185*var.SCALE
    dy6 = 42*var.SCALE
    x6 = var.WIDTH - (dx6 + padding_right)
    y6 = 280*var.SCALE

    x7 = global_x + 25*var.SCALE
    y7 = 400*var.SCALE
    dx7 = 340*var.SCALE
    dy7 = 71*var.SCALE

    x8 = base_x
    y8 = 530*var.SCALE
    dx8 = 340*var.SCALE
    dy8 = 71*var.SCALE

    x9 = base_x + 380*var.SCALE
    y9 = 500*var.SCALE
    dx9 = var.WIDTH - (x9 + padding_right)
    dy9 = 150*var.SCALE

    x10 = base_x
    y10 = 700*var.SCALE
    dx10 = 340*var.SCALE
    dy10 = 71*var.SCALE

    x11 = base_x
    y11 = 790*var.SCALE
    dx11 = 340*var.SCALE
    dy11 = 71*var.SCALE

    x12 = base_x
    y12 = 840*var.SCALE
    dx12 = 340*var.SCALE
    dy12 = 71*var.SCALE

    x13 = base_x + 380*var.SCALE
    y13 = 680*var.SCALE
    dx13 = var.WIDTH - (x13 + padding_right)
    dy13 = 290*var.SCALE

    dx14 = 800*var.SCALE
    dy14 = 71*var.SCALE
    x14 = var.WIDTH - (dx14 + 0.6*padding_right)
    y14 = 980*var.SCALE

    if var.TEXTO_ACTIVO == var.PALABRA_BUSCADA:
        if tecla[pg.K_BACKSPACE]:
            var.PALABRA_BUSCADA = var.PALABRA_BUSCADA[:-1]
        elif len(var.PALABRA_BUSCADA) <= var.MAXIMO_LETRAS_TEXT_AREA:
            var.PALABRA_BUSCADA += j_func.mayuscula(func.letras_y_espacios(evento.unicode))
        var.TEXTO_ACTIVO = var.PALABRA_BUSCADA
        estimar_tiempo_busqueda(var.PALABRA_BUSCADA)

        if tecla[pg.K_RETURN] or tecla[pg.K_TAB]:
            var.PALABRA_BUSCADA = var.PALABRA_BUSCADA[:-1]
            buscar_palabras(var.PALABRA_BUSCADA)
        
        if (tecla[pg.K_LCTRL] or tecla[pg.K_RCTRL]) and tecla[pg.K_v]:
            var.PALABRA_BUSCADA += str(func.pegar_texto_portapapeles())
            fig.rectangulo_redondeado_con_borde_y_texto(var.PALABRA_BUSCADA, size_letra, color.AMARILLO, color.MORADO, color.BLANCO, x5, y5, dx5, dy5, radio, grosor)