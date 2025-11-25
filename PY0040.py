import math

radio = int(input("Introduzca un radio: "))

calculoRadio = (lambda rad : math.pi * (rad ** 2))
print(f"Área: {calculoRadio(radio):.2f}")