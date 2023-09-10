def actual():
    nombre_archivo = f"archivos/version.txt"
    contenido = 0
    with open(nombre_archivo, encoding='utf8') as archivo:
        for linea in archivo:
            contenido = int(linea)

    contenido += 1
    with open(nombre_archivo, "w") as archivo:
        nuevo_contenido = str(contenido)
        archivo.write(nuevo_contenido)

    return contenido

'''
La numeración de versiones se utiliza para indicar el estado y el 
progreso del desarrollo de software. En la convención común de 
numeración de versiones llamada "Semantic Versioning" o "SemVer", la 
numeración está formada por tres partes: MAJOR.MINOR.PATCH.

MAJOR: El número mayor indica cambios significativos e incompatibles 
con versiones anteriores. Si hay un aumento en el número mayor, significa 
que ha habido cambios importantes que pueden afectar la funcionalidad 
anterior del programa.

MINOR: El número menor indica cambios que agregan nuevas características 
o mejoras sin romper la compatibilidad con versiones anteriores. Si hay 
un aumento en el número menor, significa que se han agregado nuevas 
funcionalidades al programa.

PATCH: El número de parche indica cambios menores, como corrección de 
errores o arreglos pequeños, sin afectar la funcionalidad principal. 
Si hay un aumento en el número de parche, significa que se han realizado 
correcciones o mejoras menores.
'''