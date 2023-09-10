import grafico.recursos.variables as var
import grafico.recursos.figuras as fig
import grafico.recursos.color as color
import grafico.recursos.funciones as func
import grafico.recursos.informacion as info
import juego.funciones as j_func
import algoritmos.alfagrama as alfagrama

def palabra_anagrama(texto):
    func.preajustes(texto)
    formula = (var.WIDTH - ((var.PADDING_X_LETRA + var.X_LETRAS + var.PADDING_X_LETRA)*len(texto)*var.SCALE))//2
    for i, letra in enumerate(texto):
        x = formula + var.PADDING_X_LETRA*var.SCALE + ((var.PADDING_X_LETRA + var.X_LETRAS + var.PADDING_X_LETRA)*i*var.SCALE)
        y = (var.HEIGHT - (var.Y_LETRAS + var.DY_INFO + var.PADDING_BOTTOM_INFO + var.PADDING_Y_LETRA)*var.SCALE)//2
        dx, dy = var.X_LETRAS*var.SCALE, var.Y_LETRAS*var.SCALE
        fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA*var.SCALE, var.COLOR_TEXTO_LETRA, color.MORADO, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)

def palabra_oculta(texto):
    func.preajustes(texto)
    formula = (var.WIDTH - ((var.PADDING_X_LETRA + var.X_LETRAS + var.PADDING_X_LETRA)*len(texto)*var.SCALE))//2
    for i, letra in enumerate(texto):
        x = formula + var.PADDING_X_LETRA*var.SCALE + ((var.PADDING_X_LETRA + var.X_LETRAS + var.PADDING_X_LETRA)*i*var.SCALE)
        y = (var.HEIGHT - (var.Y_LETRAS + var.DY_INFO + var.PADDING_BOTTOM_INFO - var.PADDING_Y_LETRA)*var.SCALE)//2
        dx, dy = var.X_LETRAS*var.SCALE, var.Y_LETRAS*var.SCALE
        fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA*var.SCALE, var.COLOR_TEXTO_LETRA, color.FUCSIA, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)
            
