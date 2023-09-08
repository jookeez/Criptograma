import re
import juego.funciones as func

def eliminar_palabras_duplicadas(lista):
    lista_sin_duplicados = list(set(lista))
    return lista_sin_duplicados

def leer_archivos_y_generar_listado(archivos_entrada, archivo_salida):
    # Crear un conjunto para almacenar las palabras no repetidas
    contenido = []

    # Leer los archivos de entrada y agregar las palabras al conjunto
    for nombre_archivo in archivos_entrada:
        with open(nombre_archivo, "r", encoding='utf8') as archivo:
            for linea in archivo:
                linea = linea.replace("\n", "")
                linea = linea.replace("-", "")
                linea = linea.replace(" ", "")
                linea = linea.replace("'", "")
                #linea = eliminar_palabras_no_letra(linea)
                if linea != '' and len(linea) > 2:
                    linea = func.mayuscula(linea)
                    contenido.append(linea)

    # Convertir el conjunto en una lista y ordenarla alfabéticamente
    listado_final = sorted(eliminar_palabras_duplicadas(contenido))

    # Escribir el listado final en el archivo de salida
    with open(archivo_salida, "w", encoding='utf8') as archivo:
        archivo.write("\n".join(listado_final))


def actual():
    nombre_archivo = f"archivos/diccionario/nuevo_lemario.txt"
    contenido = []
    with open(nombre_archivo, encoding='utf8') as archivo:
        for linea in archivo:
            linea = linea.replace("\n", "")
            linea = linea.replace("-", "")
            linea = linea.replace(" ", "")
            linea = linea.replace("'", "")
            contenido.append(linea)
    return contenido

def guardar_palabras_por_longitud(palabras):
    palabras_por_longitud = {}
    for palabra in palabras:
        longitud = len(palabra)
        if longitud not in palabras_por_longitud:
            palabras_por_longitud[longitud] = []
        palabras_por_longitud[longitud].append(palabra)

    for longitud, lista_palabras in palabras_por_longitud.items():
        nombre_archivo = f"archivos/diccionario/{longitud}.txt"
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write("\n".join(lista_palabras))

if __name__ == '__main__':
    # Ejemplo de uso:
    archivos_entrada = ["archivos/diccionario/apellidos-es.txt", "archivos/diccionario/lemario.txt", "archivos/diccionario/nombres-propios-ar.txt", "archivos/diccionario/nombres-propios-es.txt", "archivos/diccionario/verbos-espanol.txt"]
    archivo_salida = "archivos/diccionario/nuevo_lemario.txt"
    leer_archivos_y_generar_listado(archivos_entrada, archivo_salida)

    guardar_palabras_por_longitud(actual())