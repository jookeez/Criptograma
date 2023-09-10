import pygame as pg
import sql.conexion_usuario as conexion
import grafico.recursos.variables as var
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.letras as letras
import grafico.recursos.figuras as fig
import grafico.recursos.funciones as func

def contenido():
    color.background()

    padding_bottom = 100*var.SCALE
    padding_contenido = 20*var.SCALE

    x1 = func.centrar_x((330+450)*var.SCALE)
    y1 = var.Y_LETRAS_SMALL*var.SCALE + padding_bottom
    dx1 = x1 + 330*var.SCALE
    dy1 = 71*var.SCALE

    x2 = func.centrar_x((330+450)*var.SCALE)
    y2 = y1 + dy1 + padding_contenido
    dx2 = x2 + 330*var.SCALE
    dy2 = 71*var.SCALE

    x3 = func.centrar_x(250*var.SCALE)
    y3 = y2 + dy2 + padding_bottom
    dx3 = 250*var.SCALE
    dy3 = 55*var.SCALE

    x4 = 0
    y4 = y3 + dy3 + padding_bottom
    dx4 = var.WIDTH
    dy4 = 55*var.SCALE

    global_dy = y4 + dy4 - padding_bottom
    global_y = func.centrar_y(global_dy)

    size_letra = 57*var.SCALE
    radio = 11*var.SCALE
    grosor = 1

    letras.logo('CRIPTOGRAMA', (var.WIDTH - ((2*var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL)*len('CRIPTOGRAMA'))*var.SCALE)//2, global_y, 1)
    
    txt.escribir_texto_izquierda('Usuario', size_letra, color.AMARILLO, x1, y1+global_y, 330*var.SCALE, dy1)
    fig.rectangulo_redondeado_con_borde_y_texto(var.LOGIN_USUARIO, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, dx1, y1+global_y, 450*var.SCALE, dy1, radio, grosor)
    #txt.escribir_texto_centrado(var.LOGIN_USUARIO, size_letra, color.AMARILLO, dx1, y1+global_y, 450*var.SCALE, dy1)
    
    txt.escribir_texto_izquierda('Clave', size_letra, color.AMARILLO, x2, y2+global_y, 330*var.SCALE, dy2)
    fig.rectangulo_redondeado_con_borde_y_texto(var.PASSWD_USUARIO_OCULTA, size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, dx2, y2+global_y, 450*var.SCALE, dy2, radio, grosor)
    #txt.escribir_texto_centrado(var.PASSWD_USUARIO, size_letra, color.AMARILLO, dx2, y2+global_y, 450*var.SCALE, dy2)

    fig.rectangulo_redondeado_con_borde_y_texto('Entrar', 42*var.SCALE, color.AMARILLO, color.MORADO, color.AMARILLO, x3, y3+global_y, dx3, dy3, radio, grosor)
    
    if var.DATOS_INCORRECTOS:
        txt.escribir_texto_centrado('Los datos son incorrectos.', 36*var.SCALE, color.BLANCO, x4, y4+global_y, dx4, dy4)


def evento_botones(x, y):
    padding_bottom = 100*var.SCALE
    padding_contenido = 20*var.SCALE

    x1 = func.centrar_x((330+450)*var.SCALE)
    y1 = var.Y_LETRAS_SMALL*var.SCALE + padding_bottom
    dx1 = x1 + 330*var.SCALE
    dy1 = 71*var.SCALE

    x2 = func.centrar_x((330+450)*var.SCALE)
    y2 = y1 + dy1 + padding_contenido
    dx2 = x2 + 330*var.SCALE
    dy2 = 71*var.SCALE

    x3 = func.centrar_x(250*var.SCALE)
    y3 = y2 + dy2 + padding_bottom
    dx3 = 250*var.SCALE
    dy3 = 55*var.SCALE

    x4 = 0
    y4 = y3 + dy3 + padding_bottom
    dx4 = var.WIDTH
    dy4 = 55*var.SCALE

    global_dy = y4 + dy4 - padding_bottom
    global_y = func.centrar_y(global_dy)

    if x1 < x < x1+dx1 and y1+global_y < y < y1+global_y+dy1:
        var.TEXTO_ACTIVO = var.LOGIN_USUARIO

    if x2 < x < x2+dx2 and y2+global_y < y < y2+global_y+dy2:
        var.TEXTO_ACTIVO = var.PASSWD_USUARIO

    if x3 < x < x3+dx3 and y3+global_y < y < y3+global_y+dy3:
        if var.LOGIN_USUARIO and var.PASSWD_USUARIO:
            iniciar_sesion(var.LOGIN_USUARIO, var.PASSWD_USUARIO)


def evento_teclado(evento, tecla):
    if var.TEXTO_ACTIVO == var.LOGIN_USUARIO:
        if tecla[pg.K_BACKSPACE]:
            var.LOGIN_USUARIO = var.LOGIN_USUARIO[:-1]
        elif len(var.LOGIN_USUARIO) <= var.MAXIMO_LETRAS_USERNAME:
            var.LOGIN_USUARIO += func.solo_letras(evento.unicode)
        var.TEXTO_ACTIVO = var.LOGIN_USUARIO

    elif var.TEXTO_ACTIVO == var.PASSWD_USUARIO:
        if tecla[pg.K_BACKSPACE]:
            var.PASSWD_USUARIO = var.PASSWD_USUARIO[:-1]
            var.PASSWD_USUARIO_OCULTA = var.PASSWD_USUARIO_OCULTA[:-1]
        elif len(var.PASSWD_USUARIO) <= var.MAXIMO_LETRAS_USERNAME:
            var.PASSWD_USUARIO += func.letras_y_numeros(evento.unicode)
            var.PASSWD_USUARIO_OCULTA += func.cambiar_caracter_por_asterisco(func.letras_y_numeros(evento.unicode))
        var.TEXTO_ACTIVO = var.PASSWD_USUARIO

def tipos_de_usuario(id):
    return var.TIPOS_DE_USUARIOS[id]

def iniciar_sesion(usuario, clave):
    if usuario and clave:
        padding_bottom = 100*var.SCALE
        padding_contenido = 20*var.SCALE

        x1 = func.centrar_x((330+450)*var.SCALE)
        y1 = var.Y_LETRAS_SMALL*var.SCALE + padding_bottom
        dx1 = x1 + 330*var.SCALE
        dy1 = 71*var.SCALE

        x2 = func.centrar_x((330+450)*var.SCALE)
        y2 = y1 + dy1 + padding_contenido
        dx2 = x2 + 330*var.SCALE
        dy2 = 71*var.SCALE

        x3 = func.centrar_x(250*var.SCALE)
        y3 = y2 + dy2 + padding_bottom
        dx3 = 250*var.SCALE
        dy3 = 55*var.SCALE

        x4 = 0
        y4 = y3 + dy3 + padding_bottom
        dx4 = var.WIDTH
        dy4 = 55*var.SCALE

        global_dy = y4 + dy4
        global_y = func.centrar_y(global_dy)

        datos = conexion.iniciar_sesion(usuario)

        if datos:
            passwd = datos[0]
            tipo_usuario = datos[1]
            if clave == passwd:
                var.DATOS_INCORRECTOS = False
                var.TIPO_USUARIO = tipos_de_usuario(tipo_usuario)
                var.NUEVO_TIPO_USUARIO = var.TIPO_USUARIO
                var.PANEL_MOSTRADO = "home"
            else:
                var.DATOS_INCORRECTOS = True
        else:
            var.DATOS_INCORRECTOS = True
    else:
        var.DATOS_INCORRECTOS = True
        
def cerrar_sesion():
    var.PASSWD_USUARIO = ""
    var.PASSWD_USUARIO_OCULTA = ""