def suma_n_numeros(*args: float) -> float:
    total = 0
    for numero in args:
        total += numero
    return total


def suma_n_enteros(*args: int) -> int:
    total = 0
    for numero in args:
        try:
            if numero == int(numero):
                total += numero
            else:
                print(f"El numero {numero} no es un entero. Será ignorado.")
        except ValueError:
            print("El número debe ser un número entero.")
    return total


def suma_dos_o_mas_numeros(n1: float, n2: float, *args: float) -> float:
    total = n1 + n2
    for numero in args:
        total += numero
    return total


print(suma_n_numeros(1, 2, 3))
print(suma_n_enteros(1, 2, 3.5, 6))
print(suma_dos_o_mas_numeros(10, 20, 3))
