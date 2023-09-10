import juego.reglas as rules
import juego.funciones as func

def palabra_anagrama(anagrama):
    palabra_oculta = anagrama.get_palabra_oculta()
    cantidad_letras = anagrama.get_cantidad_letras()
    palabra_inicial_muestra = anagrama.get_palabra_inicial_muestra()
    palabra_inicial_muestra_copia = anagrama.get_palabra_inicial_muestra()
    palabra_oculta_muestra = anagrama.get_palabra_oculta_muestra()
    palabra_inicial_copia = anagrama.get_palabra_inicial_copia()

    func.limpiar_consola()
    print(palabra_inicial_muestra)
    print(palabra_oculta_muestra)

    for i in range(cantidad_letras):
        func.cronometro_segundos(3)
        func.limpiar_consola()
        palabra_inicial_copia, palabra_inicial_muestra, palabra_oculta_muestra = rules.mover_letra(palabra_inicial_copia, palabra_oculta, palabra_inicial_muestra, palabra_oculta_muestra)
        if i < cantidad_letras-1:
            print(palabra_inicial_muestra)
        else:
            print(palabra_inicial_muestra_copia)
        print(palabra_oculta_muestra)
    func.cronometro_segundos(10)

def contrarreloj(listado_anagrama):
    for i in range(len(listado_anagrama)):
        anagrama = listado_anagrama[i]
        palabra_inicial_muestra = anagrama.get_palabra_inicial_muestra()
        palabra_oculta_muestra = anagrama.get_palabra_oculta_muestra()
        palabra_oculta_muestra_copia = anagrama.get_palabra_oculta_muestra_copia()
        pista = anagrama.get_pista()

        func.limpiar_consola()
        print(palabra_inicial_muestra)
        print(palabra_oculta_muestra)
        print(f"Pista: {pista}")
        func.cronometro_segundos(3)

        func.limpiar_consola()
        print(palabra_inicial_muestra)
        print(palabra_oculta_muestra_copia)
        print(f"Pista: {pista}")

        func.cronometro_segundos(2)

def frase_alfagrama(alfagrama):
    frase = alfagrama.get_frase()
    alfagrama_generado = alfagrama.get_frase_generada()
    alfagrama_generado_muestra = alfagrama_generado
    frase_generada_muestra = alfagrama.get_frase_generada_muestra()
    pista = alfagrama.get_pista()
    letras_menos_repetida = alfagrama.get_letra_menos_repetida()
    letras_mas_repetida = alfagrama.get_letra_mas_repetida()
    cantidad_letra_menos_repetida = alfagrama.get_cantidad_letra_menos_repetida()
    cantidad_letra_mas_repetida = alfagrama.get_cantidad_letra_mas_repetida()

    func.limpiar_consola()
    print(alfagrama_generado_muestra)
    print(frase_generada_muestra)
    print(f"Pista: {pista}")
    print(f"Letra menos repetida: {letras_menos_repetida}")
    print(f"Letra más repetida: {letras_mas_repetida}")
    func.cronometro_segundos(5)

    for i in range(cantidad_letra_menos_repetida):
        alfagrama_generado_muestra = rules.borrar_letra(alfagrama_generado_muestra, letras_menos_repetida)
        frase_generada_muestra = rules.agregar_letra(frase, frase_generada_muestra, letras_menos_repetida)

    for i in range(cantidad_letra_mas_repetida):
        alfagrama_generado_muestra = rules.borrar_letra(alfagrama_generado_muestra, letras_mas_repetida)
        frase_generada_muestra = rules.agregar_letra(frase, frase_generada_muestra, letras_mas_repetida)

    func.limpiar_consola()
    print(alfagrama_generado_muestra)
    print(frase_generada_muestra)
    print(f"Pista: {pista}")
    func.cronometro_segundos(15)

def contrarreloj_multiple(listado_anagrama):
    func.limpiar_consola()
    palabra_inicial_muestra = listado_anagrama[0].get_palabra_inicial_muestra()
    palabra_oculta_muestra = listado_anagrama[0].get_palabra_oculta_muestra()
    print(palabra_inicial_muestra)
    print(palabra_oculta_muestra)
    func.cronometro_segundos(3)

    for i in range(len(listado_anagrama)):
        anagrama = listado_anagrama[i]
        palabra_inicial_muestra = anagrama.get_palabra_inicial_muestra()
        palabra_oculta_muestra = anagrama.get_palabra_oculta_muestra()
        palabra_oculta_muestra_copia = anagrama.get_palabra_oculta_muestra_copia()

        if palabra_inicial_muestra != palabra_oculta_muestra_copia:
            print(palabra_oculta_muestra_copia)
            func.cronometro_segundos(2)

    func.cronometro_segundos(10)

def criptocodigo(alfagrama, anagrama):
    frase = alfagrama.get_frase()
    alfagrama_generado = alfagrama.get_frase_generada()
    alfagrama_generado_muestra = alfagrama_generado
    frase_generada_muestra = alfagrama.get_frase_generada_muestra()
    pista_alfagrama = alfagrama.get_pista()
    letras_menos_repetida = alfagrama.get_letra_menos_repetida()
    letras_mas_repetida = alfagrama.get_letra_mas_repetida()
    cantidad_letra_menos_repetida = alfagrama.get_cantidad_letra_menos_repetida()
    cantidad_letra_mas_repetida = alfagrama.get_cantidad_letra_mas_repetida()

    palabra_oculta = anagrama.get_palabra_oculta()
    cantidad_letras = anagrama.get_cantidad_letras()
    palabra_inicial_muestra = anagrama.get_palabra_inicial_muestra()
    palabra_inicial_muestra_copia = anagrama.get_palabra_inicial_muestra()
    palabra_oculta_muestra = anagrama.get_palabra_oculta_muestra()
    palabra_inicial_copia = anagrama.get_palabra_inicial_copia()
    pista_anagrama = anagrama.get_pista()

    func.limpiar_consola()
    print(alfagrama_generado_muestra)
    print(frase_generada_muestra)
    print(palabra_oculta_muestra)
    print(f"Letra menos repetida: {letras_menos_repetida}")
    print(f"Letra más repetida: {letras_mas_repetida}")
    func.cronometro_segundos(10)

    for i in range(cantidad_letra_menos_repetida):
        alfagrama_generado_muestra = rules.borrar_letra(alfagrama_generado_muestra, letras_menos_repetida)
        frase_generada_muestra = rules.agregar_letra(frase, frase_generada_muestra, letras_menos_repetida)

    for i in range(cantidad_letra_mas_repetida):
        alfagrama_generado_muestra = rules.borrar_letra(alfagrama_generado_muestra, letras_mas_repetida)
        frase_generada_muestra = rules.agregar_letra(frase, frase_generada_muestra, letras_mas_repetida)

    func.limpiar_consola()
    print(alfagrama_generado_muestra)
    print(frase_generada_muestra)
    print(palabra_oculta_muestra)
    print(f"Pista del Alfagrama: {pista_alfagrama}")
    print(f"Pista del Anagrama: {pista_anagrama}")
    func.cronometro_segundos(30)
