import pygame as pg
import sql.conexion_juego as conexion_juego
import juego.funciones as j_func
import juego.variables as j_var
import grafico.recursos.variables as var
import grafico.recursos.funciones as func
import grafico.recursos.texto as txt
import grafico.recursos.color as color
import grafico.recursos.figuras as fig
import grafico.pantalla.menu as p_menu
import grafico.pantalla.crear_paneles.contrarreloj as cp_contrarreloj

def contenido():
    color.background()
    p_menu.principal()

    global_x = var.DX_MENU*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 48*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE
    centrado_x = (var.WIDTH + global_x - (base_x + 765*var.SCALE))//2

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = centrado_x
    y2 = 125*var.SCALE
    dx2 = 500*var.SCALE
    dy2 = 71*var.SCALE

    x3 = x2
    y3 = 205*var.SCALE
    dx3 = dx2
    dy3 = dy2
    desfase_y = 90*var.SCALE

    x4 = centrado_x + dx3 + 15*var.SCALE
    y4 = 125*var.SCALE
    dx4 = 120*var.SCALE
    dy4 = 71*var.SCALE

    x5 = x4
    y5 = 205*var.SCALE
    dx5 = dx4
    dy5 = dy4

    x6 = x5 + dx5 + 15*var.SCALE
    y6 = y5
    dx6 = 150*var.SCALE
    dy6 = dy4

    x8 = x6 + dx6 + 75*var.SCALE
    y8 = y3
    dx8 = 325*var.SCALE
    dy8 = 71*var.SCALE

    x9 = x8 + dx8 + 15*var.SCALE
    y9 = y8
    dx9 = 110*var.SCALE
    dy9 = var.DY_INFO*var.SCALE

    x7 = x6 + dx6 + 75*var.SCALE
    y7 = 125*var.SCALE
    dx7 = dx8 + dx9 + 15*var.SCALE
    dy7 = 71*var.SCALE

    x10 = x8 + 8*var.SCALE
    y10 = 670*var.SCALE
    dx10 = 300*var.SCALE
    dy10 = 71*var.SCALE

    x11 = x10 + dx10
    y11 = y10 - 10*var.SCALE
    dx11 = 150*var.SCALE
    dy11 = dy4

    x15 = x8 + 8*var.SCALE
    y15 = 755*var.SCALE
    dx15 = 300*var.SCALE
    dy15 = 71*var.SCALE

    x16 = x15 + dx15
    y16 = y15 - 10*var.SCALE
    dx16 = 150*var.SCALE
    dy16 = dy4

    padding_right = 50*var.SCALE
    dx12 = 300*var.SCALE
    dy12 = 50*var.SCALE
    x12 = var.WIDTH - (dx12 + padding_right)
    y12 = var.HEIGHT - (dy12 + 50*var.SCALE) 

    dx13 = dx12
    dy13 = dy12
    x13 = var.WIDTH - (dx12 + dx13 + padding_right + 20*var.SCALE)
    y13 = var.HEIGHT - (dy13 + 50*var.SCALE)

    txt.escribir_texto_izquierda('Resumen del juego', 57*var.SCALE, color.AMARILLO, x1, y1, dx1, dy1)
    txt.escribir_texto_centrado('Paneles', size_titulo, color.AMARILLO, x2, y2, dx2, dy2)
    txt.escribir_texto_centrado('ID', size_titulo, color.AMARILLO, x4, y4, dx4, dy4)

    for i, panel in enumerate(var.LISTADO_PANELES):
        fig.rectangulo_redondeado_con_borde_y_texto(panel, size_letra, color.AMARILLO, color.CELESTE, color.AMARILLO, x3, y3+(i*desfase_y), dx3, dy3, radio, grosor)
        fig.rectangulo_redondeado_con_borde_y_texto(var.ID_LISTADO_PANELES[i], size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x5, y5+(i*desfase_y), dx5, dy5, radio, grosor)
        fig.rectangulo_redondeado_con_borde_y_texto("Jugar", size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x6, y6+(i*desfase_y), dx6, dy6, radio, grosor)
        
    txt.escribir_texto_centrado('Participantes', size_titulo, color.AMARILLO, x7, y7, dx7, dy7)

    for i in range(j_var.PARTICIPANTES):
        fig.rectangulo_redondeado_con_borde_y_texto(j_var.NOMBRE_PARTICIPANTES[i], size_letra, color.AMARILLO, color.FUCSIA, color.AMARILLO, x8, y8+(i*desfase_y), dx8, dy8, radio, grosor)
        fig.rectangulo_redondeado_con_borde_y_texto(j_var.PUNTAJE_PARTICIPANTES[i], var.SIZE_INFO*var.SCALE, var.COLOR_TEXTO_INFO, color.MORADO, var.COLOR_PARTICIPANTES[i], x9, y9+(i*desfase_y), dx9, dy9, var.BORDE_RADIO_INFO*var.SCALE, var.GROSOR_BORDE_INFO*var.SCALE)

    txt.escribir_texto_izquierda('Jugadores', size_titulo, color.AMARILLO, x10, y10, dx10, dy10)
    fig.rectangulo_redondeado_con_borde_y_texto(j_var.PARTICIPANTES, size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x11, y11, dx11, dy11, radio, grosor)
    txt.escribir_texto_izquierda('Tiempo jugado', size_titulo, color.AMARILLO, x15, y15, dx15, dy15)
    fig.rectangulo_redondeado_con_borde_y_texto(j_func.segundos_a_minutos_segundos(j_var.TIEMPO_TOTAL_JUEGO_SEGUNDOS), size_letra, color.AMARILLO, color.MORADO, color.AMARILLO, x16, y16, dx16, dy16, radio, grosor)

    fig.rectangulo_redondeado_con_borde_y_texto("Reiniciar datos", size_subtitulo, color.AMARILLO, color.MORADO, color.AMARILLO, x13, y13, dx13, dy13, radio, grosor)
    fig.rectangulo_redondeado_con_borde_y_texto("Ver 2da pantalla", size_subtitulo, color.AMARILLO, color.MORADO, color.AMARILLO, x12, y12, dx12, dy12, radio, grosor)

