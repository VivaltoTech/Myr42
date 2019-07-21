import random

def tirada(n, dados):
    """ Para cada dado de la lista que tenga un 0, calcula un nuevo valor al azar
        entre 1 y 6. Luego devuelve la lista de dados."""

    for i in range(len(dados)):
        if dados[i] == 0:
            dados[i] = random.randint(1, 6)

    print(str(n) + "º tirada: " + str(dados[0:5]), end="")
    return dados


def reubicar(a_cambiar, dados):
    """ Por cada caracter de la cadena a_cambiar, pone a 0 el dado correspondiente.
        Luego devuelve la lista de dados."""
    for x in a_cambiar:
        dados[int(x)-1] = 0
    return dados


# Inicializo las variables
nro_tirada = 1
result = [0, 0, 0, 0, 0]

########################################################
# INICIA BUCLE: TIRA DIRECTAMENTE Y PREGUNTA SI CAMBIA #
########################################################

while nro_tirada < 4:

    result = tirada(nro_tirada, result)
    nro_tirada += 1

    if nro_tirada == 4:
        break

    cambiar = input(
        " --------------> Tirar de nuevo: [1,2,3,4,5] o [0] para terminar:>"
    )

    if cambiar == "0":
        break
    else:
        result = reubicar(cambiar, result)

print("\n   TIRADA: " + str(result[0:5]))
