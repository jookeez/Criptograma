import grafico.recursos.variables as var
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.figuras as fig
import grafico.pantalla.login as login
import grafico.pantalla.crear_paneles.palabra_anagrama as cp_palabra_anagrama
import grafico.pantalla.crear_paneles.contrarreloj as cp_contrarreloj
import grafico.pantalla.crear_paneles.frase_alfagrama as cp_frase_alfagrama
import grafico.pantalla.crear_paneles.contrarreloj_multiple as cp_contrarreloj_multiple
import grafico.pantalla.crear_paneles.criptocodigo as cp_criptocodigo
import grafico.pantalla.juegos.palabra_anagrama as p_palabra_anagrama
import grafico.pantalla.juegos.contrarreloj  as p_contrarreloj
import grafico.pantalla.juegos.frase_alfagrama as p_frase_alfagrama
import grafico.pantalla.juegos.contrarreloj_multiple as p_contrarreloj_multiple
import grafico.pantalla.juegos.criptocodigo as p_criptocodigo

def principal():
    color_otro = color.AMARILLO
    color_seleccionado = color.BLANCO

    size_titulo = 57*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_menu = 52*var.SCALE

    global_x = 40*var.SCALE
    global_y = 0

    x1 = 30*var.SCALE
    y1 = 25*var.SCALE
    dx1 = 350*var.SCALE
    dy1 = 65*var.SCALE

    x2 = 30*var.SCALE
    y2 = y1 + dy1
    dx2 = 350*var.SCALE
    dy2 = 50*var.SCALE

    x3 = 55*var.SCALE
    y3 = y2 + dy2 + 30*var.SCALE
    dx3 = 450*var.SCALE
    dy3 = y3

    x4 = 30*var.SCALE
    y4 = y3 + 30*var.SCALE
    dx4 = 350*var.SCALE
    dy4 = 65*var.SCALE

    x5 = 30*var.SCALE
    y5 = y4 + dy4
    dx5 = 350*var.SCALE
    dy5 = 65*var.SCALE

    x6 = 30*var.SCALE
    y6 = y5 + dy5
    dx6 = 350*var.SCALE
    dy6 = 65*var.SCALE

    dx14 = 350*var.SCALE
    dy14 = 65*var.SCALE
    x14 = 30*var.SCALE
    y14 = var.HEIGHT - (dy14 + 30*var.SCALE)

    x13 = 55*var.SCALE
    y13 = y14 - 30*var.SCALE
    dx13 = 450*var.SCALE
    dy13 = y14 - 30*var.SCALE

    dx12 = 350*var.SCALE
    dy12 = 65*var.SCALE
    x12 = 30*var.SCALE
    y12 = y13 - dy12 - 30*var.SCALE

    dx11 = 350*var.SCALE
    dy11 = 65*var.SCALE
    x11 = 30*var.SCALE
    y11 = y12 - dy11

    dx10 = 350*var.SCALE
    dy10 = 65*var.SCALE
    x10 = 30*var.SCALE
    y10 = y11 - dy10

    x9 = 55*var.SCALE
    y9 = y10 - 30*var.SCALE
    dx9 = 450*var.SCALE
    dy9 = y10 - 30*var.SCALE

    dx8 = 350*var.SCALE
    dy8 = 65*var.SCALE
    x8 = 30*var.SCALE
    y8 = y9 - dy8 - 30*var.SCALE

    x15 = 510*var.SCALE
    y15 = 30*var.SCALE
    dx15 = x15
    dy15 = var.HEIGHT - y15
    
    txt.escribir_texto_izquierda(f'Hola @{var.LOGIN_USUARIO}', size_titulo, color.AMARILLO, x1+global_x, y1+global_y, dx1, dy1)
    txt.escribir_texto_izquierda(f'{var.TIPO_USUARIO}', size_subtitulo, color.AMARILLO, x2+global_x, y2+global_y, dx2, dy2)
    fig.linea(color.BLANCO, x3, y3, dx3, dy3)
    fig.linea(color.BLANCO, x9, y9, dx9, dy9)
    fig.linea(color.BLANCO, x13, y13, dx13, dy13)
    #fig.linea(color.BLANCO, x15, y15, dx15, dy15)

    menu = var.PANEL_MOSTRADO
    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[2]:
        if menu == "crear_palabras":
            txt.escribir_texto_izquierda("Crear palabras", size_menu, color_seleccionado, x4+global_x, y4+global_y, dx4, dy4)
        else:
            txt.escribir_texto_izquierda("Crear palabras", size_menu, color_otro, x4+global_x, y4+global_y, dx4, dy4)

    #CREAR PANELES
    nombre_crear_panel = "Visualizar paneles"
    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[2]:
        nombre_crear_panel = "Crear paneles"
    if menu == "crear_panel":
        txt.escribir_texto_izquierda(nombre_crear_panel, size_menu, color_seleccionado, x5+global_x, y5+global_y, dx5, dy5)
    else:
        txt.escribir_texto_izquierda(nombre_crear_panel, size_menu, color_otro, x5+global_x, y5+global_y, dx5, dy5)

    if menu == "cp_palabra_anagrama":
        cp_palabra_anagrama.contenido()

    if menu == "cp_contrarreloj":
        cp_contrarreloj.contenido()

    if menu == "cp_frase_alfagrama":
        cp_frase_alfagrama.contenido()

    if menu == "cp_contrarreloj_multiple":
        cp_contrarreloj_multiple.contenido()

    if menu == "cp_criptocodigo":
        cp_criptocodigo.contenido()

    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[1]:
        if menu == "crear_partida":
            txt.escribir_texto_izquierda("Crear partida", size_menu, color_seleccionado, x6+global_x, y6+global_y, dx6, dy6)
        else:
            txt.escribir_texto_izquierda("Crear partida", size_menu, color_otro, x6+global_x, y6+global_y, dx6, dy6)

    #MENU INFERIOR
    if menu == "home":
        txt.escribir_texto_izquierda("Home", size_menu, color_seleccionado, x8+global_x, y8+global_y, dx8, dy8)
    else:
        txt.escribir_texto_izquierda("Home", size_menu, color_otro, x8+global_x, y8+global_y, dx8, dy8)

    if menu == "reglas":
        txt.escribir_texto_izquierda("Reglas", size_menu, color_seleccionado, x10+global_x, y10+global_y, dx10, dy10)
    else:
        txt.escribir_texto_izquierda("Reglas", size_menu, color_otro, x10+global_x, y10+global_y, dx10, dy10)

    if menu == "creditos":
        txt.escribir_texto_izquierda("Créditos", size_menu, color_seleccionado, x11+global_x, y11+global_y, dx11, dy11)
    else:
        txt.escribir_texto_izquierda("Créditos", size_menu, color_otro, x11+global_x, y11+global_y, dx11, dy11)

    if menu == "datos_usuario":
        txt.escribir_texto_izquierda("Datos del usuario", size_menu, color_seleccionado, x12+global_x, y12+global_y, dx12, dy12)
    else:
        txt.escribir_texto_izquierda("Datos del usuario", size_menu, color_otro, x12+global_x, y12+global_y, dx12, dy12)

    if menu == "logout":
        txt.escribir_texto_izquierda("Cerrar sesión", size_menu, color_seleccionado, x14+global_x, y14+global_y, dx14, dy14)
    else:
        txt.escribir_texto_izquierda("Cerrar sesión", size_menu, color_otro, x14+global_x, y14+global_y, dx14, dy14)

    # JUGAR
    if menu == "p_palabra_anagrama":
        p_palabra_anagrama.contenido()

    if menu == "p_contrarreloj":
        p_contrarreloj.contenido()

    if menu == "p_frase_alfagrama":
        p_frase_alfagrama.contenido()

    if menu == "p_contrarreloj_multiple":
        p_contrarreloj_multiple.contenido()

    if menu == "p_criptocodigo":
        p_criptocodigo.contenido()


