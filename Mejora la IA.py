# esta versión es la base para trabajar en la evaluación III


def crear_tablero():
    tablero = [[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]
    return tablero


def imprimir_tablero(tablero):
        print(f"{tablero[0][0]}|{tablero[0][1]}|{tablero[0][2]}")
        print("-----")
        print(f"{tablero[1][0]}|{tablero[1][1]}|{tablero[1][2]}")
        print("-----")
        print(f"{tablero[2][0]}|{tablero[2][1]}|{tablero[2][2]}")



def movimiento_jugador(tablero, jugador):
    while True:
        try:
            fila = int(input("Elige fila (0, 1, 2): "))
            columna = int(input("Elige columna (0, 1, 2): "))
            if 0 <= fila <= 2 and 0 <= columna <= 2:
                if tablero[fila][columna] == " ":
                    tablero[fila][columna] = jugador
                    break
                else:
                    print("¡Casilla ocupada!")
            else:
                print("¡Entrada inválida! Por favor elige números entre 0 y 2.")
        except ValueError:
            print("¡Entrada inválida! Por favor ingresa números.")


def hay_ganador(tablero):
    # Verificar filas y columnas
    for i in range(3):
        if tablero[i][0] == tablero[i][1] == tablero[i][2] != " ":
            return True
        if tablero[0][i] == tablero[1][i] == tablero[2][i] != " ":
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != " ":
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != " ":
        return True

    return False


def tablero_lleno(tablero):
    for fila in tablero:
        if " " in fila:
            return False
    return True


import random

def movimiento_ia(tablero):
    # Estrategia de la IA:
    # 1. Verificar si la IA puede ganar en el próximo movimiento.
    # 2. Verificar si el jugador puede ganar en el próximo movimiento y bloquearlo.
    # 3. Si no hay jugadas ganadoras o de bloqueo, realizar un movimiento aleatorio.

    # Símbolo de la IA y del jugador
    ia_simbolo = "O"
    jugador_simbolo = "X"

    # 1. Verificar si la IA puede ganar
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = ia_simbolo
                if hay_ganador(tablero):
                    return
                tablero[i][j] = " " # Deshacer el movimiento

    # 2. Verificar si el jugador puede ganar y bloquear
    for i in range(3):
        for j in range(3):
            if tablero[i][j] == " ":
                tablero[i][j] = jugador_simbolo
                if hay_ganador(tablero):
                    tablero[i][j] = ia_simbolo # Bloquear la jugada del jugador
                    return
                tablero[i][j] = " " # Deshacer el movimiento

    # 3. Movimiento aleatorio si no hay jugadas ganadoras o de bloqueo
    casillas_vacias = [(i, j) for i in range(3) for j in range(3) if tablero[i][j] == " "]
    if casillas_vacias:
        fila, columna = random.choice(casillas_vacias)
        tablero[fila][columna] = ia_simbolo


def juego_completo():
    victorias_x = 0
    victorias_o = 0

    while True:
        tablero = crear_tablero()
        jugador_actual = "X"

        while True:
            imprimir_tablero(tablero)
            print(f"Turno de {jugador_actual}")

            if jugador_actual == "X":
                movimiento_jugador(tablero, jugador_actual)
            else:
                movimiento_ia(tablero)


            if hay_ganador(tablero):
                imprimir_tablero(tablero) # Imprimir el tablero final para ver la jugada ganadora
                print(f"¡{jugador_actual} ha ganado!")
                if jugador_actual == "X":
                    victorias_x += 1
                else:
                    victorias_o += 1
                break

            if tablero_lleno(tablero):
                imprimir_tablero(tablero) # Imprimir el tablero final en caso de empate
                print("¡Empate!")
                break

            if(jugador_actual=="O"):
                jugador_actual="X"
            else:
                jugador_actual = "O"
        
        print(f"Victorias - X: {victorias_x}, O: {victorias_o}")

        jugar_de_nuevo = input("¿Quieres jugar de nuevo? (s/n): ")
        if jugar_de_nuevo.lower() != 's':
            break


#tablero = crear_tablero()
#imprimir_tablero(tablero)
#movimiento_jugador(tablero)
#imprimir_tablero(tablero)

juego_completo()