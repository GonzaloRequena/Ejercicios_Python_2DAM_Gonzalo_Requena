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

# #PY0001
# menu = ["sopa", "pisto", "tarta"]
# for i in range(0,len(menu)):
#     print(f"{i+1}. {menu[i].capitalize()}")

# #PY0002
# precios = [2, 5.95, 3.40, 8.4]
# preciosDescuento = []
# for i in range(0, len(precios)):
#     if i % 2 == 0:
#         preciosDescuento.append(precios[i] * 0.9)
#     else:
#         preciosDescuento.append(precios[i] * 0.8)
#     print(f"indice_lista = {i}, precio_antes = {precios[i]:.2f}, precio_depués = {preciosDescuento[i]:.2f}")

# #PY0015
# matriz = [[1, 1, 1, 1], [2, 2, 2, 2], [3, 3, 3, 3], [4, 4, 4, 4]]
# for fila in matriz:
#     fila[3] = sum(fila[:3:])
# print(f"Matriz = {matriz}")

# #PY0003
# asistentes = []
# while True:
#     asistente = input("Añade un asistente a la lista: ").capitalize()
#     asistentes.append(asistente)
#     if asistente == "fin".capitalize():
#         asistentes.remove("fin".capitalize())
#         break
#
# miembro = input("Indica un asistente para buscarlo en la lista: ").capitalize()
# print(f"El asistente {miembro} aparece {asistentes.count(miembro)} veces.")
# print(f"La primera vez que aparece {miembro} en la lista es en la posición {asistentes.index(miembro)}.")
# asistentes.remove(miembro)
# vip = input("Indica un asistente VIP para introducirlo en la lista: ").capitalize()
# asistentes.insert(0, vip)
# print(f"Lista de asistentes: {asistentes}")

# #PY0004
# menu = ["Ensalada", "Sopa", "Pasta"]
# menu_hoy = menu.copy()
# menu_hoy.extend(["Pescado", "Postre"])
# menu_hoy.pop(len(menu_hoy) -1)
# menu_hoy.remove("Sopa")
# menu_hoy.pop(0)
# menu_hoy.reverse()
# print(f"Menú de hoy: {menu_hoy}")
# menu.clear()
# print(f"\nMenú base: {menu}")
# print(f"\nMenú de hoy: {menu_hoy}")