def printeaMenu():
    print("\nMenú:")
    print("1) Hacer otra operación con el resultado actual")
    print("2) Reiniciar calculadora")
    print("3) Ver historial")
    print("4) Salir")

def operar(operador, num1, num2):
    if operador == "/" and segundo_numero == 0:
        print("Error: división por cero no permitida.")

    if operador == "+":
        resultado = primer_numero + segundo_numero
    elif operador == "-":
        resultado = primer_numero - segundo_numero
    elif operador == "*":
        resultado = primer_numero * segundo_numero
    elif operador == "/":
        resultado = primer_numero / segundo_numero
    return resultado


print("Calculadora con historial")

# Inicializamos variables
historial = []
primer_numero = None

while True:
    if primer_numero is None:
        primer_numero = input("Ingrese el primer número: ")
        # Validar que sea número
        try:
            primer_numero = float(primer_numero)
        except:
            print("Número inválido, intente de nuevo.")
            primer_numero = None
            continue

    printeaMenu()

    opcion = input("Elija una opción: ")

    if opcion == "1":
        operador = input("Ingrese la operación (+, -, *, /): ")
        if operador not in ["+", "-", "*", "/"]:
            print("Operador inválido.")
            continue

        segundo_numero = input("Ingrese el segundo número: ")
        try:
            segundo_numero = float(segundo_numero)
        except:
            print("Número inválido.")
            continue


        resultado = operar(operador, primer_numero, segundo_numero);

        print(f"{primer_numero} {operador} {segundo_numero} = {resultado}")
        historial.append(f"{primer_numero} {operador} {segundo_numero} = {resultado}")
        primer_numero = resultado

    elif opcion == "2":
        primer_numero = None
        historial = []
        print("Calculadora reiniciada.")

    elif opcion == "3":
        if len(historial) == 0:
            print("No hay operaciones en el historial.")
        else:
            print("Historial de operaciones:")
            for operacion in historial:
                print(operacion)

    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente de nuevo.")



