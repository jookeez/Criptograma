import juego.reglas as rules
import juego.funciones as func

class Alfagrama:
    def __init__(self, id, frase, pista):
        self.id = id
        self.frase = frase
        self.frase_generada = generar_alfagrama(frase)
        self.pista = pista
        self.frase_muestra = [letra for letra in frase]
        self.frase_generada_muestra = rules.reemplazar_letras_por_guion(self.frase_muestra)
        self.letra_menos_repetida, self.cantidad_letra_menos_repetida = buscar_letra_menos_repetida(self.frase_generada)
        self.letra_mas_repetida, self.cantidad_letra_mas_repetida = buscar_letra_mas_repetida(self.frase_generada)

    def get_id(self):
        return self.id

    def get_frase(self):
        return self.frase
    
    def get_frase_generada(self):
        return self.frase_generada

    def get_pista(self):
        return self.pista
    
    def get_frase_muestra(self):
        return self.frase_muestra
    
    def get_frase_generada_muestra(self):
        return self.frase_generada_muestra
    
    def get_letra_mas_repetida(self):
        return self.letra_mas_repetida
    
    def get_letra_menos_repetida(self):
        return self.letra_menos_repetida
    
    def get_cantidad_letra_mas_repetida(self):
        return self.cantidad_letra_mas_repetida
    
    def get_cantidad_letra_menos_repetida(self):
        return self.cantidad_letra_menos_repetida
    
    def set_frase_generada(self, frase_generada):
        self.frase_generada = frase_generada

def generar_alfagrama(frase):
    for buscar in frase:
        if not func.es_letra(buscar):
            frase = frase.replace(buscar, '')
    letras = list(frase)
    letras.sort()
    return letras

def generar_alfagrama_en_palabra(alfagrama):
    alfagrama = generar_alfagrama(alfagrama)
    palabra = ""
    for letra in alfagrama:
        palabra += letra
    return palabra


def buscar_letra_mas_repetida(frase):
    contador_letras = {}
    for letra in frase:
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
    
    letra_mas_repetida = ''
    contador_max = 0
    for letra, contador in contador_letras.items():
        if func.es_letra(letra) and contador > contador_max:
            letra_mas_repetida = letra
            contador_max = contador
    return letra_mas_repetida, contador_max

def buscar_letra_menos_repetida(frase):
    contador_letras = {}
    for letra in frase:
        if letra in contador_letras:
            contador_letras[letra] += 1
        else:
            contador_letras[letra] = 1
    
    letra_menos_repetida = None
    contador_min = float('inf')

    for letra, contador in contador_letras.items():
        if func.es_letra(letra) and contador < contador_min:
            letra_menos_repetida = letra
            contador_min = contador
    return letra_menos_repetida, contador_min

