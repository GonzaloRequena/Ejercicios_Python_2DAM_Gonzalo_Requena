def suma(x, y) -> float:
    return x + y

def multiplicacion(x, y) -> float:
    return x * y

def division(x, y) -> float:
    return x / y

def resta(x, y) -> float:
    return x - y



while True:
    print("---CALCULADORA---")
    print("1. SUMAR")
    print("2. MULTIPLICAR")
    print("3. DIVIDIR")
    print("4. RESTAR")
    print("5. SALIR")

    opcion = input("\nElige una opción: 1/2/3/4/Salir: ").strip().lower()
    if opcion == "salir":
        print("Saliendo...")
        break

    while True:
        try:
            n1 = int(input("Introduce un número entero: "))
            n2 = int(input("Introduce un número entero: "))
        except ValueError:
            print("Debes introducir un número entero.")
        else:
            match opcion:
                case "1":
                    print(f"SUMA: {suma(n1, n2):.2f}\n")
                    break
                case "2":
                    print(f"MULTIPLICACIÓN: {multiplicacion(n1, n2):.2f}\n")
                    break
                case "3":
                    if n2 != 0:
                        print(f"DIVISIÓN: {division(n1, n2):.2f}\n")
                    else:
                        print("No se puede dividir por 0.\n")
                    break
                case "4":
                    print(f"RESTA: {resta(n1, n2):.2f}\n")
                    break
                case _:
                    print("Operación no válida.\n")
                    break

