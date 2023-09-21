import pymysql

class DataBaseUsuario:
    def __init__(self):
        self.conexion = pymysql.connect(host='',
                                    user='',
                                    password='',
                                    db='')
        self.cursor = self.conexion.cursor()

    def get_conexion(self):
        return self.conexion

    def get_cursor(self):
        return self.cursor
    
    def get_close(self):
        return self.conexion.close()

def iniciar_sesion(username):
    nueva_conexion = DataBaseUsuario()
    sql = "SELECT passwd, tipo_usuario FROM Usuario WHERE username = '{}'".format(username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        nueva_conexion.get_close()
        return datos

    except Exception as e:
        raise

def cambiar_clave(username, clave_nueva):
    nueva_conexion = DataBaseUsuario()
    sql = "UPDATE Usuario SET passwd = '{}' WHERE username = '{}'".format(clave_nueva, username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def cambiar_tipo_usuario(username, tipo):
    nueva_conexion = DataBaseUsuario()
    sql = "UPDATE Usuario SET tipo_usuario = '{}' WHERE username = '{}'".format(tipo, username)
    try:
        nueva_conexion.get_cursor().execute(sql)
        nueva_conexion.get_conexion().commit()
        nueva_conexion.get_close()

    except Exception as e:
        raise

def verificar_palabra_clave():
    nueva_conexion = DataBaseUsuario()
    sql = "SELECT palabra FROM PalabraClave"
    try:
        nueva_conexion.get_cursor().execute(sql)
        datos = nueva_conexion.get_cursor().fetchone()
        palabra_clave = datos[0]

        nueva_conexion.get_close()
        return palabra_clave

    except Exception as e:
        raise