def evento_botones(x, y):
    global_x = var.DX_MENU*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 48*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE
    centrado_x = (var.WIDTH + global_x - (base_x + 765*var.SCALE))//2

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = centrado_x
    y2 = 125*var.SCALE
    dx2 = 500*var.SCALE
    dy2 = 71*var.SCALE

    x3 = x2
    y3 = 205*var.SCALE
    dx3 = dx2
    dy3 = dy2
    desfase_y = 90*var.SCALE

    x4 = centrado_x + dx3 + 15*var.SCALE
    y4 = 125*var.SCALE
    dx4 = 120*var.SCALE
    dy4 = 71*var.SCALE

    x5 = x4
    y5 = 205*var.SCALE
    dx5 = dx4
    dy5 = dy4

    x6 = x5 + dx5 + 15*var.SCALE
    y6 = y5
    dx6 = 150*var.SCALE
    dy6 = dy4

    x8 = x6 + dx6 + 75*var.SCALE
    y8 = y3
    dx8 = 325*var.SCALE
    dy8 = 71*var.SCALE

    x9 = x8 + dx8 + 15*var.SCALE
    y9 = y8
    dx9 = 110*var.SCALE
    dy9 = var.DY_INFO*var.SCALE

    x7 = x6 + dx6 + 75*var.SCALE
    y7 = 125*var.SCALE
    dx7 = dx8 + dx9 + 15*var.SCALE
    dy7 = 71*var.SCALE

    x10 = x8 + 8*var.SCALE
    y10 = 670*var.SCALE
    dx10 = 300*var.SCALE
    dy10 = 71*var.SCALE

    x11 = x10 + dx10
    y11 = y10 - 10*var.SCALE
    dx11 = 150*var.SCALE
    dy11 = dy4

    x15 = x8 + 8*var.SCALE
    y15 = 755*var.SCALE
    dx15 = 300*var.SCALE
    dy15 = 71*var.SCALE

    x16 = x15 + dx15
    y16 = y15 - 10*var.SCALE
    dx16 = 150*var.SCALE
    dy16 = dy4

    padding_right = 50*var.SCALE
    dx12 = 300*var.SCALE
    dy12 = 50*var.SCALE
    x12 = var.WIDTH - (dx12 + padding_right)
    y12 = var.HEIGHT - (dy12 + 50*var.SCALE) 

    dx13 = dx12
    dy13 = dy12
    x13 = var.WIDTH - (dx12 + dx13 + padding_right + 20*var.SCALE)
    y13 = var.HEIGHT - (dy13 + 50*var.SCALE)

    for i, panel in enumerate(var.ID_LISTADO_PANELES):
        if x5 < x < x5+dx5 and y5+(i*desfase_y) < y < y5+(i*desfase_y)+dy5:
            var.TEXTO_ACTIVO = var.ID_LISTADO_PANELES[i]

    for i, panel in enumerate(var.LISTADO_PANELES):
        if x6 < x < x6+dx6 and y6+(i*desfase_y) < y < y6+(i*desfase_y)+dy6:
            j_func.reiniciar_puntaje_parcial()
            j_func.reiniciar_cronometro()
            var.ID_CONTRARRELOJ = 0
            j_var.MOSTRAR_PANEL = False
            cargar_datos(var.LISTADO_PANELES[i], int(var.ID_LISTADO_PANELES[i]))

            jugar_panel = j_func.minuscula(var.LISTADO_PANELES[i])
            jugar_panel = j_func.quitar_tildes(jugar_panel)
            jugar_panel = func.cambiar_espacios_por_underscore(jugar_panel)
            var.PANEL_MOSTRADO = f"p_{jugar_panel}"

    for i in range(j_var.PARTICIPANTES):
        if x8 < x < x8+dx8 and y8+(i*desfase_y) < y < y8+(i*desfase_y)+dy8:
            var.TEXTO_ACTIVO = j_var.NOMBRE_PARTICIPANTES[i]

    if x11 < x < x11+dx11 and y11 < y < y11+dy11:
        if j_var.PARTICIPANTES == 2:
            j_var.PARTICIPANTES = 3

        elif j_var.PARTICIPANTES == 3:
            j_var.PARTICIPANTES = 4
            
        elif j_var.PARTICIPANTES == 4:
            j_var.PARTICIPANTES = 2

    if x13 < x < x13+dx13 and y13 < y < y13+dy13:
        j_func.paneles_por_defecto()
        j_func.reiniciar_puntaje_total()
        j_func.reiniciar_tiempo_jugado()
        j_func.reiniciar_participantes()
        print("datos reiniciados")

    if x12 < x < x12+dx12 and y12 < y < y12+dy12:
        func.abrir_2da_pantalla()

