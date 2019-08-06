"""
Tenemos 12 bolitas, y una de ellas pesa diferente (no se sabe si mas o si menos).
Y tenemos una balanza de platillos, a la que sólo podemos usar 3 veces.
Hay que averiguar qué bolita es, y por puntos extras, si pesa más o menos.

Voy a usar bolas numeradas para tratar de explicar mi razonamiento y, de paso, ir verificando si es válido.
Tenemos bolas de la 1 a la 12. Asumamos que la 6 es más pesada que el resto. El razonamiento sería similar si la bola fuera otra o fuera más liviana.
Cada letra corresponde a un caso posible y 1), 2) y 3) corresponden al número de pesada.
"""


def p(bolas_a_pesar):
    """ Calcula el peso de todas las bolas pasadas como argumento separadas por "-".
    """
    lista_bolas = bolas_a_pesar.split("-")
    p = 0
    for i in lista_bolas:
        p += bolas[int(i)]
    return p


def genero_bolas(nro_bolas, bola_distinta, mas_pesada):
    """ Genera una lista de n bolas de igual peso salvo la bola
    distinta que puede ser más pesada (True) o menos pesada (False).
    """
    peso_normal = 2
    peso_distinto = (peso_normal + 1) if mas_pesada else (peso_normal - 1)
    bolas = [peso_normal if n != bola_distinta else peso_distinto for n in range(nro_bolas)]
    return bolas


def analizo_bolas(bolas):
    """ Dado un conjunto de 12 bolas, 11 de ellas iguales y una más o menos pesada
    que las demás, devuelve el número de la bola distinta (0 a 11), si es más pesada
    (True o Flase) y el total de pesadas necesarias para encontrar la respuesta.
    """

    if p("0-1-2-3") == p("4-5-6-7"):
        if p("0-1-2") == p("8-9-10"):  # la bola distinta es la 11
            bola_x = 11
            if p("11") > p("0"):
                mas_pesada = True
            else:
                mas_pesada = False
        elif p("0-1-2") > p("8-9-10"):  # la bola es más liviana y está entre 8-9-10
            mas_pesada = False
            if p("8") == p("9"):
                bola_x = 10
            elif p("8") > p("9"):
                bola_x = 9
            else:
                bola_x = 8
        else:  # la bola es más pesada y está entre 8-9-10
            mas_pesada = True
            if p("8") == p("9"):
                bola_x = 10
            elif p("8") > p("9"):
                bola_x = 8
            else:
                bola_x = 9

    elif p("0-1-2-3") > p("4-5-6-7"):
        if p("0-1-2-4") > p("3-8-9-10"):  # la bola es más pesada y está entre 0-1-2
            mas_pesada = True
            if p("0") == p("1"):
                bola_x = 2
            elif p("0") > p("1"):
                bola_x = 0
            else:
                bola_x = 1
        elif p("0-1-2-4") == p("3-8-9-10"):  # La bola es más liviana y está entre 5-6-7
            mas_pesada = False
            if p("5") == p("6"):
                bola_x = 7
            elif p("5") > p("6"):
                bola_x = 6
            else:
                bola_x = 5
        else:  # p("0-1-2-4") < p("3-8-9-10"):    # La bola es la 3 y es más pesada o la 4 y es más liviana
            if p("3") > p("0"):
                bola_x = 3
                mas_pesada = True
            else:
                bola_x = 4
                mas_pesada = False

    else:  # p("0-1-2-3") < p("4-5-6-7")
        if p("0-1-2-4") < p("3-9-10-11"):  # la bola es más liviana y está entre 0-1-2
            mas_pesada = False
            if p("0") == p("1"):
                bola_x = 2
            elif p("0") > p("1"):
                bola_x = 1
            else:
                bola_x = 0
        elif p("0-1-2-4") == p("3-9-10-11"):  # La bola es más pesada y está entre 5-6-7
            mas_pesada = True
            if p("5") == p("6"):
                bola_x = 7
            elif p("5") > p("6"):
                bola_x = 5
            else:
                bola_x = 6
        else:  # p("0-1-2-4") > p("3-9-10-11"):    # La bola es la 3 y es más liviana o la 4 y es más pesada
            if p("4") > p("0"):
                bola_x = 4
                mas_pesada = True
            else:
                bola_x = 3
                mas_pesada = False

    return bola_x, mas_pesada


# Pruebo todas las combinaciones para verificar la lógica
for i in range(12):
    for m in (False, True):
        bolas = genero_bolas(12, i, m)
        bola_x, mas_pesada = analizo_bolas(bolas)
        if bola_x != i or mas_pesada != m:
            print(f"Mal resuelto!!! {i} {m} {bola_x} {mas_pesada}\n")


# Parte interactiva
# Pregunto qué bola será distinta
bola_distinta = int(input("Ingrese el nro de bola que quiere que sea distinta (0 a 11): "))

# Pregunto si debe ser más o menos pesada
diferencia = input("Ingrese + o - para que la bola sea más pesada o más liviana: ")
if diferencia == "+":
    mas_pesada = True
else:
    mas_pesada = False

bolas = genero_bolas(12, bola_distinta, mas_pesada)

bola_x, mas_pesada = analizo_bolas(bolas)

# Imprimo el resultado
print(f"La bola distinta es la {bola_x}.")
if mas_pesada == True:
    print("La bola es más pesada.")
else:
    print("La bola es más liviana.")
