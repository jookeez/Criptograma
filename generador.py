import time
import filtro.directo as f1
import filtro.busqueda as buscar
import juego.funciones as func
from algoritmos.anagrama import Anagrama
from algoritmos.alfagrama import Alfagrama

if __name__ == '__main__':
    palabra = input("-> ")

    palabra = func.mayuscula(palabra)
    valor = Anagrama(1, palabra, "", "")

    inicio_f1 = time.time()
    listado1, cantidad1 = f1.generar_listado(valor)
    listado1, cantidad_combinaciones = buscar.revisar(palabra, listado1)
    final_f1 = time.time()
    tiempo_f1 = final_f1 - inicio_f1

    if len(listado1):
        print(f'{len(listado1)} resultados: {listado1}')
    else:
        print('Sin resultados.')

    print(f'Tiempo de ejecución: {tiempo_f1:.4f} segundos.')

def buscar_anagrama(palabra):
    palabra = func.mayuscula(palabra)
    valor = Anagrama(1, palabra, "", "")

    inicio_f1 = time.time()
    listado1, cantidad1 = f1.generar_listado(valor)
    listado1, cantidad_combinaciones = buscar.revisar(palabra, listado1)
    final_f1 = time.time()
    tiempo_f1 = final_f1 - inicio_f1
    return len(listado1), listado1, tiempo_f1

def buscar_alfagrama(frase):
    valor = Alfagrama(1, frase, "")
    return valor.get_frase_generada()