def cargar_datos(nombre_panel, id):
    if nombre_panel == "Palabra anagrama" and id:
        datos = conexion_juego.consultar_panel_palabra_anagrama(id)
        if datos:
            var.CONTENIDO_DATOS_PANEL[0] = datos[0]
            var.CONTENIDO_DATOS_PANEL[1] = datos[1]
        else:
            var.CONTENIDO_DATOS_PANEL[0] = "-"
            var.CONTENIDO_DATOS_PANEL[1] = "-"

    elif nombre_panel == "Contrarreloj" and id:
        cp_contrarreloj.buscar_en_bd(id)

    elif nombre_panel == "Frase alfagrama" and id:
        datos = conexion_juego.consultar_panel_frase_alfagrama(id)
        if datos:
            var.CONTENIDO_DATOS_PANEL[0] = datos[0]
            var.CONTENIDO_DATOS_PANEL[1] = datos[1]
            var.CONTENIDO_DATOS_PANEL[2] = datos[2]
        else:
            var.CONTENIDO_DATOS_PANEL[0] = "-"
            var.CONTENIDO_DATOS_PANEL[1] = "-"
            var.CONTENIDO_DATOS_PANEL[2] = "-"

    elif nombre_panel == "Contrarreloj múltiple" and id:
        datos = conexion_juego.consultar_panel_contrarreloj_multiple(id)
        if datos:
            var.CONTENIDO_DATOS_PANEL[0] = datos[0]
            var.CONTENIDO_DATOS_PANEL[1] = datos[1]
        else:
            var.CONTENIDO_DATOS_PANEL[0] = "-"
            var.CONTENIDO_DATOS_PANEL[1] = "-"

    elif nombre_panel == "Criptocódigo" and id:
        datos = conexion_juego.consultar_panel_criptocodigo(id)
        if datos:
            var.CONTENIDO_DATOS_PANEL[0] = datos[0]
            var.CONTENIDO_DATOS_PANEL[1] = datos[1]
            var.CONTENIDO_DATOS_PANEL[2] = datos[2]
            var.CONTENIDO_DATOS_PANEL[3] = datos[3]
            var.CONTENIDO_DATOS_PANEL[4] = datos[4]
            var.CONTENIDO_DATOS_PANEL[5] = datos[5]
            var.CONTENIDO_DATOS_PANEL[6] = datos[6]
            var.CONTENIDO_DATOS_PANEL[7] = datos[7]
        else:
            var.CONTENIDO_DATOS_PANEL[0] = "-"
            var.CONTENIDO_DATOS_PANEL[1] = "-"
            var.CONTENIDO_DATOS_PANEL[2] = "-"
            var.CONTENIDO_DATOS_PANEL[3] = "-"
            var.CONTENIDO_DATOS_PANEL[4] = "-"
            var.CONTENIDO_DATOS_PANEL[5] = "-"
            var.CONTENIDO_DATOS_PANEL[6] = "-"
            var.CONTENIDO_DATOS_PANEL[7] = "-"

