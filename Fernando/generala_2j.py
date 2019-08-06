""" Ejercicio de Generala de 2 jugadores

El programa debe preguntar el nombre del jugador 1, luego hacerle hacer
una tirada completa. Luego debe preguntar el nombre del jugador 2, y hacerle
hacer una tirada completa.
Luego el programa imprimirá el nombre de cada jugador con la disposición
final de sus datos, para evaluar quién hizo mas puntos.

En el juego de la generala uno tira sus 5 dados al mismo tiempo, pero tiene
tres tiradas (porque hay que formar combinaciones para ganar).
Entonces, en la segunda tirada, uno puede elegir volver a tirar una cantidad
cualquiera de dados, y en la tercera lo mismo.
Por ejemplo, si nos salió 1,3,1,4,2 y buscáramos tener todos los dados iguales,
podríamos elegir volver a tirar el 3, el 4 y el 2 (dejando los 1) a ver si nos sale un 1.
Tiramos de nuevo, y nos queda 1, 5, 1, 1, 4, y tenemos una ronda mas, donde elegimos
tirar el 5 y el 4 (es decir, el segundo y el 5to dado) a ver si nos salen mas 1s
(los que ya salieron los dejamos)
Se requiere que el programa simule una tirada completa de generala, es decir que luego
de la primer tirada nos deje elegir volver a tirar los dados hasta dos rondas mas.
Tener en cuenta que uno podría estar satisfecho en cualquier punto, y no querer volver
a tirar.
"""
import random


def tirada_completa():
    """ Función para realizar una tirada de dados completa para 1 jugador.
    Retorna la lista con los dados de la tirada final.
    """
    dados = [0, 0, 0, 0, 0]
    tirar = "12345"
    nro_tirada = 1
    while tirar != "":
        for c in tirar:
            n = int(c) - 1
            if 0 <= n <= 4:
                dados[n] = random.randint(1, 6)
        print(f"Tirada {nro_tirada}: {dados}")
        nro_tirada += 1
        if nro_tirada > 3:
            return dados
        tirar = input(
            "Ingrese la posición (1 a 5) de los dados que quiere volver a tirar: "
        ).strip()
    return dados


def calc_puntaje(dados):
    """Función para calcular el puntaje de una tirada de 5 dados"""

    # Ordeno los dados de menor a mayor (lo nocesito para chequear la escalera)
    dados.sort()

    # Inicializo los arrays para las sumas y las cuentas
    sumas = [0, 0, 0, 0, 0, 0]
    cuentas = [0, 0, 0, 0, 0, 0]

    # Por cada número, cuento los dados
    for dado in dados:
        sumas[dado - 1] += dado
        cuentas[dado - 1] += 1

    # Me fijo si se formó un juego y asigno los puntos correspondientes
    if 5 in cuentas:
        puntos = 50  # Generala
    elif 4 in cuentas:
        puntos = 40  # Poker
    elif 3 in cuentas and 2 in cuentas:
        puntos = 30  # Full
    elif (
        dados == [1, 2, 3, 4, 5] or dados == [2, 3, 4, 5, 6] or dados == [1, 3, 4, 5, 6]
    ):
        puntos = 20  # Escalera
    else:
        puntos = 0

    # Retorno el máximo entre los puntos y las sumas de los números
    return max(puntos, max(sumas))


print("Juego de la Generala")

# Averiguo el número de jugadores
nro_jug = 0
while nro_jug <= 0:
    entrada = input("Cuántos jugadores van a jugar: ")
    try:
        nro_jug = int(entrada)
    except:
        print("Valor inválido")

# Obtengo el nombre de cada jugador
nombres = []
for i in range(nro_jug):
    nombre = input(f"Ingrese Nombre del Jugador {i+1}: ")
    nombres.append(nombre)

# Hago una tirada completa por cada jugador
dados_finales = []
for i in range(nro_jug):
    print(f"\nTurno de {nombres[i]}")
    dados_finales.append(tirada_completa())

# Calculo e imprimo el puntaje de cada jugador para esta tirada completa
puntajes = []
print()
for i in range(nro_jug):
    puntajes.append(calc_puntaje(dados_finales[i]))
    print(f"Puntaje de {nombres[i]}: {puntajes[i]}")
print()

# Averiguo el puntaje máximo y el número de ganadores
nro_ganadores = 0
maximo = max(puntajes)
for i in range(nro_jug):
    if puntajes[i] == maximo:
        nro_ganadores += 1

# Imprimo el encabezado correspondiente de acuerdo al número de ganadores
if nro_ganadores == 1:
    print("El ganador es: ")
else:
    print("Los ganadores son: ")
# Vuelvo a barrer la lista para imprimir los nombres de los ganadores
for i in range(nro_jug):
    if puntajes[i] == maximo:
        print(nombres[i])
print()
