import pymysql

class DataBaseJuego:
    def __init__(self):
        self.conexion = pymysql.connect(host='107.167.93.202',
                                    user='jookeezc_criptojookeez',
                                    password='c0ntr4$3n4_',
                                    db='jookeezc_criptograma')
        self.cursor = self.conexion.cursor()

    def get_conexion(self):
        return self.conexion

    def get_cursor(self):
        return self.cursor
    
    def get_close(self):
        return self.conexion.close()

# CREAR PANEL
def agregar_palabra_anagrama(palabra_mostrar, palabra_oculta, username):
    nueva_conexion = DataBaseJuego()
    sql = "INSERT INTO PalabraAnagrama (palabra_a_mostrar, palabra_oculta, usuario) VALUES ('{}', '{}', '{}')".format(palabra_mostrar, palabra_oculta, username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def editar_palabra_anagrama(id, palabra_mostrar, palabra_oculta, username):
    nueva_conexion = DataBaseJuego()
    sql = "UPDATE PalabraAnagrama SET palabra_a_mostrar = '{}', palabra_oculta = '{}', usuario = '{}' WHERE id = {}".format(palabra_mostrar, palabra_oculta, username, id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def consultar_palabra_anagrama(id):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT palabra_a_mostrar, palabra_oculta FROM PalabraAnagrama WHERE id = {}".format(id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise

def agregar_contrarreloj(id_panel, contenido_contrarreloj, username):
    for i, contenido in enumerate(contenido_contrarreloj):
        nueva_conexion = DataBaseJuego()
        palabra_a_mostrar = contenido[1]
        anagrama_oculto = contenido[2]
        pista = contenido[3]
        sql = "INSERT INTO Contrarreloj (id_panel, palabra_a_mostrar, anagrama_oculto, pista, usuario) VALUES ({}, '{}', '{}', '{}', '{}')".format(id_panel, palabra_a_mostrar, anagrama_oculto, pista, username)
        try:
            nueva_conexion.get_cursor().execute(sql)
            nueva_conexion.get_conexion().commit()
            nueva_conexion.get_close()

        except Exception as e:
            raise

def editar_contrarreloj(id_panel, contenido_contrarreloj, username):
    for i, contenido in enumerate(contenido_contrarreloj):
        nueva_conexion = DataBaseJuego()
        palabra_a_mostrar = contenido[1]
        anagrama_oculto = contenido[2]
        pista = contenido[3]
        sql = "UPDATE Contrarreloj SET palabra_a_mostrar = '{}', anagrama_oculto = '{}', pista = '{}', usuario = '{}' WHERE id_panel = {}".format(palabra_a_mostrar, anagrama_oculto, pista, username, id_panel)
        try:
            nueva_conexion.get_cursor().execute(sql)
            nueva_conexion.get_conexion().commit()
            nueva_conexion.get_close()

        except Exception as e:
            raise

def consultar_contrarreloj(id_panel):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT palabra_a_mostrar, anagrama_oculto, pista FROM Contrarreloj WHERE id_panel = {}".format(id_panel)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchall()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise

def agregar_frase_alfagrama(frase_oculta, alfagrama, pista, username):
    nueva_conexion = DataBaseJuego()
    sql = "INSERT INTO FraseAlfagrama (frase_oculta, texto_alfagrama, pista, usuario) VALUES ('{}', '{}', '{}', '{}')".format(frase_oculta, alfagrama, pista, username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def editar_frase_alfagrama(id, frase_oculta, alfagrama, pista, username):
    nueva_conexion = DataBaseJuego()
    sql = "UPDATE FraseAlfagrama SET frase_oculta = '{}', texto_alfagrama = '{}', pista = '{}' , usuario = '{}' WHERE id = {}".format(frase_oculta, alfagrama, pista, username, id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def consultar_frase_alfagrama(id):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT frase_oculta, pista FROM FraseAlfagrama WHERE id = {}".format(id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise

def agregar_contrarreloj_multiple(palabra_a_mostrar, anagrama_oculto, username):
    nueva_conexion = DataBaseJuego()
    sql = "INSERT INTO ContrarrelojMultiple (palabra_a_mostrar, anagrama_oculto, usuario) VALUES ('{}', '{}', '{}')".format(palabra_a_mostrar, anagrama_oculto, username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def editar_contrarreloj_multiple(id, palabra_a_mostrar, anagrama_oculto, username):
    nueva_conexion = DataBaseJuego()
    sql = "UPDATE ContrarrelojMultiple SET palabra_a_mostrar = '{}', anagrama_oculto = '{}' , usuario = '{}' WHERE id = {}".format(palabra_a_mostrar, anagrama_oculto, username, id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def consultar_contrarreloj_multiple(id):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT palabra_a_mostrar, anagrama_oculto FROM ContrarrelojMultiple WHERE id = {}".format(id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise

def agregar_criptocodigo(frase_oculta, texto_alfagrama, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama, letra_mas_repetida, letra_menos_repetida, username):
    nueva_conexion = DataBaseJuego()
    sql = "INSERT INTO Criptocodigo (frase_oculta, texto_alfagrama, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama, letra_mas_repetida, letra_menos_repetida, usuario) VALUES ('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(frase_oculta, texto_alfagrama, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama, letra_mas_repetida, letra_menos_repetida, username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def editar_criptocodigo(id, frase_oculta, texto_alfagrama, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama, letra_mas_repetida, letra_menos_repetida, username):
    nueva_conexion = DataBaseJuego()
    sql = "UPDATE Criptocodigo SET frase_oculta = '{}', texto_alfagrama = '{}', pista_alfagrama = '{}', anagrama_de_la_frase = '{}', anagrama_oculto = '{}', pista_anagrama = '{}', letra_mas_repetida = '{}', letra_menos_repetida = '{}', usuario = '{}' WHERE id = {}".format(frase_oculta, texto_alfagrama, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama, letra_mas_repetida, letra_menos_repetida, username, id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def consultar_criptocodigo(id):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT frase_oculta, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama FROM Criptocodigo WHERE id = {}".format(id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise


# CREAR PARTIDA 
def consultar_panel_palabra_anagrama(id):
    return consultar_palabra_anagrama(id)

def consultar_panel_contrarreloj(id_panel):
    return consultar_contrarreloj(id_panel)

def consultar_panel_frase_alfagrama(id):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT frase_oculta, texto_alfagrama, pista FROM FraseAlfagrama WHERE id = {}".format(id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise

def consultar_panel_contrarreloj_multiple(id_panel):
    return consultar_contrarreloj_multiple(id_panel)

def consultar_panel_criptocodigo(id):
    nueva_conexion = DataBaseJuego()
    sql = "SELECT frase_oculta, texto_alfagrama, pista_alfagrama, anagrama_de_la_frase, anagrama_oculto, pista_anagrama, letra_mas_repetida, letra_menos_repetida FROM Criptocodigo WHERE id = {}".format(id)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise