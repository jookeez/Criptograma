import threading
import juego.funciones as func

filtro_consonantes_entre = 5
filtro_vocales_entre = 5
filtro_consonantes_inicio_final = 3

#hilo_cronometro = threading.Thread(target=func.cronometro)

PARTICIPANTES = 2
NOMBRE_PARTICIPANTES = ["", "", "", ""]
PUNTAJE_PARTICIPANTES_PARCIAL = [0, 0, 0, 0]
PUNTAJE_PARTICIPANTES = [0, 0, 0, 0]
PULSADOR_PARTICIPANTE = 9

TIEMPO_TOTAL_JUEGO = "30"

MOSTRAR_PANEL = False
CRONOMETRO_INICIADO = False
CRONOMETRO_INICIO = 0
AUXILIAR_INICIO = 1
TIEMPO_PARCIAL_JUEGO = "0:00"
TIEMPO_TOTAL_JUEGO_SEGUNDOS = 0
TIEMPO_TOTAL_JUEGO = "0:00"
TIEMPO_TOTAL_PANELES = ["2:00", "5:00", "2:00", "10:00"]