def evento_teclado(evento, tecla):
    global_x = var.DX_MENU*var.SCALE

    size_titulo = 52*var.SCALE
    size_subtitulo = 36*var.SCALE
    size_letra = 48*var.SCALE
    radio = 11*var.SCALE
    grosor = 1
    base_x = global_x + 50*var.SCALE
    centrado_x = (var.WIDTH + global_x - (base_x + 765*var.SCALE))//2

    x1 = global_x + 25*var.SCALE
    y1 = 30*var.SCALE
    dx1 = 340*var.SCALE
    dy1 = 71*var.SCALE

    x2 = centrado_x
    y2 = 125*var.SCALE
    dx2 = 500*var.SCALE
    dy2 = 71*var.SCALE

    x3 = x2
    y3 = 205*var.SCALE
    dx3 = dx2
    dy3 = dy2
    desfase_y = 90*var.SCALE

    x4 = centrado_x + dx3 + 15*var.SCALE
    y4 = 125*var.SCALE
    dx4 = 120*var.SCALE
    dy4 = 71*var.SCALE

    x5 = x4
    y5 = 205*var.SCALE
    dx5 = dx4
    dy5 = dy4

    x6 = x5 + dx5 + 15*var.SCALE
    y6 = y5
    dx6 = 150*var.SCALE
    dy6 = dy4

    x8 = x6 + dx6 + 75*var.SCALE
    y8 = y3
    dx8 = 325*var.SCALE
    dy8 = 71*var.SCALE

    x9 = x8 + dx8 + 15*var.SCALE
    y9 = y8
    dx9 = 110*var.SCALE
    dy9 = var.DY_INFO*var.SCALE

    x7 = x6 + dx6 + 75*var.SCALE
    y7 = 125*var.SCALE
    dx7 = dx8 + dx9 + 15*var.SCALE
    dy7 = 71*var.SCALE

    x10 = x8 + 8*var.SCALE
    y10 = 670*var.SCALE
    dx10 = 300*var.SCALE
    dy10 = 71*var.SCALE

    x11 = x10 + dx10
    y11 = y10 - 10*var.SCALE
    dx11 = 150*var.SCALE
    dy11 = dy4

    x15 = x8 + 8*var.SCALE
    y15 = 755*var.SCALE
    dx15 = 300*var.SCALE
    dy15 = 71*var.SCALE

    x16 = x15 + dx15
    y16 = y15 - 10*var.SCALE
    dx16 = 150*var.SCALE
    dy16 = dy4

    padding_right = 50*var.SCALE
    dx12 = 300*var.SCALE
    dy12 = 50*var.SCALE
    x12 = var.WIDTH - (dx12 + padding_right)
    y12 = var.HEIGHT - (dy12 + 50*var.SCALE) 

    dx13 = dx12
    dy13 = dy12
    x13 = var.WIDTH - (dx12 + dx13 + padding_right + 20*var.SCALE)
    y13 = var.HEIGHT - (dy13 + 50*var.SCALE)

    if tecla[pg.K_ESCAPE]:
        j_func.detener_cronometro()
        j_func.sumar_puntaje_parcial()
        j_func.reiniciar_puntaje_parcial()
        j_var.PULSADOR_PARTICIPANTE = 9
        var.PANEL_MOSTRADO = "crear_partida"


    if var.PANEL_MOSTRADO == "p_palabra_anagrama":
        if tecla[pg.K_q]:
            j_var.PULSADOR_PARTICIPANTE = 0
            print("rojo")

        elif tecla[pg.K_w]:
            j_var.PULSADOR_PARTICIPANTE = 1
            print("naranjo")

        elif tecla[pg.K_e]:
            j_var.PULSADOR_PARTICIPANTE = 2
            print("verde")

        elif tecla[pg.K_r]:
            j_var.PULSADOR_PARTICIPANTE = 3
            print("azul")

        elif tecla[pg.K_RETURN] and j_var.CRONOMETRO_INICIADO:
            print("correcto")
            j_var.PUNTAJE_PARTICIPANTES_PARCIAL[j_var.PULSADOR_PARTICIPANTE] += 1
            j_func.detener_cronometro()

        elif tecla[pg.K_BACKSPACE]:
            print("incorrecto")

        elif tecla[pg.K_SPACE]:
            if j_var.CRONOMETRO_INICIADO:
                j_func.detener_cronometro()
            else:
                j_func.iniciar_cronometro()
                j_var.MOSTRAR_PANEL = True

    if var.PANEL_MOSTRADO == "p_contrarreloj":
        if j_var.MOSTRAR_PANEL:
            if tecla[pg.K_q]:
                j_var.PULSADOR_PARTICIPANTE = 0
                print("rojo")

            elif tecla[pg.K_w]:
                j_var.PULSADOR_PARTICIPANTE = 1
                print("naranjo")

            elif tecla[pg.K_e]:
                j_var.PULSADOR_PARTICIPANTE = 2
                print("verde")

            elif tecla[pg.K_r]:
                j_var.PULSADOR_PARTICIPANTE = 3
                print("azul")

            elif tecla[pg.K_RETURN] and j_var.CRONOMETRO_INICIADO:
                print("correcto")
                j_var.PUNTAJE_PARTICIPANTES_PARCIAL[j_var.PULSADOR_PARTICIPANTE] += 1
                if var.ID_CONTRARRELOJ == 14:
                    j_func.detener_cronometro()

            elif tecla[pg.K_LEFT] and var.ID_CONTRARRELOJ > 0:
                var.ID_CONTRARRELOJ -= 1

            elif tecla[pg.K_RIGHT] and var.ID_CONTRARRELOJ < 14:
                var.ID_CONTRARRELOJ += 1

        if tecla[pg.K_SPACE]:
            if not j_var.CRONOMETRO_INICIADO:
                j_func.iniciar_cronometro()
                j_var.MOSTRAR_PANEL = True

    if var.PANEL_MOSTRADO == "p_frase_alfagrama":
        if j_var.MOSTRAR_PANEL:
            if tecla[pg.K_q]:
                j_var.PULSADOR_PARTICIPANTE = 0
                print("rojo")

            elif tecla[pg.K_w]:
                j_var.PULSADOR_PARTICIPANTE = 1
                print("naranjo")

            elif tecla[pg.K_e]:
                j_var.PULSADOR_PARTICIPANTE = 2
                print("verde")

            elif tecla[pg.K_r]:
                j_var.PULSADOR_PARTICIPANTE = 3
                print("azul")

            elif tecla[pg.K_RETURN] and j_var.CRONOMETRO_INICIADO:
                print("correcto")
                j_var.PUNTAJE_PARTICIPANTES_PARCIAL[j_var.PULSADOR_PARTICIPANTE] += 1
                #j_func.detener_cronometro()

        if tecla[pg.K_SPACE]:
            if not j_var.CRONOMETRO_INICIADO:
                j_func.iniciar_cronometro()
                j_var.MOSTRAR_PANEL = True

    if var.PANEL_MOSTRADO == "p_contrarreloj_multiple":
        if j_var.MOSTRAR_PANEL:
            if tecla[pg.K_q]:
                j_var.PULSADOR_PARTICIPANTE = 0
                print("rojo")

            elif tecla[pg.K_w]:
                j_var.PULSADOR_PARTICIPANTE = 1
                print("naranjo")

            elif tecla[pg.K_e]:
                j_var.PULSADOR_PARTICIPANTE = 2
                print("verde")

            elif tecla[pg.K_r]:
                j_var.PULSADOR_PARTICIPANTE = 3
                print("azul")

            elif tecla[pg.K_RETURN] and j_var.CRONOMETRO_INICIADO:
                print("correcto")
                j_var.PUNTAJE_PARTICIPANTES_PARCIAL[j_var.PULSADOR_PARTICIPANTE] += 1
                var.ID_CONTRARRELOJ_MULTIPLE += 1
                if var.ID_CONTRARRELOJ_MULTIPLE == var.CANTIDAD_CONTRARRELOJ_MULTIPLE:
                    j_func.detener_cronometro()

        if tecla[pg.K_SPACE]:
            if not j_var.CRONOMETRO_INICIADO:
                j_func.iniciar_cronometro()
                j_var.MOSTRAR_PANEL = True

    if var.PANEL_MOSTRADO == "p_criptocodigo":
        if tecla[pg.K_SPACE]:
            if j_var.CRONOMETRO_INICIADO:
                j_func.detener_cronometro()
            else:
                j_func.iniciar_cronometro()

        elif tecla[pg.K_RETURN] and j_var.CRONOMETRO_INICIADO:
            print("correcto")
            j_func.detener_cronometro()

        elif tecla[pg.K_BACKSPACE]:
            print("incorrecto")

    # Si estamos escribiendo en ID
    for i, panel in enumerate(var.LISTADO_PANELES):
        if var.TEXTO_ACTIVO == var.ID_LISTADO_PANELES[i]:
            if tecla[pg.K_BACKSPACE]:
                var.ID_LISTADO_PANELES[i] = var.ID_LISTADO_PANELES[i][:-1]
            elif len(var.ID_LISTADO_PANELES[i]) < var.MAXIMO_LETRAS_ID:
                var.ID_LISTADO_PANELES[i] += func.solo_numeros(evento.unicode)
            var.TEXTO_ACTIVO = var.ID_LISTADO_PANELES[i]
            
    # Si estamos escribiendo en PARTICIPANTES
    for i in range(j_var.PARTICIPANTES):
        if var.TEXTO_ACTIVO == j_var.NOMBRE_PARTICIPANTES[i]:
            if tecla[pg.K_BACKSPACE]:
                j_var.NOMBRE_PARTICIPANTES[i] = j_var.NOMBRE_PARTICIPANTES[i][:-1]
            elif len(j_var.NOMBRE_PARTICIPANTES[i]) <= var.MAXIMO_LETRAS_USERNAME:
                j_var.NOMBRE_PARTICIPANTES[i] += j_func.mayuscula(func.letras_y_espacios(evento.unicode))
            var.TEXTO_ACTIVO = j_var.NOMBRE_PARTICIPANTES[i]

            if tecla[pg.K_RETURN] or tecla[pg.K_TAB]:
                j_var.NOMBRE_PARTICIPANTES[i] = j_var.NOMBRE_PARTICIPANTES[i][:-1]

            if (tecla[pg.K_LCTRL] or tecla[pg.K_RCTRL]) and tecla[pg.K_v]:
                j_var.NOMBRE_PARTICIPANTES[i] += str(func.pegar_texto_portapapeles())
                fig.rectangulo_redondeado_con_borde_y_texto(j_var.NOMBRE_PARTICIPANTES[i], size_letra, color.AMARILLO, color.FUCSIA, color.BLANCO, x8, y8, dx8, dy8, radio, grosor)
