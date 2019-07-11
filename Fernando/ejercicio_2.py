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

# Inicializo los 2 primeros términos y la suma
a, b, suma = 1, 2, 0

# Empiezo un lazo que terminará al superar el valor límite
while a <= limite:
    if imprimir:
        # En vez de agregar \n al final, termino la línea con espacio
        print(a, end=" ")
    # Acumulo el valor del término actual
    suma += a
    # Calculo el nuevo término y reasigno las variables
    a, b = b, a + b

# Imprimo resultado formateado para separar los miles
print("\nLa suma es: {0:,d}".format(suma))
