import time
import filtro.ninguno as f0
import filtro.directo as f1
from algoritmos.anagrama import Anagrama

if __name__ == '__main__':
    listado_palabras = ['SOL', 'ROMA', 'CAPAS', 'SALDRE', 'ESPONJA', 'CONSERVA', 'CONSERVAR', 'CONSERVADO', 'CONSERVADOR', 'CONSERVADORA']
    #cantidades = [5, 23, 118, 719, 5039, 40319, 362878, 3628798, 39916796, 479001592]
    print("Letras \t\tCombinaciones \t\tTiempo (s) \t\tFiltro listado \t\t% Reducción listado \tTiempo (s)")

    for i, palabra in enumerate(listado_palabras):
        valor = Anagrama(1, palabra, "", "")

        inicio_f0 = time.time()
        listado, cantidad = f0.generar_listado(valor)
        final_f0 = time.time()
        tiempo_f0 = final_f0 - inicio_f0

        inicio_f1 = time.time()
        listado1, cantidad1 = f1.generar_listado(valor)
        final_f1 = time.time()
        tiempo_f1 = final_f1 - inicio_f1

        diferencia_f1 = float(100-(cantidad1*100)/cantidad)
        largo_numero = len(str(cantidad))

        if (largo_numero <= 7):
            print(f"{len(palabra)}\t\t{cantidad}\t\t\t{tiempo_f0:.6f}\t\t{cantidad1}\t\t\t{diferencia_f1:.1f}%\t\t\t{tiempo_f1:.6f}")

        elif (largo_numero == 8):
            print(f"{len(palabra)}\t\t{cantidad}\t\t{tiempo_f0:.6f}\t\t{cantidad1}\t\t\t{diferencia_f1:.1f}%\t\t\t{tiempo_f1:.6f}")

        elif (largo_numero == 9):
            print(f"{len(palabra)}\t\t{cantidad}\t\t{tiempo_f0:.6f}\t\t{cantidad1}\t\t{diferencia_f1:.1f}%\t\t\t{tiempo_f1:.6f}")


        '''
        valor = Anagrama(1, palabra, "", "")
        inicio_f1 = time.time()
        listado1, cantidad1 = f1.generar_listado(valor)
        final_f1 = time.time()
        tiempo_f1 = final_f1 - inicio_f1
        diferencia_f1 = float(100-(cantidad1*100)/cantidades[i])
        largo_numero = len(str(cantidades[i]))

        if (largo_numero <= 7):
            print(f"{len(palabra)}\t\t{cantidades[i]}\t\t\t{cantidad1}\t\t\t{diferencia_f1:.1f}%\t\t\t{tiempo_f1:.6f}")

        elif (largo_numero == 8):
            print(f"{len(palabra)}\t\t{cantidades[i]}\t\t{cantidad1}\t\t\t{diferencia_f1:.1f}%\t\t\t{tiempo_f1:.6f}")

        elif (largo_numero == 9):
            print(f"{len(palabra)}\t\t{cantidades[i]}\t\t{cantidad1}\t\t{diferencia_f1:.1f}%\t\t\t{tiempo_f1:.6f}")
        '''