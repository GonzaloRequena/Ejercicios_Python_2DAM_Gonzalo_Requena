# #PY0016
# for cont in range (21):
#     print(cont)
# print("\n")
# for cont in range (21):
#     if cont % 2 == 0:
#         print(cont)
# print("\n")
# for cont in range (-1, -21, -1):
#     if cont % 2 != 0:
#         print(cont)
import time

# #PY0017
# pares = range(0, 101, 2)
# suma = sum(pares)
# print(f"Los números pares sumados son: {list(pares)}")
# print(f"La suma de todos los números enteros pares del 0 al 100 es: {suma}")

# #PY0019
# flag = 0
# while flag == 0:
#     try:
#         num = int(input("Introduce un número impar: "))
#     except ValueError:
#         print("Debes introducir un número impar.")
#     else:
#         if num % 2 == 0:
#             print("El numero no es impar.")
#         else:
#             print("El numero es impar.")
#             flag += 1

# #PY0014
# mediaPonderada = 0
# try:
#     n1 = float(input("Introduce un número decimal: "))
#     n2 = float(input("Introduce un número decimal: "))
#     n3 = float(input("Introduce un número decimal: "))
# except ValueError:
#     print("Debe ser un número decimal.")
# else:
#     mediaPonderada = n1 * 0.15 + n2 * 0.35 + n3 * 0.5
#     print(f"La media ponderada es: {mediaPonderada:.2f}")

# #PY0020
# while True:
#     print("---CALCULADORA---")
#     print("1. SUMAR")
#     print("2. MULTIPLICAR")
#     print("3. DIVIDIR")
#     print("4. RESTAR")
#     print("5. SALIR")
#
#     opcion = input("\nElige una opción: 1/2/3/4/Salir: ").strip().lower()
#     if opcion == "salir":
#         print("Saliendo...")
#         break
#
#     while True:
#         try:
#             n1 = int(input("Introduce un número entero: "))
#             n2 = int(input("Introduce un número entero: "))
#         except ValueError:
#             print("Debes introducir un número entero.")
#         else:
#             match opcion:
#                 case "1":
#                     resultado = n1 + n2
#                     print(f"SUMA: {n1} + {n2} = {resultado:.2f}\n")
#                     break
#                 case "2":
#                     resultado = n1 * n2
#                     print(f"MULTIPLICACIÓN: {n1} x {n2} = {resultado:.2f}\n")
#                     break
#                 case "3":
#                     if n2 != 0:
#                         resultado = n1 / n2
#                         print(f"DIVISIÓN: {n1} / {n2} = {resultado:.2f}\n")
#                     else:
#                         print("No se puede dividir por 0.\n")
#                     break
#                 case "4":
#                     resultado = n1 - n2
#                     print(f"RESTA: {n1} - {n2} = {resultado:.2f}\n")
#                     break
#                 case _:
#                     print("Operación no válida.\n")
#                     break

# #PY0018
# registro = "zeréP nauJ,01"
# cadena = registro [::-1]
# nota = cadena.split(",") [0]
# nombre = cadena.split(",") [1]
# print(f"{nombre} ha sacado una nota de {nota}")

# #PY0043
# cadena = input("Introduce una cadena de texto: ").lower().replace(" ", "")
# letras = []
# ocurrencias = []
#
# for letra in cadena:
#     if letra not in letras:
#         letras.append(letra)
#         ocurrencias.append(1)
#     else:
#         ocurrencias[letras.index(letra)] += 1
#
# for letra in range(len(letras)):
#     print(letras[letra], ":", ocurrencias[letra])

# #PY0013
# cadena = input("Introduce una cadena de texto: ")
# car1 = input("Introduce el caracter que quieres cambiar: \t")
# car2 = input("Introduce el nuevo caracter: \t")
# if len(car1) > 1 or len(car2) > 1:
#     print("Sólo puedes introducir un caracter.")
#     time.sleep(3)
# else:
#     print(cadena.replace(car1, car2))
