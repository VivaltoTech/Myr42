"""EJERCICIO 2
Cada nuevo término en la secuencia de Fibonacci es generado al sumar
los dos términos anteriores entre si.
Comenzando con 1 y 2, los primeros 10 términos serían:
1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
Considerando los términos en la secuencia de Fibonacci cuyo valor no excede
los cuatro millones, encontrar la suma de todos los términos pares.
"""

# Valor que no debe ser excedido
limite = 4000000
# Variable para controlar si se quieren imprimir o no los términos de la serie
imprimir = True

# Inicializo los 2 primeros términos
a = 1
b = 2
# Inicializo la suma con los 2 primeros términos
suma = a + b

# Imprimo los 2 primeros términos solo si está habilitado
if imprimir:
    # Uso ", " para separar los términos y para terminar la línea
    print(a, b, sep = ", ", end = ", ")

# Empiezo un lazo que sólo terminará al superar el valor límite
while True:
    # Calculo el nuevo término y reasigno las variables
    # Esta asignación con tuplas elimina el uso de una variable intermedia
    a, b = b, a + b
    # Me fijo si superé o no el límite
    if b <= limite:
        # Imprimo el nuevo término solo si está habilitado
        if imprimir:
            # En vez de agregar \n al final, termino la línea con coma y espacio
            print(b, end=", ")
        # Acumulo el valor del nuevo término
        suma += b
    else:
        # Superé el valor límite
        if imprimir:
            # Imprimo \n al final para imprimir el resultado en otra línea
            print("")
        # Termino el lazo
        break

# Imprimo el resultado sin formatear
# print("La suma es:", suma)
# Imprimo resultado formateado para separar los miles
print("La suma es: {0:,d}".format(suma))
