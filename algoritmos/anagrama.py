import juego.reglas as rules

class Anagrama:
    def __init__(self, id, palabra_inicial, palabra_oculta, pista):
        self.id = id
        self.palabra_inicial = palabra_inicial
        self.palabra_oculta = palabra_oculta
        self.pista = pista
        self.listado = []
        self.largo_anagrama = len(palabra_inicial)
        self.cantidad_letras = 0
        self.cantidad_anagramas = 0
        self.palabra_inicial_muestra = [letra for letra in palabra_inicial]
        self.palabra_oculta_muestra = rules.reemplazar_letras_por_guion(palabra_oculta)
        self.palabra_oculta_muestra_copia = [letra for letra in palabra_oculta]
        self.palabra_inicial_copia = palabra_inicial

    def get_id(self):
        return self.id

    def get_palabra_inicial(self):
        return self.palabra_inicial
    
    def get_palabra_oculta(self):
        return self.palabra_oculta
    
    def get_pista(self):
        return self.pista
    
    def get_listado(self):
        return self.listado
    
    def get_largo_anagrama(self):
        return self.largo_anagrama
    
    def get_cantidad_letras(self):
        return len(self.palabra_inicial)
    
    def get_cantidad_anagramas(self):
        return len(self.listado)
    
    def get_palabra_inicial_muestra(self):
        return self.palabra_inicial_muestra
    
    def get_palabra_oculta_muestra(self):
        return self.palabra_oculta_muestra
    
    def get_palabra_oculta_muestra_copia(self):
        return self.palabra_oculta_muestra_copia
    
    def get_palabra_inicial_copia(self):
        return self.palabra_inicial_copia
    
    def set_palabra_inicial(self, palabra_inicial):
        self.palabra_inicial = palabra_inicial

    def set_palabra_oculta(self, palabra_oculta):
        self.palabra_oculta = palabra_oculta

    def set_listado(self, listado):
        self.listado = listado