def evento_botones(x, y):
    global_x = 0
    global_y = 0

    x1 = 30*var.SCALE
    y1 = 25*var.SCALE
    dx1 = 450*var.SCALE
    dy1 = 65*var.SCALE

    x2 = 30*var.SCALE
    y2 = y1 + dy1
    dx2 = 450*var.SCALE
    dy2 = 50*var.SCALE

    x3 = 55*var.SCALE
    y3 = y2 + dy2 + 30*var.SCALE
    dx3 = dx2
    dy3 = y3

    x4 = 30*var.SCALE
    y4 = y3 + 30*var.SCALE
    dx4 = 450*var.SCALE
    dy4 = 65*var.SCALE

    x5 = 30*var.SCALE
    y5 = y4 + dy4
    dx5 = 450*var.SCALE
    dy5 = 65*var.SCALE

    x6 = 30*var.SCALE
    y6 = y5 + dy5
    dx6 = 450*var.SCALE
    dy6 = 65*var.SCALE

    dx14 = 450*var.SCALE
    dy14 = 65*var.SCALE
    x14 = 30*var.SCALE
    y14 = var.HEIGHT - (dy14 + 30*var.SCALE)

    x13 = 55*var.SCALE
    y13 = y14 - 30*var.SCALE
    dx13 = 450*var.SCALE
    dy13 = y14 - 30*var.SCALE

    dx12 = 450*var.SCALE
    dy12 = 65*var.SCALE
    x12 = 30*var.SCALE
    y12 = y13 - dy12 - 30*var.SCALE

    dx11 = 450*var.SCALE
    dy11 = 65*var.SCALE
    x11 = 30*var.SCALE
    y11 = y12 - dy11

    dx10 = 450*var.SCALE
    dy10 = 65*var.SCALE
    x10 = 30*var.SCALE
    y10 = y11 - dy10

    x9 = 55*var.SCALE
    y9 = y10 - 30*var.SCALE
    dx9 = 450*var.SCALE
    dy9 = y10 - 30*var.SCALE

    dx8 = 450*var.SCALE
    dy8 = 65*var.SCALE
    x8 = 30*var.SCALE
    y8 = y9 - dy8 - 30*var.SCALE

    x15 = 510*var.SCALE
    y15 = 30*var.SCALE
    dx15 = x15
    dy15 = var.HEIGHT - y15

    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[2]:
        if x4+global_x < x < x4+global_x+dx4 and y4+global_y < y < y4+global_y+dy4:
            var.PANEL_MOSTRADO = "crear_palabras"

    if x5+global_x < x < x5+global_x+dx5 and y5+global_y < y < y5+global_y+dy5:
        var.PANEL_MOSTRADO = "crear_panel"
        var.PANEL_CREAR = "default"

    if var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[0] or var.TIPO_USUARIO == var.TIPOS_DE_USUARIOS[1]:
        if x6+global_x < x < x6+global_x+dx6 and y6+global_y < y < y6+global_y+dy6:
            var.PANEL_MOSTRADO = "crear_partida"

    if x8+global_x < x < x8+global_x+dx8 and y8+global_y < y < y8+global_y+dy8:
        var.PANEL_MOSTRADO = "home"

    elif x10+global_x < x < x10+global_x+dx10 and y10+global_y < y < y10+global_y+dy10:
        var.PANEL_MOSTRADO = "reglas"

    elif x11+global_x < x < x11+global_x+dx11 and y11+global_y < y < y11+global_y+dy11:
        var.PANEL_MOSTRADO = "creditos"

    elif x12+global_x < x < x12+global_x+dx12 and y12+global_y < y < y12+global_y+dy12:
        var.PANEL_MOSTRADO = "datos_usuario"

    elif x14+global_x < x < x14+global_x+dx14 and y14+global_y < y < y14+global_y+dy14:
        login.cerrar_sesion()
        var.PANEL_MOSTRADO = "login"
