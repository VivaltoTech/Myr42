# Calculadora simple V1

print("Calculadora Simple V1 (para salir ingrese 'q' como operador)\n")

while True:
    input1 = input("Ingrese 1er número: ")
    input2 = input("Ingrese 2do número: ")
    operador = input("Ingrese operador (+, -, *, /, //, %, **, q): ").strip().lower()

    # Verifico la condición de salida
    # Lo hago acá para no tener que chequear los números si la intención es terminar
    if operador == "q":
        # Salir de la calculadora
        break

    # Convertir cadenas de entrada a números y capturar si da un error
    try:
        num1 = float(input1)
        num2 = float(input2)
    except ValueError:
        print("Alguno de los números ingresados es inválido\n")
        continue

    # Procesar el operador y realizar el cálculo
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("Error: No se puede dividir por 0\n")
            continue
        resultado = num1 / num2
    elif operador == "//":
        if num2 == 0:
            print("Error: No se puede dividir por 0\n")
            continue
        resultado = num1 // num2
    elif operador == "%":
        if num2 == 0:
            print("Error: No se puede dividir por 0\n")
            continue
        resultado = num1 % num2
    elif operador == "**":
        resultado = num1 ** num2
    else:   # No se reconoció al operador
        print("Operador inválido\n")
        continue

    # Imprimir el resultado
    print("El resultado es: ", resultado, "\n")
