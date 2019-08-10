""" Ejercicio de Pokerala Completa de N jugadores

El nombre Pokerala viene de mezclar Poker y Generala.

El ganador se decide según la siguiente tabla (va de mayor valor a menor valor)
- Generala: 5 dados iguales (lo que mas vale)
- Escalera: 5 dados en progresión (del 1 al 5 o del 2 al 6)
- Poker: 4 dados iguales
- Full: 3 dados iguales y 2 iguales
- Trio: 3 dados iguales
- Doble Par: 2 dados iguales y 2 iguales
- Par: 2 dados iguales
- Nada: sumatoria de puntos
En caso de que los dos jugadores tengan la misma categoria gana el que tenga el número mas alto.
Por ejemplo, si los dos tienen un par, gana el que tenga el par mas alto: 5,5,3,2,1 le gana a
4,4,6,5,3 porque el par de 5s le gana al par de 4s.
En caso de que empaten en la categoria, se considera la sumatoria total de puntos para
determinar ganador (ej: 5,5,4,3,2 le gana a 5,5,3,2,1, porque aunque los dos tienen par de 5,
el primero desempata con el resto de sus dados).
En caso de Full, gana el que tiene el triple más alto, y si empatan, el doble más alto.
En caso de doble par, gana el que tiene el doble par más alto. En caso de empate, el
segundo par más alto, en caso de empate el dado suelto más alto.
En caso de escalera, la escalera que empieza en 2 vale más que la que empieza en 1.
Si los dos sacaron "nada", gana el que tiene más sumatoria de puntos.

El programa pregunta por el número de jugadores y por el nombre de cada uno de ellos.
Luego hace que cada uno realice una tirada completa.
Luego el programa imprimirá el nombre de cada jugador con la disposición
final de sus datos, y evaluará quién hizo más puntos y resultó ganador.

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
        tirar = input("Ingrese la posición (1 a 5) de los dados que quiere volver a tirar: ").strip()
    return dados


def calc_puntaje(dados):
    """Calcula el puntaje de una tirada de 5 dados de Pokerala.
    Recibe una lista con 5 dados y devuelve el puntaje de la tirada.
    """

    """ Como el puntaje se puede definir a voluntad para facilitar la determinación
    del ganador, se usará el siguiente esquema:
    Suma = Suma de los dados que no formaron juego
    Par =       10.000 + Nro. Par x 1.000 + Suma de los dados sueltos
    Doble Par = 20.000 + Nro. Par alto x 1.000 + Nro. Par bajo x 100 + dado suelto
    Trío =      30.000 + Nro. Trío x 1.000 + Suma de los dados sueltos
    Full =      40.000 + Nro. Trío x 1.000 + Nro. Par x 100
    Póker =     50.000 + Nro. Póker x 1.000 + dado suelto
    Escalera =  60.000 + 1.000 si empieza en 2
    Generala =  70.000 + Nro. Generala x 1.000
    """
    # Ordeno los dados de menor a mayor (lo necesito para chequear la escalera
    # pero también lo aprovecho para hallar el par bajo y el par alto en el par doble)
    dados.sort()

    # Inicializo el arrays para las cuentas de cada número (1 al 6)
    cuentas = [0, 0, 0, 0, 0, 0]

    # Por cada número del 1 al 6, cuento la cantidad de dados con ese número
    for dado in dados:
        cuentas[dado - 1] += 1

    # Calculo la suma de los dados cuyo número salió solo una vez
    suma_suelta = suma_dados_sueltos(cuentas)

    # Me fijo si se formó un juego y asigno los puntos correspondientes
    if 5 in cuentas:  # Generala
        puntos = 70000 + dados[0] * 1000
    elif dados == [1, 2, 3, 4, 5]:  # Escalera 1
        puntos = 60000
    elif dados == [2, 3, 4, 5, 6]:  # Escalera 2
        puntos = 60000 + 1000
    elif 4 in cuentas:  # Poker
        puntos = 50000 + (cuentas.index(4) + 1) * 1000 + suma_suelta
    elif 3 in cuentas and 2 in cuentas:  # Full
        puntos = 40000 + (cuentas.index(3) + 1) * 1000 + (cuentas.index(2) + 1) * 100
    elif 3 in cuentas:  # Trío
        puntos = 30000 + (cuentas.index(3) + 1) * 1000 + suma_suelta
    elif cuentas.count(2) == 2:  # Par Doble
        par_bajo = cuentas.index(2) + 1
        par_alto = cuentas.index(2, par_bajo) + 1
        puntos = 20000 + par_alto * 1000 + par_bajo * 100 + suma_suelta
    elif 2 in cuentas:  # Par
        puntos = 10000 + (cuentas.index(2) + 1) * 1000 + suma_suelta
    else:  # Sin juego
        puntos = suma_suelta

    # Retorno los puntos
    return puntos


def suma_dados_sueltos(cuenta_dados):
    """Devuelve la suma de los dados que solo están una vez en la cuenta de dados.
    """
    suma = 0
    for n, cant in enumerate(cuenta_dados, 1):
        suma += n if cant == 1 else 0
    return suma


def ganador(lista_tiradas):
    """Calcula el ganador o los ganadores de una lista de tirada (cada una de 5 dados)
    de Pokerala.
    Recibe una lista con las tiradas y devuelve una lista con la posición de la tirada o
    tiradas ganadoras.
    """
    # Armo lista con los puntajes de cada tirada
    puntajes = [calc_puntaje(tirada) for tirada in lista_tiradas]
    # Hallo el máximo puntaje
    maximo = max(puntajes)
    # Armo la lista de los ganadores con los que obtuvieron el mayor puntaje
    ganadores = [x for x, puntaje in enumerate(puntajes) if puntaje == maximo]
    return ganadores


# Comienzo del programa principal
if __name__ == "__main__":
    # Pequeña lista de prueba para probar la función de calculo de puntaje
    # lista_prueba = [[1,1,1,1,1],[2,2,2,2,2],[1,2,3,4,5],[1,2,1,1,1],[3,1,3,3,1],[1,1,2,4,4],[6,1,6,6,5],[5,4,4,5,4],[3,6,3,3,3],[4,3,1,5,5]]
    # for i in lista_prueba:
    #     print(i, calc_puntaje(i))
    # exit()

    print("Juego de la Pokerala")

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

    # Imprimo el encabezado correspondiente de acuerdo al número de ganadores
    ganadores = ganador(dados_finales)
    if len(ganadores) == 1:
        print("\nEl ganador es: ")
    else:
        print("\nLos ganadores son: ")
    # Vuelvo a barrer la lista para imprimir los nombres de los ganadores
    for i in ganadores:
        print(nombres[i])
    print()
