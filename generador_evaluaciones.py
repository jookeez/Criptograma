import time
import filtro.ninguno as f0
import filtro.directo as f1
import filtro.busqueda as buscar
import juego.funciones as func
from algoritmos.anagrama import Anagrama

if __name__ == '__main__':
    listado_palabras = ['SOL', 'ROMA', 'CAPAS', 'SALDRE', 'ESPONJA', 'CONSERVA', 'CONSERVAR', 'CONSERVADO', 'CONSERVADOR', 'CONSERVADORA']

    for palabra in listado_palabras:
        palabra = func.mayuscula(palabra)
        valor = Anagrama(1, palabra, "", "")

        inicio_f0 = time.time()
        listado, cantidad = f0.generar_listado(valor)
        listado, cantidad0 = buscar.revisar(palabra, listado)
        final_f0 = time.time()
        tiempo_f0 = final_f0 - inicio_f0

        inicio_f1 = time.time()
        listado1, cantidad1 = f1.generar_listado(valor)
        listado1, cantidad_combinaciones = buscar.revisar(palabra, listado1)
        final_f1 = time.time()
        tiempo_f1 = final_f1 - inicio_f1

        diferencia_f1 = float(100-(cantidad1*100)/cantidad)
        largo_numero = len(str(cantidad))

        print("Letras \tCombinaciones \tTiempo (s) \tFiltro listado \t% Reducción \tCombinaciones \tTiempo (s) \tPalabra")
        if (largo_numero <= 7):
            print(f"{len(palabra)}\t{cantidad}\t\t{tiempo_f0:.6f}\t{cantidad1}\t\t{diferencia_f1:.1f}%\t\t{cantidad_combinaciones}\t\t{tiempo_f1:.6f}\t{palabra}")

        elif (largo_numero == 8):
            print(f"{len(palabra)}\t{cantidad}\t{tiempo_f0:.6f}\t{cantidad1}\t\t{diferencia_f1:.1f}%\t\t{cantidad_combinaciones}\t\t{tiempo_f1:.6f}\t{palabra}")

        elif (largo_numero == 9):
            print(f"{len(palabra)}\t{cantidad}\t{tiempo_f0:.6f}\t{cantidad1}\t{diferencia_f1:.1f}%\t\t{cantidad_combinaciones}\t\t{tiempo_f1:.6f}\t{palabra}")

        if len(listado1):
            print(f'{len(listado1)} resultados: {listado1}')
        else:
            print('Sin resultados.')
