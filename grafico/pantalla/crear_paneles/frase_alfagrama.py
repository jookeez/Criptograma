import pygame as pg
import sql.conexion_juego as conexion_juego
import algoritmos.alfagrama as alfagrama
import juego.funciones as j_func
import grafico.recursos.variables as var
import grafico.recursos.funciones as func
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

    x2 = base_x + 50*var.SCALE
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    dx5 = 215*var.SCALE
    dy5 = 71*var.SCALE
    x5 = var.WIDTH - (dx5 + padding_right)
    y5 = 140*var.SCALE
    
    dx4 = 70*var.SCALE
    dy4 = 71*var.SCALE
    x4 = x5 - dx4
    y4 = 150*var.SCALE

    x3 = base_x + 200*var.SCALE
    y3 = 140*var.SCALE
    dx3 = x5 - x3 - dx4 - 50*var.SCALE
    dy3 = 71*var.SCALE

    dx6 = 185*var.SCALE
    dy6 = 42*var.SCALE
    x6 = var.WIDTH - (dx6 + padding_right)
    y6 = 225*var.SCALE

    x14 = base_x
    y14 = 330*var.SCALE
    dx14 = 340*var.SCALE
    dy14 = 71*var.SCALE

    x7 = base_x + padding_right - 30*var.SCALE
    y7 = 481*var.SCALE
    dx7 = 400*var.SCALE
    dy7 = 71*var.SCALE

    x8 = base_x + padding_right + dx7
    y8 = 443*var.SCALE
    dx8 = var.WIDTH - (x8 + padding_right)
    dy8 = 142*var.SCALE

    x9 = base_x + padding_right - 30*var.SCALE
    y9 = 621*var.SCALE
    dx9 = 400*var.SCALE
    dy9 = 71*var.SCALE

    x10 = base_x + padding_right + dx9
    y10 = 614*var.SCALE
    dx10 = var.WIDTH - (x10 + padding_right)
    dy10 = 71*var.SCALE

    dx11 = 230*var.SCALE
    dy11 = 71*var.SCALE
    x11 = var.WIDTH - (dx11 + padding_right)
    y11 = var.HEIGHT - (dy11 + 50*var.SCALE) 

    dx12 = 230*var.SCALE
    dy12 = 71*var.SCALE
    x12 = var.WIDTH - (dx11 + dx12 + padding_right + 20*var.SCALE)
    y12 = var.HEIGHT - (dy12 + 50*var.SCALE)

    txt.escribir_texto_izquierda('Creador de paneles', size_letra, color.AMARILLO, x1, y1, dx1, dy1)
    txt.escribir_texto_izquierda('Panel', size_titulo, color.AMARILLO, x2, y2, dx2, dy2)
    fig.rectangulo_redondeado_con_borde_y_texto("Frase alfagrama", size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x3, y3, dx3, dy3, radio, grosor)
    txt.escribir_texto_izquierda('ID', size_titulo, color.AMARILLO, x4, y4, dx4, dy4)
    fig.rectangulo_redondeado_con_borde_y_texto(var.CONTENIDO_CREAR_PANEL[2][0], size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x5, y5, dx5, dy5, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Buscar", size_subtitulo, color.AMARILLO, color.FUCSIA, color.AMARILLO, x6, y6, dx6, dy6, radio, grosor)
    txt.escribir_texto_izquierda('El alfagrama oculto se genera automáticamente al guardar el panel.', size_subtitulo, color.AMARILLO, x14, y14, dx14, dy14)
    txt.escribir_texto_izquierda('Frase oculta', size_titulo, color.AMARILLO, x7, y7, dx7, dy7)
    fig.rectangulo_redondeado_con_borde_y_texto(var.CONTENIDO_CREAR_PANEL[2][1], size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x8, y8, dx8, dy8, radio, grosor)
    txt.escribir_texto_izquierda('Pista', size_titulo, color.AMARILLO, x9, y9, dx9, dy9)
    fig.rectangulo_redondeado_con_borde_y_texto(var.CONTENIDO_CREAR_PANEL[2][2], size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x10, y10, dx10, dy10, radio, grosor)    
    
    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[2]:
        fig.rectangulo_redondeado_con_borde_y_texto("Guardar", size_titulo, color.AMARILLO, color.MORADO, color.AMARILLO, x12, y12, dx12, dy12, radio, grosor)
        fig.rectangulo_redondeado_con_borde_y_texto("Editar", size_titulo, color.AMARILLO, color.MORADO, color.AMARILLO, x11, y11, dx11, dy11, radio, grosor)

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

    x2 = base_x + 50*var.SCALE
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    dx5 = 215*var.SCALE
    dy5 = 71*var.SCALE
    x5 = var.WIDTH - (dx5 + padding_right)
    y5 = 140*var.SCALE
    
    dx4 = 70*var.SCALE
    dy4 = 71*var.SCALE
    x4 = x5 - dx4
    y4 = 150*var.SCALE

    x3 = base_x + 200*var.SCALE
    y3 = 140*var.SCALE
    dx3 = x5 - x3 - dx4 - 50*var.SCALE
    dy3 = 71*var.SCALE

    dx6 = 185*var.SCALE
    dy6 = 42*var.SCALE
    x6 = var.WIDTH - (dx6 + padding_right)
    y6 = 225*var.SCALE

    x14 = base_x
    y14 = 330*var.SCALE
    dx14 = 340*var.SCALE
    dy14 = 71*var.SCALE

    x7 = base_x + padding_right - 30*var.SCALE
    y7 = 481*var.SCALE
    dx7 = 400*var.SCALE
    dy7 = 71*var.SCALE

    x8 = base_x + padding_right + dx7
    y8 = 443*var.SCALE
    dx8 = var.WIDTH - (x8 + padding_right)
    dy8 = 142*var.SCALE

    x9 = base_x + padding_right - 30*var.SCALE
    y9 = 621*var.SCALE
    dx9 = 400*var.SCALE
    dy9 = 71*var.SCALE

    x10 = base_x + padding_right + dx9
    y10 = 614*var.SCALE
    dx10 = var.WIDTH - (x10 + padding_right)
    dy10 = 71*var.SCALE

    dx11 = 230*var.SCALE
    dy11 = 71*var.SCALE
    x11 = var.WIDTH - (dx11 + padding_right)
    y11 = var.HEIGHT - (dy11 + 50*var.SCALE) 

    dx12 = 230*var.SCALE
    dy12 = 71*var.SCALE
    x12 = var.WIDTH - (dx11 + dx12 + padding_right + 20*var.SCALE)
    y12 = var.HEIGHT - (dy12 + 50*var.SCALE)

    if x5 < x < x5+dx5 and y5 < y < y5+dy5:
        var.TEXTO_ACTIVO = var.CONTENIDO_CREAR_PANEL[2][0]

    if x6 < x < x6+dx6 and y6 < y < y6+dy6:
        buscar_en_bd(var.CONTENIDO_CREAR_PANEL[1][0])

    if x8 < x < x8+dx8 and y8 < y < y8+dy8:
        var.TEXTO_ACTIVO = var.CONTENIDO_CREAR_PANEL[2][1]

    if x10 < x < x10+dx10 and y10 < y < y10+dy10:
        var.TEXTO_ACTIVO = var.CONTENIDO_CREAR_PANEL[2][2]

    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[2]:
        if x12 < x < x12+dx12 and y12 < y < y12+dy12:
            print("guardando datos")
            agregar_datos(var.CONTENIDO_CREAR_PANEL[2][1], var.CONTENIDO_CREAR_PANEL[2][2], var.LOGIN_USUARIO)
            print("datos guardados")

        if x11 < x < x11+dx11 and y11 < y < y11+dy11:
            print("editando datos")
            editar_datos(var.CONTENIDO_CREAR_PANEL[2][0], var.CONTENIDO_CREAR_PANEL[2][1], var.CONTENIDO_CREAR_PANEL[2][2], var.LOGIN_USUARIO)
            print("datos modificados")

def agregar_datos(frase_oculta, pista, username):
    texto_alfagrama = alfagrama.generar_alfagrama_en_palabra(frase_oculta)
    if frase_oculta and texto_alfagrama and pista and username:
        conexion_juego.agregar_frase_alfagrama(frase_oculta, texto_alfagrama, pista, username)

def editar_datos(id, frase_oculta, pista, username):
    texto_alfagrama = alfagrama.generar_alfagrama_en_palabra(frase_oculta)
    if id and frase_oculta and texto_alfagrama and pista and username:
        conexion_juego.editar_frase_alfagrama(id, frase_oculta, texto_alfagrama, pista, username)

def buscar_en_bd(id):
    if id:
        datos = conexion_juego.consultar_frase_alfagrama(id)
        if datos:
            var.CONTENIDO_CREAR_PANEL[2][1] = datos[0]
            var.CONTENIDO_CREAR_PANEL[2][2] = datos[1]
        else:
            var.CONTENIDO_CREAR_PANEL[2][1] = "-"
            var.CONTENIDO_CREAR_PANEL[2][2] = "-"


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

    x2 = base_x + 50*var.SCALE
    y2 = 150*var.SCALE
    dx2 = 340*var.SCALE
    dy2 = 71*var.SCALE

    dx5 = 215*var.SCALE
    dy5 = 71*var.SCALE
    x5 = var.WIDTH - (dx5 + padding_right)
    y5 = 140*var.SCALE
    
    dx4 = 70*var.SCALE
    dy4 = 71*var.SCALE
    x4 = x5 - dx4
    y4 = 150*var.SCALE

    x3 = base_x + 200*var.SCALE
    y3 = 140*var.SCALE
    dx3 = x5 - x3 - dx4 - 50*var.SCALE
    dy3 = 71*var.SCALE

    dx6 = 185*var.SCALE
    dy6 = 42*var.SCALE
    x6 = var.WIDTH - (dx6 + padding_right)
    y6 = 225*var.SCALE

    x14 = base_x
    y14 = 330*var.SCALE
    dx14 = 340*var.SCALE
    dy14 = 71*var.SCALE

    x7 = base_x + padding_right - 30*var.SCALE
    y7 = 481*var.SCALE
    dx7 = 400*var.SCALE
    dy7 = 71*var.SCALE

    x8 = base_x + padding_right + dx7
    y8 = 443*var.SCALE
    dx8 = var.WIDTH - (x8 + padding_right)
    dy8 = 142*var.SCALE

    x9 = base_x + padding_right - 30*var.SCALE
    y9 = 621*var.SCALE
    dx9 = 400*var.SCALE
    dy9 = 71*var.SCALE

    x10 = base_x + padding_right + dx9
    y10 = 614*var.SCALE
    dx10 = var.WIDTH - (x10 + padding_right)
    dy10 = 71*var.SCALE

    dx11 = 230*var.SCALE
    dy11 = 71*var.SCALE
    x11 = var.WIDTH - (dx11 + padding_right)
    y11 = var.HEIGHT - (dy11 + 50*var.SCALE) 

    dx12 = 230*var.SCALE
    dy12 = 71*var.SCALE
    x12 = var.WIDTH - (dx11 + dx12 + padding_right + 20*var.SCALE)
    y12 = var.HEIGHT - (dy12 + 50*var.SCALE)

    # Si estamos escribiendo en ID
    if var.TEXTO_ACTIVO == var.CONTENIDO_CREAR_PANEL[2][0]:
        if tecla[pg.K_BACKSPACE]:
            var.CONTENIDO_CREAR_PANEL[2][0] = var.CONTENIDO_CREAR_PANEL[2][0][:-1]
        elif len(var.CONTENIDO_CREAR_PANEL[2][0]) < var.MAXIMO_LETRAS_ID:
            var.CONTENIDO_CREAR_PANEL[2][0] += func.solo_numeros(evento.unicode)
        var.TEXTO_ACTIVO = var.CONTENIDO_CREAR_PANEL[2][0]

        if tecla[pg.K_RETURN]:
            buscar_en_bd(var.CONTENIDO_CREAR_PANEL[2][0])
        
    # Si estamos escribiendo en FRASE OCULTA
    elif var.TEXTO_ACTIVO == var.CONTENIDO_CREAR_PANEL[2][1]:
        if tecla[pg.K_BACKSPACE]:
            var.CONTENIDO_CREAR_PANEL[2][1] = var.CONTENIDO_CREAR_PANEL[2][1][:-1]
        elif len(var.CONTENIDO_CREAR_PANEL[2][1]) <= var.MAXIMO_LETRAS_TEXT_AREA:
            var.CONTENIDO_CREAR_PANEL[2][1] += j_func.mayuscula(func.letras_y_espacios(evento.unicode))
        var.TEXTO_ACTIVO = var.CONTENIDO_CREAR_PANEL[2][1]

        if tecla[pg.K_RETURN] or tecla[pg.K_TAB]:
            var.CONTENIDO_CREAR_PANEL[2][1] = var.CONTENIDO_CREAR_PANEL[2][1][:-1]

        if (tecla[pg.K_LCTRL] or tecla[pg.K_RCTRL]) and tecla[pg.K_v]:
            var.CONTENIDO_CREAR_PANEL[2][1] += str(func.pegar_texto_portapapeles())
            fig.rectangulo_redondeado_con_borde_y_texto(var.CONTENIDO_CREAR_PANEL[2][1], size_letra, color.AMARILLO, color.FUCSIA, color.BLANCO, x8, y8, dx8, dy8, radio, grosor)

    # Si estamos escribiendo en PISTA
    elif var.TEXTO_ACTIVO == var.CONTENIDO_CREAR_PANEL[2][2]:
        if tecla[pg.K_BACKSPACE]:
            var.CONTENIDO_CREAR_PANEL[2][2] = var.CONTENIDO_CREAR_PANEL[2][2][:-1]
        elif len(var.CONTENIDO_CREAR_PANEL[2][2]) <= var.MAXIMO_LETRAS_TEXT_AREA:
            var.CONTENIDO_CREAR_PANEL[2][2] += func.letras_y_espacios(evento.unicode)
        var.TEXTO_ACTIVO = var.CONTENIDO_CREAR_PANEL[2][2]

        if tecla[pg.K_RETURN] or tecla[pg.K_TAB]:
            var.CONTENIDO_CREAR_PANEL[2][2] = var.CONTENIDO_CREAR_PANEL[2][2][:-1]

        if (tecla[pg.K_LCTRL] or tecla[pg.K_RCTRL]) and tecla[pg.K_v]:
            var.CONTENIDO_CREAR_PANEL[2][2] += str(func.pegar_texto_portapapeles())
            fig.rectangulo_redondeado_con_borde_y_texto(var.CONTENIDO_CREAR_PANEL[2][2], size_letra, color.AMARILLO, color.FUCSIA, color.BLANCO, x10, y10, dx10, dy10, radio, grosor)
