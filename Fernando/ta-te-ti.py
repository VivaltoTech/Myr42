""" TA-TE-TI
Programa para jugar al TA-TE-TI contra la computadora
Ejercicio para usar TKinter y el algoritmo minimax
La computadora jugará con las X y el humano con las O.
Se sorteará al azar quien comienza en cada vuelta.
El humano debe hacer click con el mouse en la casilla vacía
donde desea poner su ficha en cada turno.
Luego de finalizada la partida, hacer click sobre el tablero
para iniciar otra partida.
"""

import random
import copy
from functools import partial

# Importo el módulo de Tkinter y los TKinter themed widgets
import tkinter as tk
from tkinter import ttk

# Declaro estas variables que serán globales e inicializadas dentro de una función
player_to_play, game_over = (None, None)


def pressed_button(row, column):
    """ Función invocada cada vez que se aprieta un botón del tablero.
    Si la casilla está vacía, procesa la movida del jugador humano.
    Luego, si la partida no terminó, hace la jugada la computadora.
    Si la partida ya había terminado, resetea el juego para comenzar de nuevo.
    Modifica las variables globales board y game_over.
    """
    global board, game_over

    if game_over:
        # Si la partida ya había terminado, reseteo el juego
        reset_game()
    elif board[row][column] == "":
        # Si la partida está en curso y el casillero está vacío, proceso la nueva jugada
        process_move(row, column)
        if not game_over:
            computer_plays()


def reset_game():
    """ Inicializa las variables globales para comenzar una partida nueva.
    Sortea también el turno inicial y, en caso de corresponder a
    la computadora, invoca la función para que realice su jugada.
    """
    global board, player_to_play, result, game_over

    # Limpio el resultado de la pantalla
    result.set("")

    # Limpio el tablero lógico (lo lleno con "")
    board = [["" for j in range(3)] for i in range(3)]

    # Actualizo el tablero en pantalla
    update_screen_board(board)

    # Inicializo flag para indicar si terminó la partida
    game_over = False

    # Elijo al azar quien va a empezar
    player_to_play = random.choice(("X", "O"))

    # Si el turno inicial es de la computadora (X), ésta realiza su jugada
    if player_to_play == "X":
        computer_plays()


def computer_plays():
    """ Elije la jugada de la computadora y luego invoca la función para
    actualizar el tablero y preparar el siguiente turno.
    Modifica la variable global board y usa game_mode.
    """
    global board, game_mode

    if game_mode.get() == "random":
        # Elijo una jugada al azar entre la lista de posibles jugadas
        row, column = random.choice(list_available_moves(board))
    else:
        # Utilizo el algoritmo minimax para elegir la mejor jugada
        row, column = make_minimax_move(board)
    # Proceso la movida seleccionada por la computadora
    process_move(row, column)


def update_screen_board(board):
    """ Actualiza el tablero en pantalla de acuerdo a los valores del
    tablero lógico pasado como argumento.
    Modifica la variable global screen_board.
    """
    global screen_board
    for row in range(3):
        for col in range(3):
            if screen_board[row][col].get() != board[row][col]:
                screen_board[row][col].set(board[row][col])


def update_screen_score(score):
    """ Actualiza el score en pantalla de acuerdo a los valores del score
    pasados como argumento.
    Modifica la variable global screen_score.
    """
    global screen_score
    # Copio el score para la computadora (X), el humano (O)
    # y los empates (T).
    for s in ["X", "O", "T"]:
        screen_score[s].set(score[s])


def list_available_moves(board):
    """ Dado un tablero como argumento, arma una lista de todas las próximas jugadas posibles.
    Devuelve una lista de tuplas con la fila y columna de cada jugada disponible.
    """
    return [(row, col) for col in range(3) for row in range(3) if board[row][col] == ""]


