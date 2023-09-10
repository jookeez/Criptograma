def leer(nombre):
    nombre_archivo = f"archivos/{nombre}.txt"
    contenido = []
    with open(nombre_archivo, encoding='utf8') as archivo:
        for linea in archivo:
            linea = linea.replace("\n", "")
            if linea != '':
                contenido.append(linea)
    return contenido
