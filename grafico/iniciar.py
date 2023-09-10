import pygame as pg
import pygame_gui as gui
import os
import grafico.recursos.variables as var
import grafico.pantalla.home as home
import grafico.pantalla.login as login
import grafico.pantalla.creditos as creditos
import grafico.pantalla.datos_usuario as datos_usuario
import grafico.pantalla.crear_partida as p_crear_partida
import grafico.pantalla.crear_palabras as p_crear_palabras
import grafico.pantalla.crear_panel as p_crear_panel
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
import grafico.pantalla.reglas.palabra_anagrama as r_palabra_anagrama
import grafico.pantalla.reglas.contrarreloj as r_contrarreloj
import grafico.pantalla.reglas.frase_alfagrama as r_frase_alfagrama
import grafico.pantalla.reglas.contrarreloj_multiple as r_contrarreloj_multiple
import grafico.pantalla.reglas.criptocodigo as r_criptocodigo


def iniciar_ventana():
    pg.init()
    pg.display.set_caption("Criptograma by @jookeez")
    pg.display.set_icon(pg.image.load(os.path.join('grafico/imagenes', 'favicon.png')))

def refrescar_ventana():
    pg.display.flip()
    pg.display.update()

def mostrar_contenido(panel):
    var.PANEL_MOSTRADO = panel
    panel_reglas = var.PANEL_REGLAS
    crear_paneles = var.PANEL_CREAR
    
    if panel == "crear_palabras":
        p_crear_palabras.contenido()

    #CREAR PANELES
    elif panel == "crear_panel":
        if crear_paneles == "cp_palabra_anagrama":
            cp_palabra_anagrama.contenido()

        elif crear_paneles == "cp_contrarreloj":
            cp_contrarreloj.contenido()

        elif crear_paneles == "cp_frase_alfagrama":
            cp_frase_alfagrama.contenido()

        elif crear_paneles == "cp_contrarreloj_multiple":
            cp_contrarreloj_multiple.contenido()

        elif crear_paneles == "cp_criptocodigo":
            cp_criptocodigo.contenido()

        else:
            p_crear_panel.contenido()
            var.PANEL_CREAR = "default"

    # CREAR PARTIDAS Y JUGAR
    elif panel == "crear_partida":
        p_crear_partida.contenido()

    elif panel == "p_palabra_anagrama":
        p_palabra_anagrama.contenido()

    elif panel == "p_contrarreloj":
        p_contrarreloj.contenido()

    elif panel == "p_frase_alfagrama":
        p_frase_alfagrama.contenido()

    elif panel == "p_contrarreloj_multiple":
        p_contrarreloj_multiple.contenido()

    elif panel == "p_criptocodigo":
        p_criptocodigo.contenido()

    #MENU INFERIOR
    elif panel == "home":
        home.contenido()

    elif panel == "reglas":
        #REGLAS
        if panel_reglas == "r_palabra_anagrama":
            r_palabra_anagrama.contenido()

        elif panel_reglas == "r_contrarreloj":
            r_contrarreloj.contenido()

        elif panel_reglas == "r_frase_alfagrama":
            r_frase_alfagrama.contenido()

        elif panel_reglas == "r_contrarreloj_multiple":
            r_contrarreloj_multiple.contenido()

        elif panel_reglas == "r_criptocodigo":
            r_criptocodigo.contenido()

    elif panel == "creditos":
        creditos.contenido()

    elif panel == "datos_usuario":
        datos_usuario.contenido()

    elif panel == "login":
        login.contenido()

    elif panel == "logout":
        login.contenido()