def make_minimax_move(board):
    """ Dado un tablero como argumento, devuelve una tupla con la fila y la columna de
    la mejor jugada disponible usando el algoritmo minimax.
    No hace optimizaciones como la eliminación de posiciones simétricas.
    """
    # Armo una lista con los pares de cada jugada disponible y su valor asociado
    move_value_pairs = [
        (move, calc_value(play_move(board, move, "X"), "O")) for move in list_available_moves(board)
    ]
    # Retorno la movida que corresponde al máximo valor
    return max(move_value_pairs, key=lambda item: item[1])[0]


def play_move(board, move, player):
    """ Realiza la movida recibida como argumento para el jugador elegido
    sobre una copia del tablero recibido.
    Retorna el nuevo tablero con la movida realizada. No modifica el tablero original.
    """
    # Realizo una copia especial del tablero para crear un nuevo tablero no  vinculado
    # al original, de modo de no modificar el tablero real al evaluar las nuevas movidas.
    new_board = copy.deepcopy(board)
    # Realizo la movida ssobre el nuevo tablero
    new_board[move[0]][move[1]] = player
    # Retorno el nuevo tablero
    return new_board


def get_board_signature(board):
    """ Convierte un tablero en una tupla que puede ser
    utilizada como key en un diccionario (como cached_values).
    """
    return tuple([y for x in board for y in x])


def calc_value(board, player):
    """ Calcula el valor de la posición para el tablero y el
    jugador pasados como argumentos.
    Devuelve 1 si gana la compuadora, 0 si es empate o -1 si
    gana el jugador humano.
    Actualiza variable global cached_values
    """
    global cached_values

    # Me fijo si la posición ya había sido calculada y para eso
    # primero convierto el tablero en una clave para buscar en el cache
    board_key = get_board_signature(board)
    if board_key in cached_values:
        # Ya estaba calculada y retorno ese valor
        return cached_values[board_key]

    # Verifico si terminó la partida y quien fue el ganador
    game_over, winner = check_win(board)

    if game_over:
        # Si la partida terminó, determino el valor de acuerdo al ganador
        value = MINIMAX_VALUES[winner]
    else:
        # Armo la lista de valores para cada jugada posible desde esta posición
        values = [
            calc_value(play_move(board, move, player), next_player(player))
            for move in list_available_moves(board)
        ]
        # El valor es el máximo de la lista si el jugador es la computadora
        # o el mínimo de la lista si es el turno del humano
        value = max(values) if player == "X" else min(values)

    # Guardo el nuevo valor en el cache de valores para uso futuro
    cached_values[board_key] = value

    return value


def process_move(row, column):
    """ Actualiza el tablero, llama a función para ver si hubo un ganador
    o si hubo empate y prepara el siguiente turno si no lo hubo.
    Si terminó la partida actualiza las variables globales result y score
    con el resultado.
    Devuelve True si hay más turnos y False si ya terminó la partida.
    Argumentos: fila y columna de la movida seleccionada.
    """
    global board, player_to_play, result, game_over, score

    # Actualizo la jugada en el tablero lógico
    board[row][column] = player_to_play

    # Actualizo también el tablero en pantalla
    update_screen_board(board)

    # Verifico si terminó el partido y si hubo un ganador
    game_over, winner = check_win(board)

    if game_over:
        # Se terminó la partida
        # Aumento el score del ganador
        score[winner] += 1
        # Actualizo el score en pantalla
        update_screen_score(score)
        # Anuncio el ganador
        result.set("Empate" if winner == "T" else "Ganó " + winner)
        return False
    else:
        # La partida continúa
        # Será el turno del siguiente jugador
        player_to_play = next_player(player_to_play)
        return True


def next_player(player):
    return "X" if player == "O" else "O"


def check_win(board):
    """ Función para verificar si hay un ganador.
    Retorna una tupla con True y el ganador si hay 3 "X" o 3 "O" en línea o
    o una tupla con True y "T" False si hay empate.
    Si no aún no finalizó la partida, retorna una tupla con False y "".
    Toma como parámetro el tablero a revisar.
    """

    # Reviso las 3 filas
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "":
            return (True, board[i][1])
    # Reviso las 3 columnas
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] != "":
            return (True, board[1][j])
    # Reviso las 2 diagonales
    if (board[0][0] == board[1][1] == board[2][2] != "") or (board[0][2] == board[1][1] == board[2][0] != ""):
        return (True, board[1][1])

    # No hay ganador. Vemos si se acabaron las movidas y es empate
    if len(list_available_moves(board)) == 0:
        # No hay más movidas. Es empate.
        return (True, "T")

    # No se dio ninguna condición por lo que retornamos False y ""
    return (False, "")


