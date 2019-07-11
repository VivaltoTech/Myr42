"""EJERCICIO 1
Si listamos todos los números naturales menores a 10 que son múltiplos de 3 o 5,
obtenemos 3, 5, 6 y 9. La suma de esos múltiplos es 23.
Encontrar la de todos los múltiplos de 3 o 5 menores a 1000.
"""

suma = 0
for x in range(3, 1000):
    if x % 3 == 0 or x % 5 == 0:
        suma += x

# Imprimo resultado sin formatear
print("La suma es:", suma)
# Imprimo resultado formateado para separar los miles
print("La suma es: {0:,d}".format(suma))
