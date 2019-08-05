""" Serie de Fibonacci - Métodos alternativos de generación
Cada nuevo término en la secuencia de Fibonacci es generado al sumar
los dos términos anteriores entre si.
Comenzando con 0 y 1, los primeros 10 términos serían:
0, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
Se analizan diversos modos de generación:
    a) Recursivo
    b) Recursivo con memoization
    c) for loop
    d) for loop alternativo

El programa solicita el número para el que se quiere generar la serie.
Luego calcula la serie por todos los métodos solicitados y mide el tiempo
de generación de cada uno.
Finalmente imprime opcionalmente la serie en pantalla.
No chequea errores en las entradas por teclado.
Nota: El método "a" empieza a tardar mucho tiempo ya con n > 30.
"""

import time
from functools import lru_cache


def fib(n):
    """ Calcula el n-esimo término  la serie de Fibonacci
    de forma recursiva.
    """
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


@lru_cache(maxsize=None)
def fib_lru(n):
    """ Calcula el n-esimo término  la serie de Fibonacci
    de forma recursiva con memoization.
    """
    if n < 2:
        return n
    return fib_lru(n - 1) + fib_lru(n - 2)


n_terms = int(input("Número de términos de la serie de Fibonacci a generar: "))
print(
    """Métodos de generación de la serie:
    1) Recursivo
    2) Recursivo con memoization
    3) for loop
    4) for loop alternativo"""
)
mode = int(input("Elija el método: "))

start = time.time()
if mode == 1:
    print("Calculando por el método recursivo...")
    fib_series = [fib(n) for n in range(n_terms)]

elif mode == 2:
    print("Calculando por el método recursivo con memoization...")
    fib_series = [fib_lru(n) for n in range(n_terms)]

elif mode == 3:
    print("Calculando con un 'for loop'...")
    fib_series = []
    a, b = 0, 1
    for n in range(n_terms):
        fib_series.append(a)
        # Calculo el nuevo término y reasigno las variables
        a, b = b, a + b

elif mode == 4:
    print("Calculando con un 'for loop' alternativo...")
    fib_series = [0, 1]
    for n in range(2, n_terms):
        fib_series.append(fib_series[-1] + fib_series[-2])

# Calculo el tiempo insumido en generar la serie y lo imprimo
end = time.time()
print(f"Tiempo insumido: {end - start}")

# Opcionalmente imprimo la serie generada
to_print = input("Desea imprimir la serie generada (S/N): ").upper()
if to_print == "S":
    print(fib_series)
