import juego.funciones as func

def principal():
    func.limpiar_consola()
    print("----- C R I P T O G R A M A -----")
    print("-         [1] Reglas            -")
    print("-         [2] Jugar             -")
    print("-         [3] Ajustes           -")
    print("-         [0] Salir             -")
    print("---------------------------------")

def jugar():
    func.limpiar_consola()
    print("----------- J U G A R -----------")
    print("-   [1] Palabra anagrama        -")
    print("-   [2] Contrarreloj            -")
    print("-   [3] Alfagrama               -")
    print("-   [4] Contrarreloj múltiple   -")
    print("-   [5] Criptocódigo            -")
    print("-   [0] Salir                   -")
    print("---------------------------------")

def salir():
    func.salir()