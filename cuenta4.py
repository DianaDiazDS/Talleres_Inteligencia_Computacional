import numpy as np

def inicializar_tablero(filas, columnas):
    return np.zeros((filas, columnas), dtype=int)

def imprimir_tablero(tablero):
    # Imprimir los números de las columnas
    print(" ".join(str(i) for i in range(len(tablero[0]))))
    print("-" * (2 * len(tablero[0]) - 1))

    for fila in tablero:
        print(' '.join(['X' if celda == 1 else 'O'
        if celda == -1 else '.' for celda in fila]))

def es_movimiento_valido(tablero, columna):
    return tablero[0][columna] == 0

def realizar_movimiento(tablero, columna, jugador):
    for fila in range(len(tablero) - 1, -1, -1):
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = jugador
            break
    return tablero

def obtener_movimientos(tablero):
    return [col for col in range(len(tablero[0]))
            if es_movimiento_valido(tablero, col)]

def evaluar_estado(tablero, jugador):
    return (np.sum(tablero == jugador) -
            np.sum(tablero == -jugador))

def es_terminal(tablero):
    # Verifica si hay cuatro fichas consecutivas en filas, columnas o diagonales.
    for jugador in [-1, 1]:  # Verifica para ambos jugadores
        # Verifica filas
        for fila in range(len(tablero) - 3):
            for col in range(len(tablero[0])):
                if np.all(tablero[fila:fila+4, col] == jugador):
                    return True

        # Verifica columnas
        for col in range(len(tablero[0]) - 3):
            for fila in range(len(tablero)):
                if np.all(tablero[fila, col:col+4] == jugador):
                    return True

        # Verifica diagonal inferior izquierda a superior derecha
        for fila in range(len(tablero) - 3):
            for col in range(len(tablero[0]) - 3):
                if np.all(np.diag(tablero[fila:fila+4, col:col+4]) == jugador):
                    return True

        # Verifica diagonal superior izquierda a inferior derecha
        for fila in range(3, len(tablero)):
            for col in range(len(tablero[0]) - 3):
                if np.all(np.diag(tablero[fila-3:fila+1, col:col+4][::-1]) == jugador):
                    return True



    return False

def minimax(tablero, profundidad, alfa, beta, maximizando_jugador):
    if profundidad == 0 or es_terminal(tablero):
        return evaluar_estado(tablero, 1)

    posibles_movimientos = obtener_movimientos(tablero)

    if maximizando_jugador:
        max_eval = float('-inf')
        for movimiento in posibles_movimientos:
            nuevo_tablero = np.copy(tablero)
            nuevo_tablero = realizar_movimiento(nuevo_tablero, movimiento, 1)
            eval = minimax(nuevo_tablero, profundidad - 1, alfa, beta, False)
            max_eval = max(max_eval, eval)
            alfa = max(alfa, eval)
            if beta <= alfa:
                break
        return max_eval
    else:
        min_eval = float('inf')
        for movimiento in posibles_movimientos:
            nuevo_tablero = np.copy(tablero)
            nuevo_tablero = realizar_movimiento(nuevo_tablero, movimiento, -1)
            eval = minimax(nuevo_tablero, profundidad - 1, alfa, beta, True)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alfa:
                break
        return min_eval

def encontrar_mejor_movimiento(tablero, profundidad):
    posibles_movimientos = obtener_movimientos(tablero)
    mejor_eval = float('-inf')
    mejor_movimiento = None
    alfa = float('-inf')
    beta = float('inf')

    for movimiento in posibles_movimientos:
        nuevo_tablero = np.copy(tablero)
        nuevo_tablero = realizar_movimiento(nuevo_tablero, movimiento, 1)
        eval = minimax(nuevo_tablero, profundidad - 1, alfa, beta, False)

        if eval > mejor_eval:
            mejor_eval = eval
            mejor_movimiento = movimiento

        alfa = max(alfa, eval)

    return mejor_movimiento

def jugar_contra_pc():
    filas, columnas = 6, 7
    tablero = inicializar_tablero(filas, columnas)

    while not es_terminal(tablero):
        imprimir_tablero(tablero)
        columna_usuario = int(input("Ingresa tu movimiento (columna del 0 al 6): "))
        if es_movimiento_valido(tablero, columna_usuario):
            tablero = realizar_movimiento(tablero, columna_usuario, -1)
        else:
            print("Movimiento no válido. Inténtalo de nuevo.")
            continue

        if es_terminal(tablero):
            break

        imprimir_tablero(tablero)
        print("Turno de la computadora...")
        columna_pc = encontrar_mejor_movimiento(tablero, profundidad=3)
        print(f"La computadora juega en la columna {columna_pc}")
        tablero = realizar_movimiento(tablero, columna_pc, 1)

    imprimir_tablero(tablero)
    ganador = evaluar_estado(tablero, 1)
    if ganador < 0:
        print("¡Ganaste!")
    elif ganador > 0:
        print("¡enpate")
    else:
        print("¡La computadora gana!")


jugar_contra_pc()