def frase_alfagrama(texto):
    func.preajustes(texto)
    texto = j_func.quitar_tildes(texto)
    #texto = alfagrama.generar_alfagrama(texto)
    mitad = len(texto)//2
    formula_x1 = (var.WIDTH - (var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*mitad*var.SCALE)//2
    formula_x2 = (var.WIDTH - (var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*(len(texto)-mitad)*var.SCALE)//2
    formula_y = (var.HEIGHT - ((var.PADDING_BOTTOM_INFO + var.DY_INFO) + (var.CANTIDAD_FILAS_ALFAGRAMA + var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO + var.CANTIDAD_FILAS_ANAGRAMA)*(var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL))*var.SCALE)//2

    for i, letra in enumerate(texto):
        if i < mitad:
            x = formula_x1 + (var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*i*var.SCALE + var.PADDING_X_LETRA_SMALL*var.SCALE
            y = formula_y
        else:
            x = formula_x2 + (var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*(i-mitad)*var.SCALE + var.PADDING_X_LETRA_SMALL*var.SCALE
            y = formula_y + (var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL)*var.SCALE
        dx, dy = var.X_LETRAS_SMALL*var.SCALE, var.Y_LETRAS_SMALL*var.SCALE
        fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA_SMALL*var.SCALE, var.COLOR_TEXTO_LETRA, color.MORADO, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)

def frase_oculta(texto):
    func.preajustes(texto)
    texto_original = texto
    frase_fila, largo_frases = func.separar_frase(texto)
    espaciado = (var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*var.ESCALADO_ESPACIADO*var.SCALE
    centrado_y = (var.HEIGHT - ((var.PADDING_BOTTOM_INFO + var.DY_INFO) + (var.CANTIDAD_FILAS_ALFAGRAMA + var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO + var.CANTIDAD_FILAS_ANAGRAMA)*(var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL))*var.SCALE)//2

    contador = 0
    cantidad_espacios = 0
    cantidad_espacios_anterior = 0
    fila_anterior = 0
    suma_fila_anterior = 0
    largo_frase = largo_frases[contador]
    total_espacios_fila = len(frase_fila[contador])-1
    for i, letra in enumerate(texto_original):
        if i < suma_fila_anterior + largo_frases[contador] + cantidad_espacios + cantidad_espacios_anterior:
            if letra != ' ':
                centrado_x = (var.WIDTH - ((var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*(largo_frases[contador]) + (espaciado*total_espacios_fila))*var.SCALE)//2 
                x = centrado_x + ((espaciado*cantidad_espacios) + (var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*(i-suma_fila_anterior-cantidad_espacios-cantidad_espacios_anterior))*var.SCALE
                y = centrado_y + (var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL)*contador*var.SCALE + ((var.CANTIDAD_FILAS_ALFAGRAMA)*(var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL))*var.SCALE
                dx, dy = var.X_LETRAS_SMALL*var.SCALE, var.Y_LETRAS_SMALL*var.SCALE
                fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA_SMALL*var.SCALE, var.COLOR_TEXTO_LETRA, color.FUCSIA, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)
            else:
                cantidad_espacios += 1
        else:
            largo_frase += largo_frases[contador]
            fila_anterior = largo_frases[contador]
            suma_fila_anterior += fila_anterior
            contador += 1
            cantidad_espacios += 1
            cantidad_espacios_anterior = cantidad_espacios_anterior + cantidad_espacios
            cantidad_espacios = 0
            total_espacios_fila = len(frase_fila[contador])-1
    #fig.borde(color.AMARILLO, 0, 0, var.WIDTH//2, var.HEIGHT, 1)

def palabra_oculta_criptocodigo(texto, palabra):
    func.preajustes(texto)
    formula = (var.WIDTH - ((var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*len(palabra)*var.SCALE))//2
    centrado_y = (var.HEIGHT - ((var.PADDING_BOTTOM_INFO + var.DY_INFO) + (var.CANTIDAD_FILAS_ALFAGRAMA + var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO + var.CANTIDAD_FILAS_ANAGRAMA)*(var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL))*var.SCALE)//2
    for i, letra in enumerate(palabra):
        #letra = '?'
        x = formula + var.PADDING_X_LETRA_SMALL*var.SCALE + ((var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*i*var.SCALE)
        y = centrado_y + ((var.CANTIDAD_FILAS_ALFAGRAMA + var.CANTIDAD_FILAS_ALFAGRAMA_RESUELTO)*(var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL))*var.SCALE
        dx, dy = var.X_LETRAS_SMALL*var.SCALE, var.Y_LETRAS_SMALL*var.SCALE
        fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA_SMALL*var.SCALE, var.COLOR_TEXTO_LETRA, color.CELESTE, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)

def anagrama_multiple(palabra, listado):
    maximo_filas = 5
    division_columnas = 1
    if len(listado) > 2*maximo_filas:
        division_columnas = 3
    elif len(listado) > maximo_filas:
        division_columnas = 2
        
    formula_x = (var.WIDTH - ((2*var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL)*len(palabra)*var.SCALE))//2
    formula_y = (var.HEIGHT - (var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL + (max(len(listado)//division_columnas, maximo_filas))*(var.Y_LETRAS_XSMALL + var.PADDING_Y_LETRA_XSMALL) + var.DY_INFO + var.PADDING_BOTTOM_INFO + var.PADDING_Y_LETRA_SMALL)*var.SCALE)//2
    for i, letra in enumerate(palabra):
        x = formula_x + var.PADDING_X_LETRA_SMALL*var.SCALE + ((2*var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL)*i*var.SCALE)
        y = formula_y
        dx, dy = var.X_LETRAS_SMALL*var.SCALE, var.Y_LETRAS_SMALL*var.SCALE
        fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA_SMALL*var.SCALE, var.COLOR_TEXTO_LETRA, color.MORADO, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)
       
    formula_x = (var.WIDTH - ((2*var.PADDING_X_LETRA_XSMALL + var.X_LETRAS_XSMALL + 0.5*var.PADDING_X_LETRA_XSMALL)*(division_columnas*len(palabra))*var.SCALE))//2
    for i, texto in enumerate(listado):
        if i%maximo_filas == 0:
            desfase_x = (2*var.PADDING_X_LETRA_XSMALL + var.X_LETRAS_XSMALL + var.PADDING_X_LETRA_XSMALL)*(len(palabra)*(i//maximo_filas))*var.SCALE
        for j, letra in enumerate(texto):
            x = formula_x + desfase_x + var.PADDING_X_LETRA_XSMALL*var.SCALE + ((var.PADDING_X_LETRA_XSMALL + var.X_LETRAS_XSMALL + var.PADDING_X_LETRA_XSMALL)*j*var.SCALE)
            y = formula_y + (var.Y_LETRAS_SMALL + var.PADDING_Y_LETRA_SMALL)*var.SCALE + (i%maximo_filas)*(var.Y_LETRAS_XSMALL + var.PADDING_Y_LETRA_XSMALL)*var.SCALE
            #letra = '_'
            dx, dy = var.X_LETRAS_XSMALL*var.SCALE, var.Y_LETRAS_XSMALL*var.SCALE
            fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA_XSMALL*var.SCALE, var.COLOR_TEXTO_LETRA, color.FUCSIA, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)
        
def logo(texto, px, py, escala):
    func.preajustes(texto)
    formula = px
    for i, letra in enumerate(texto):
        x = formula + (var.PADDING_X_LETRA_SMALL*escala*var.SCALE) + ((var.PADDING_X_LETRA_SMALL + var.X_LETRAS_SMALL + var.PADDING_X_LETRA_SMALL)*escala*var.SCALE*i)
        y = py
        dx, dy = var.X_LETRAS_SMALL*escala*var.SCALE, var.Y_LETRAS_SMALL*escala*var.SCALE
        if j_func.cantidad_vocales(letra):
            color_defecto = color.FUCSIA
        else:
            color_defecto = color.MORADO
        fig.rectangulo_redondeado_con_borde_y_texto(letra, var.SIZE_LETRA_SMALL*escala*var.SCALE, var.COLOR_TEXTO_LETRA, color_defecto, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)

def boton(texto, x, y):
    x = x*var.SCALE + (var.WIDTH - ((var.PADDING_X_BOTON + var.X_BOTON)*var.SCALE))//2
    y = y*var.SCALE + (var.HEIGHT - (var.Y_BOTON)*var.SCALE)//2
    dx, dy = var.X_BOTON*var.SCALE, var.Y_BOTON*var.SCALE
    fig.rectangulo_redondeado_con_borde_y_texto(texto, var.SIZE_BOTON*var.SCALE, var.COLOR_TEXTO_LETRA, color.CELESTE, color.BORDE_AMARILLO, x, y, dx, dy, var.BORDE_RADIO_LETRA*var.SCALE, var.GROSOR_BORDE_LETRA*var.SCALE)
