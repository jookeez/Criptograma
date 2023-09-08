import pygame as pg
import juego.funciones as j_func
import otros.version as ver
import grafico.recursos.funciones as func
import grafico.recursos.variables as var
import grafico.iniciar as init
import grafico.pantalla.menu as p_menu
import grafico.pantalla.reglas.menu as r_menu
import grafico.pantalla.login as login
import grafico.pantalla.creditos as creditos
import grafico.pantalla.crear_panel as crear_panel
import grafico.pantalla.crear_partida as crear_partida
import grafico.pantalla.crear_palabras as crear_palabras
import grafico.pantalla.datos_usuario as datos_usuario
import grafico.pantalla.crear_paneles.palabra_anagrama as cp_palabra_anagrama
import grafico.pantalla.crear_paneles.contrarreloj as cp_contrarreloj
import grafico.pantalla.crear_paneles.frase_alfagrama as cp_frase_alfagrama
import grafico.pantalla.crear_paneles.contrarreloj_multiple as cp_contrarreloj_multiple
import grafico.pantalla.crear_paneles.criptocodigo as cp_criptocodigo

init.iniciar_ventana()

if __name__ == '__main__':
    clock = pg.time.Clock()
    var.VERSION_PATCH = ver.actual()

    while True:
        UI_REFRESH_RATE = clock.tick(var.FPS)
        init.mostrar_contenido(var.PANEL_MOSTRADO)
        for evento in pg.event.get():
            ''' Habilita la X de la ventana '''
            if evento.type == pg.QUIT:
                func.salir()

            ''' Redimensiona la ventana '''
            if evento.type == pg.VIDEORESIZE:
                if evento.w < var.MIN_WIDTH:
                    evento.w = var.MIN_WIDTH
                if evento.h < var.MIN_HEIGHT:
                    evento.h = var.MIN_HEIGHT
                var.WIDTH, var.HEIGHT = evento.w, evento.h
                SCALE_X, SCALE_Y = (evento.w*100)/var.WIDTH_ORIGINAL, (evento.h*100)/var.HEIGHT_ORIGINAL
                var.SCALE = min(SCALE_X, SCALE_Y)/100
                var.SURFACE = pg.display.set_mode((var.WIDTH, var.HEIGHT), pg.RESIZABLE)

            if evento.type == pg.MOUSEBUTTONDOWN:
                pos_x_mouse, pos_y_mouse = evento.pos
                
                for menu in var.MENU_PRINCIPAL:
                    if var.PANEL_MOSTRADO == menu:
                        p_menu.evento_botones(pos_x_mouse, pos_y_mouse)

                for rule in var.MENU_REGLAS:
                    if var.PANEL_REGLAS == rule:
                        r_menu.evento_botones(pos_x_mouse, pos_y_mouse)

                if var.PANEL_MOSTRADO == "crear_panel":
                    if var.PANEL_CREAR == "cp_palabra_anagrama":
                        cp_palabra_anagrama.evento_botones(pos_x_mouse, pos_y_mouse)
                    elif var.PANEL_CREAR == "cp_contrarreloj":
                        cp_contrarreloj.evento_botones(pos_x_mouse, pos_y_mouse)
                    elif var.PANEL_CREAR == "cp_frase_alfagrama":
                        cp_frase_alfagrama.evento_botones(pos_x_mouse, pos_y_mouse)
                    elif var.PANEL_CREAR == "cp_contrarreloj_multiple":
                        cp_contrarreloj_multiple.evento_botones(pos_x_mouse, pos_y_mouse)
                    elif var.PANEL_CREAR == "cp_criptocodigo":
                        cp_criptocodigo.evento_botones(pos_x_mouse, pos_y_mouse)
                    else:
                        crear_panel.evento_botones(pos_x_mouse, pos_y_mouse)

                if var.PANEL_MOSTRADO == "login":
                    login.evento_botones(pos_x_mouse, pos_y_mouse)

                if var.PANEL_MOSTRADO == "crear_partida":
                    crear_partida.evento_botones(pos_x_mouse, pos_y_mouse)
                
                if var.PANEL_MOSTRADO == "crear_palabras":
                    crear_palabras.evento_botones(pos_x_mouse, pos_y_mouse)

                if var.PANEL_MOSTRADO == "creditos":
                    creditos.evento_botones(pos_x_mouse, pos_y_mouse)

                if var.PANEL_MOSTRADO == "datos_usuario":
                    datos_usuario.evento_botones(pos_x_mouse, pos_y_mouse)

            tecla = pg.key.get_pressed()
            if evento.type == pg.KEYDOWN:
                for menu in var.MENU_PANELES:
                    if var.PANEL_MOSTRADO == menu:
                        crear_partida.evento_teclado(evento, tecla)

                if var.PANEL_MOSTRADO == "login":
                    login.evento_teclado(evento, tecla)

                elif var.PANEL_MOSTRADO == "crear_palabras":
                    crear_palabras.evento_teclado(evento, tecla)

                elif var.PANEL_MOSTRADO == "crear_panel":
                    if var.PANEL_CREAR == "cp_palabra_anagrama":
                        cp_palabra_anagrama.evento_teclado(evento, tecla)
                    elif var.PANEL_CREAR == "cp_contrarreloj":
                        cp_contrarreloj.evento_teclado(evento, tecla)
                    elif var.PANEL_CREAR == "cp_frase_alfagrama":
                        cp_frase_alfagrama.evento_teclado(evento, tecla)
                    elif var.PANEL_CREAR == "cp_contrarreloj_multiple":
                        cp_contrarreloj_multiple.evento_teclado(evento, tecla)
                    elif var.PANEL_CREAR == "cp_criptocodigo":
                        cp_criptocodigo.evento_teclado(evento, tecla)
                
                elif var.PANEL_MOSTRADO == "crear_partida":
                    crear_partida.evento_teclado(evento, tecla)

                elif var.PANEL_MOSTRADO == "datos_usuario":
                    datos_usuario.evento_teclado(evento, tecla)

        j_func.cronometro_iniciado()
        # Coloca aquí el código para dibujar y actualizar la ventana.
        init.refrescar_ventana()
