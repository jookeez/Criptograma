import pygame as pg
import sql.conexion_usuario as conexion
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

    centrado_x = (var.WIDTH + global_x - (base_x + 220*var.SCALE))//2

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = centrado_x - 25*var.SCALE
    y2 = 160*var.SCALE
    dx2 = 350*var.SCALE
    dy2 = 71*var.SCALE

    x3 = centrado_x + 350*var.SCALE
    y3 = 150*var.SCALE
    dx3 = 450*var.SCALE
    dy3 = 71*var.SCALE

    x4 = centrado_x - 25*var.SCALE
    y4 = 260*var.SCALE
    dx4 = 350*var.SCALE
    dy4 = 71*var.SCALE

    x5 = centrado_x + 350*var.SCALE
    y5 = 250*var.SCALE
    dx5 = 450*var.SCALE
    dy5 = 71*var.SCALE

    x6 = centrado_x - 25*var.SCALE
    y6 = 360*var.SCALE
    dx6 = 350*var.SCALE
    dy6 = 71*var.SCALE

    x7 = centrado_x + 350*var.SCALE
    y7 = 350*var.SCALE
    dx7 = 450*var.SCALE
    dy7 = 71*var.SCALE

    dx8 = 230*var.SCALE
    dy8 = 71*var.SCALE
    x8 = (var.WIDTH + global_x - dx8)//2
    y8 = 450*var.SCALE

    x14 = centrado_x - 25*var.SCALE
    y14 = 660*var.SCALE
    dx14 = 350*var.SCALE
    dy14 = 71*var.SCALE

    x9 = centrado_x + 350*var.SCALE
    y9 = 650*var.SCALE
    dx9 = 450*var.SCALE
    dy9 = 71*var.SCALE

    x10 = centrado_x - 25*var.SCALE
    y10 = 760*var.SCALE
    dx10 = 350*var.SCALE
    dy10 = 71*var.SCALE

    x11 = centrado_x + 350*var.SCALE
    y11 = 750*var.SCALE
    dx11 = 450*var.SCALE
    dy11 = 71*var.SCALE

    dx12 = 230*var.SCALE
    dy12 = 71*var.SCALE
    x12 = (var.WIDTH + global_x - dx12)//2
    y12 = 850*var.SCALE

    x13 = global_x + 25*var.SCALE
    y13 = 550*var.SCALE
    dx13 = 340*var.SCALE
    dy13 = 71*var.SCALE

    txt.escribir_texto_izquierda('Datos del usuario', size_letra, color.AMARILLO, x1, y1, dx1, dy1)
    txt.escribir_texto_izquierda('Usuario', size_titulo, color.AMARILLO, x2, y2, dx2, dy2)
    fig.rectangulo_redondeado_con_borde_y_texto(var.LOGIN_USUARIO, size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x3, y3, dx3, dy3, radio, grosor)
    txt.escribir_texto_izquierda('Tipo de usuario', size_titulo, color.AMARILLO, x4, y4, dx4, dy4)
    fig.rectangulo_redondeado_con_borde_y_texto(var.NUEVO_TIPO_USUARIO, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x5, y5, dx5, dy5, radio, grosor)
    txt.escribir_texto_izquierda('Palabra clave', size_titulo, color.AMARILLO, x6, y6, dx6, dy6)
    fig.rectangulo_redondeado_con_borde_y_texto(var.PALABRA_CLAVE_OCULTA, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x7, y7, dx7, dy7, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Cambiar", size_titulo, color.AMARILLO, color.MORADO, color.AMARILLO, x8, y8, dx8, dy8, radio, grosor)
    txt.escribir_texto_izquierda('Cambio de clave', size_letra, color.AMARILLO, x13, y13, dx13, dy13)
    txt.escribir_texto_izquierda('Clave nueva', size_titulo, color.AMARILLO, x14, y14, dx14, dy14)
    fig.rectangulo_redondeado_con_borde_y_texto(var.CLAVE_NUEVA_OCULTA, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x9, y9, dx9, dy9, radio, grosor)
    txt.escribir_texto_izquierda('Repetir clave', size_titulo, color.AMARILLO, x10, y10, dx10, dy10)
    fig.rectangulo_redondeado_con_borde_y_texto(var.REPETIR_CLAVE_NUEVA_OCULTA, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x11, y11, dx11, dy11, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Cambiar", size_titulo, color.AMARILLO, color.MORADO, color.AMARILLO, x12, y12, dx12, dy12, radio, grosor)

def verificar_palabra_clave(palabra_clave):
    PALABRA_CLAVE_VERIFICADA = conexion.verificar_palabra_clave()
    if PALABRA_CLAVE_VERIFICADA == palabra_clave:
        var.PALABRA_CLAVE = ""
        var.PALABRA_CLAVE_OCULTA = ""
        return True
    else:
        return False

def cambiar_tipo_usuario(username, tipo_usuario, palabra_clave):
    if verificar_palabra_clave(palabra_clave):
        var.TIPO_USUARIO = tipo_usuario
        id_tipo_usuario = 0
        for i, usuario in enumerate(var.TIPOS_DE_USUARIOS):
            if usuario == tipo_usuario:
                id_tipo_usuario = i
                break
        conexion.cambiar_tipo_usuario(username, id_tipo_usuario)
    

def cambiar_clave(usuario, clave_nueva, repetir_clave):
    if clave_nueva == repetir_clave:
        conexion.cambiar_clave(usuario, clave_nueva)
        print("clave cambiada")
        var.CLAVE_NUEVA = ""
        var.CLAVE_NUEVA_OCULTA = ""
        var.REPETIR_CLAVE_NUEVA = ""
        var.REPETIR_CLAVE_NUEVA_OCULTA = ""
    else:
        print("los datos no coinciden")

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

    centrado_x = (var.WIDTH + global_x - (base_x + 220*var.SCALE))//2

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = centrado_x - 25*var.SCALE
    y2 = 160*var.SCALE
    dx2 = 350*var.SCALE
    dy2 = 71*var.SCALE

    x3 = centrado_x + 350*var.SCALE
    y3 = 150*var.SCALE
    dx3 = 450*var.SCALE
    dy3 = 71*var.SCALE

    x4 = centrado_x - 25*var.SCALE
    y4 = 260*var.SCALE
    dx4 = 350*var.SCALE
    dy4 = 71*var.SCALE

    x5 = centrado_x + 350*var.SCALE
    y5 = 250*var.SCALE
    dx5 = 450*var.SCALE
    dy5 = 71*var.SCALE

    x6 = centrado_x - 25*var.SCALE
    y6 = 360*var.SCALE
    dx6 = 350*var.SCALE
    dy6 = 71*var.SCALE

    x7 = centrado_x + 350*var.SCALE
    y7 = 350*var.SCALE
    dx7 = 450*var.SCALE
    dy7 = 71*var.SCALE

    dx8 = 230*var.SCALE
    dy8 = 71*var.SCALE
    x8 = (var.WIDTH + global_x - dx8)//2
    y8 = 450*var.SCALE

    x14 = centrado_x - 25*var.SCALE
    y14 = 660*var.SCALE
    dx14 = 350*var.SCALE
    dy14 = 71*var.SCALE

    x9 = centrado_x + 350*var.SCALE
    y9 = 650*var.SCALE
    dx9 = 450*var.SCALE
    dy9 = 71*var.SCALE

    x10 = centrado_x - 25*var.SCALE
    y10 = 760*var.SCALE
    dx10 = 350*var.SCALE
    dy10 = 71*var.SCALE

    x11 = centrado_x + 350*var.SCALE
    y11 = 750*var.SCALE
    dx11 = 450*var.SCALE
    dy11 = 71*var.SCALE

    dx12 = 230*var.SCALE
    dy12 = 71*var.SCALE
    x12 = (var.WIDTH + global_x - dx12)//2
    y12 = 850*var.SCALE

    x13 = global_x + 25*var.SCALE
    y13 = 550*var.SCALE
    dx13 = 340*var.SCALE
    dy13 = 71*var.SCALE

    if x5 < x < x5+dx5 and y5 < y < y5+dy5:
        if var.NUEVO_TIPO_USUARIO == "Administrador":
            var.NUEVO_TIPO_USUARIO = "Moderador"

        elif var.NUEVO_TIPO_USUARIO == "Moderador":
            var.NUEVO_TIPO_USUARIO = "Editor"

        elif var.NUEVO_TIPO_USUARIO == "Editor":
            var.NUEVO_TIPO_USUARIO = "Administrador"

    if x7 < x < x7+dx7 and y7 < y < y7+dy7:
        var.TEXTO_ACTIVO = var.PALABRA_CLAVE

    if x9 < x < x9+dx9 and y9 < y < y9+dy9:
        var.TEXTO_ACTIVO = var.CLAVE_NUEVA

    if x11 < x < x11+dx11 and y11 < y < y11+dy11:
        var.TEXTO_ACTIVO = var.REPETIR_CLAVE_NUEVA

    if x8 < x < x8+dx8 and y8 < y < y8+dy8:
        cambiar_tipo_usuario(var.LOGIN_USUARIO, var.NUEVO_TIPO_USUARIO, var.PALABRA_CLAVE)

    if x12 < x < x12+dx12 and y12 < y < y12+dy12:
        cambiar_clave(var.LOGIN_USUARIO, var.CLAVE_NUEVA, var.REPETIR_CLAVE_NUEVA)

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

    centrado_x = (var.WIDTH + global_x - (base_x + 220*var.SCALE))//2

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = centrado_x - 25*var.SCALE
    y2 = 160*var.SCALE
    dx2 = 350*var.SCALE
    dy2 = 71*var.SCALE

    x3 = centrado_x + 350*var.SCALE
    y3 = 150*var.SCALE
    dx3 = 450*var.SCALE
    dy3 = 71*var.SCALE

    x4 = centrado_x - 25*var.SCALE
    y4 = 260*var.SCALE
    dx4 = 350*var.SCALE
    dy4 = 71*var.SCALE

    x5 = centrado_x + 350*var.SCALE
    y5 = 250*var.SCALE
    dx5 = 450*var.SCALE
    dy5 = 71*var.SCALE

    x6 = centrado_x - 25*var.SCALE
    y6 = 360*var.SCALE
    dx6 = 350*var.SCALE
    dy6 = 71*var.SCALE

    x7 = centrado_x + 350*var.SCALE
    y7 = 350*var.SCALE
    dx7 = 450*var.SCALE
    dy7 = 71*var.SCALE

    dx8 = 230*var.SCALE
    dy8 = 71*var.SCALE
    x8 = (var.WIDTH + global_x - dx8)//2
    y8 = 450*var.SCALE

    x14 = centrado_x - 25*var.SCALE
    y14 = 660*var.SCALE
    dx14 = 350*var.SCALE
    dy14 = 71*var.SCALE

    x9 = centrado_x + 350*var.SCALE
    y9 = 650*var.SCALE
    dx9 = 450*var.SCALE
    dy9 = 71*var.SCALE

    x10 = centrado_x - 25*var.SCALE
    y10 = 760*var.SCALE
    dx10 = 350*var.SCALE
    dy10 = 71*var.SCALE

    x11 = centrado_x + 350*var.SCALE
    y11 = 750*var.SCALE
    dx11 = 450*var.SCALE
    dy11 = 71*var.SCALE

    dx12 = 230*var.SCALE
    dy12 = 71*var.SCALE
    x12 = (var.WIDTH + global_x - dx12)//2
    y12 = 850*var.SCALE

    x13 = global_x + 25*var.SCALE
    y13 = 550*var.SCALE
    dx13 = 340*var.SCALE
    dy13 = 71*var.SCALE

    if var.TEXTO_ACTIVO == var.PALABRA_CLAVE:
        if tecla[pg.K_BACKSPACE]:
            var.PALABRA_CLAVE = var.PALABRA_CLAVE[:-1]
            var.PALABRA_CLAVE_OCULTA = var.PALABRA_CLAVE_OCULTA[:-1]
        elif len(var.PALABRA_CLAVE) <= var.MAXIMO_LETRAS_USERNAME:
            var.PALABRA_CLAVE += func.letras_y_numeros(evento.unicode)
            var.PALABRA_CLAVE_OCULTA += func.cambiar_caracter_por_asterisco(func.letras_y_numeros(evento.unicode))
        var.TEXTO_ACTIVO = var.PALABRA_CLAVE

    elif var.TEXTO_ACTIVO == var.CLAVE_NUEVA:
        if tecla[pg.K_BACKSPACE]:
            var.CLAVE_NUEVA = var.CLAVE_NUEVA[:-1]
            var.CLAVE_NUEVA_OCULTA = var.CLAVE_NUEVA_OCULTA[:-1]
        elif len(var.CLAVE_NUEVA) <= var.MAXIMO_LETRAS_USERNAME:
            var.CLAVE_NUEVA += func.letras_y_numeros(evento.unicode)
            var.CLAVE_NUEVA_OCULTA += func.cambiar_caracter_por_asterisco(func.letras_y_numeros(evento.unicode))
        var.TEXTO_ACTIVO = var.CLAVE_NUEVA

    elif var.TEXTO_ACTIVO == var.REPETIR_CLAVE_NUEVA:
        if tecla[pg.K_BACKSPACE]:
            var.REPETIR_CLAVE_NUEVA = var.REPETIR_CLAVE_NUEVA[:-1]
            var.REPETIR_CLAVE_NUEVA_OCULTA = var.REPETIR_CLAVE_NUEVA_OCULTA[:-1]
        elif len(var.REPETIR_CLAVE_NUEVA) <= var.MAXIMO_LETRAS_USERNAME:
            var.REPETIR_CLAVE_NUEVA += func.letras_y_numeros(evento.unicode)
            var.REPETIR_CLAVE_NUEVA_OCULTA += func.cambiar_caracter_por_asterisco(func.letras_y_numeros(evento.unicode))
        var.TEXTO_ACTIVO = var.REPETIR_CLAVE_NUEVA