# Comienzo del programa principal

# Defino diccionario con los 3 valores posibles para el
# cálculo de las posiciones con el algoritmo minimax
MINIMAX_VALUES = {"X": 1, "T": 0, "O": -1}

# Creo un diccionario global para guardar el cache de los valores
# para cada tablero ya calculado
cached_values = {}

# Inicializo la ventana en la que dibujaremos el tablero
root = tk.Tk()
root.title("TA-TE-TI")
mainframe = ttk.Frame(root, padding="3")
mainframe.grid(column=0, row=0, sticky="NSEW")

# Creo el tablero lógico como una matriz de 3 x 3 inicializada con "" en cada celda
board = [["" for j in range(3)] for i in range(3)]

# Defino una matriz de 3 x 3 inicializada con cadenas vacías de tipo
# "tkinter.StringVar" para representar al tablero en pantalla y
# dibujo el tablero usando botones que apuntan a pressed_button con los
# argumentos preparados de su fila y columna
screen_board = [[tk.StringVar() for j in range(3)] for i in range(3)]

# Dibujo el tablero como una matriz de botones en la pantalla
for i in range(3):
    for j in range(3):
        # Creo el botón correspondiente a cada casillero
        ttk.Button(mainframe, textvariable=screen_board[i][j], command=partial(pressed_button, i, j)).grid(
            row=i, column=j + 1, sticky="NSEW"
        )

# Defino el lugar en la ventana para anunciar el resultado
result = tk.StringVar()
ttk.Label(mainframe, textvariable=result).grid(column=2, row=3, sticky="WE")

# Defino los radiobuttons para elegir el modo de juego
# entre "Inteligente" o "Al azar". El valor inicial es "Inteligente".
game_mode = tk.StringVar()
game_mode.set("intelligent")
ttk.Label(mainframe, text="Modo de Juego:").grid(row=4, column=0, columnspan=2, sticky="W")
ttk.Radiobutton(mainframe, text="Inteligente", variable=game_mode, value="intelligent").grid(
    row=5, column=0, columnspan=2, sticky="W"
)
ttk.Radiobutton(mainframe, text="Al azar", variable=game_mode, value="random").grid(
    row=6, column=0, columnspan=2, sticky="W"
)

# Incializo a 0 el score de ambos jugadores y el de los empates ("T")
score = {"X": 0, "O": 0, "T": 0}
# Defino las variables para mostrar el score en pantalla
screen_score = {"X": tk.StringVar(), "O": tk.StringVar(), "T": tk.StringVar()}
# Actualizo el score en pantalla con los valores de score
update_screen_score(score)
# Creo y posiciono las leyendas y valores de los scores en pantalla
ttk.Label(mainframe, text="Score:").grid(column=2, row=4, columnspan=2, sticky="E")
ttk.Label(mainframe, text="Computadora (X):").grid(column=2, row=5, columnspan=2, sticky="E")
ttk.Label(mainframe, text="Humano (O):").grid(column=2, row=6, columnspan=2, sticky="E")
ttk.Label(mainframe, text="Empates:").grid(column=2, row=7, columnspan=2, sticky="E")
ttk.Label(mainframe, textvariable=screen_score["X"], width=3).grid(column=4, row=5, sticky="W")
ttk.Label(mainframe, textvariable=screen_score["O"]).grid(column=4, row=6, sticky="W")
ttk.Label(mainframe, textvariable=screen_score["T"]).grid(column=4, row=7, sticky="W")

# Seteo las condiciones iniciales
reset_game()

# Comienzo el loop que está atento a los eventos en pantalla
root.mainloop()
