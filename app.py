import juego.paneles as panel
import juego.menu as menu
import juego.cargar_datos as cargar

if __name__ == '__main__':

    while True:
        menu.principal()
        valor = ''
        valor = input("-> ")

        if valor == "1": # Reglas
            pass

        elif valor == "2": # Jugar
            while True:
                menu.jugar()
                valor = input("-> ")
                if valor == "1":
                    datos = cargar.palabra_anagrama()
                    panel.palabra_anagrama(datos)

                elif valor == "2":
                    datos = cargar.contrarreloj()
                    panel.contrarreloj(datos)

                elif valor == "3":
                    datos = cargar.frase_alfagrama()
                    panel.frase_alfagrama(datos)

                elif valor == "4":
                    datos = cargar.contrarreloj_multiple()
                    panel.contrarreloj_multiple(datos)

                elif valor == "5":
                    datos_alfagrama, datos_anagrama = cargar.criptocodigo()
                    panel.criptocodigo(datos_alfagrama, datos_anagrama)

                elif valor == "0":
                    break

                elif valor == "00":
                    menu.salir()


        elif valor == "3": # Ajustes
            pass

        elif valor == "0" or valor == "00": # Salir
            menu.salir()

        else:
            print("No válido")