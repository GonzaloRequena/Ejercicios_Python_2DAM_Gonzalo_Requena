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

# #PY0025
# paises = ["España", "Argentina", "Perú"]
# maxPaises = 6
# nOperaciones = 0
# nIntentos = 0
# operacionValida = False
# operacionExitosa = False
# while True:
#     nIntentos += 1
#     print("\n-----------------------------------")
#     print("---MENÚ PAÍSES---")
#     print(f"Intento nº {nIntentos}")
#     print("1. Imprimir alfabéticamente en orden ascendente.")
#     print("2. Imprimir alfabéticamente en orden descendente.")
#     print("3. Añadir país.")
#     print("4. Eliminar país.")
#     print("5. Salir.")
#     print("-----------------------------------")
#
#     operacionValida = False
#     operacionExitosa = False
#
#     try:
#         opcion = int(input("\nElige una opción: "))
#         if opcion >= 1 and opcion <= 5:
#             operacionValida = True
#         else:
#             print("Debes introducir una opción del menú.")
#
#     except ValueError:
#         print("Debes introducir una opción del menú.")
#     if operacionValida:
#         if opcion == 5:
#             break
#         nOperaciones += 1
#         print(f"---Operación nº {nOperaciones} realizada.---")
#         if opcion == 1:
#             paises.sort()
#             print(paises)
#             print("\n")
#             operacionExitosa = True
#         elif opcion == 2:
#             paises.sort(reverse=True)
#             print(paises)
#             print("\n")
#             operacionExitosa = True
#         elif opcion == 3:
#             if len(paises) >= maxPaises:
#                 print(f"La lista no puede ser de más de {maxPaises} países.")
#             else:
#                 pais = input("Añade un nuevo país a la lista: ").strip().lower().capitalize()
#                 if pais == "":
#                     print("El nombre del país no es válido.")
#                 elif pais in paises:
#                     print(f"{pais} ya está en la lista.")
#                 else:
#                     paises.append(pais)
#                     print(f"{pais} añadido a la lista.")
#                     print(paises)
#                     print("\n")
#                     operacionExitosa = True
#         elif opcion == 4:
#             if len(paises) == 0:
#                 print("La lista está vacía. No hay países que eliminar.")
#             else:
#                 pais = input("Indica el país a eliminar: ").strip().lower().capitalize()
#                 if pais in paises:
#                     paises.remove(pais)
#                     print(f"{pais} eliminado de la lista.")
#                     print(paises)
#                     print("\n")
#                     operacionExitosa = True
#                 else:
#                     print(f"{pais} no existe en la lista.")
#         if operacionExitosa:
#             print("#" * 70 + "\n")
#
# if opcion ==5 and operacionValida:
#     print("\n-----------------------------------")
#     print("¡Gracias por confiar en nosotros!")
#     print(f"Número total de intentos: {nIntentos}")
#     print("¡Un saludo!")

# #PY0028
# pizzas = ["Margarita", "Napolitana", "Carbonara", "Barbacoa"]
# precios = [10.50, 11.50, 12.50, 15.00]
# extras = ["Queso", "Aceitunas", "Champiñones"]
# preciosExtra = [1.25, 0.50, 0.75]
#
# print("--- PIZZERIA LA BEATA ---")
# while True:
#     saldo = 0.0
#
#     while True:
#         try:
#             cantidad = input("\nIntroduce tu saldo: ")
#             saldo = round(float(cantidad), 2)
#             if saldo <= 0:
#                 print("El saldo debe ser positivo.")
#                 continue
#             break
#         except ValueError:
#             print("El saldo no es válido.")
#
#     print("\n--- MENÚ ---")
#     for i in range(len(pizzas)):
#         print(f"{i + 1}. {pizzas[i]}: {precios[i]:.2f}€")
#     print("\n")
#     pizzaElegida = ""
#     costePizza = 0.0
#
#     while True:
#         try:
#             opcion = int(input("Elige una pizza: "))
#             if opcion < 1 or opcion > len(pizzas):
#                 print("Elige una pizza del menú.")
#             else:
#                 i = opcion - 1
#                 pizzaElegida = pizzas[i]
#                 costePizza = precios[i]
#                 saldoRestante = round(float(saldo - costePizza), 2)
#                 if saldoRestante < 0:
#                     print("El saldo no es suficiente. Por favor, inténtalo de nuevo.")
#                     costePizza = 0.0
#                     break
#                 print(f"Has elegido {pizzaElegida}: {costePizza:.2f}€.")
#                 print(f"Saldo restante: {saldoRestante:.2f}€.")
#                 break
#         except ValueError:
#             print("Opción no válida. Elige una pizza del menú.")
#     if costePizza == 0.0:
#         continue
#
#     extrasElegidos = []
#     costeExtras = 0.0
#
#     while True:
#         respuesta = input("\n¿Quieres añadirle algún extra? S/N ").strip().upper()
#         if respuesta == "N":
#             break
#         elif respuesta == "S":
#             print("EXTRAS: ")
#             for i in range(len(extras)):
#                 print(f"{i + 1}. {extras[i]}: {preciosExtra[i]:.2f}.")
#
#             while True:
#                 cantidad = input("\nElige una extra o elige \"Salir\": ")
#                 if cantidad.lower().capitalize() == "Salir":
#                     break
#                 try:
#                     opcionExtra = int(cantidad)
#                     if opcionExtra >= 1 and opcionExtra <= len(extras):
#                         i = opcionExtra - 1
#                         costeExtraAnterior = costeExtras
#                         costeExtras += preciosExtra[i]
#                         costeTotal = costePizza + costeExtras
#                         saldoRestante = round(saldo - costeTotal, 2)
#                         if saldoRestante < 0:
#                             print("El saldo no es suficiente. Por favor, inténtalo de nuevo.")
#                             costeExtras = costeExtraAnterior
#                             break
#                         extrasElegidos.append(extras[i])
#                         print(f"Has elegido {extrasElegidos}.")
#                         print(f"Saldo restante: {saldoRestante:.2f}€.")
#                     else:
#                         print("Elige una extra del menú o elige \"Salir\".")
#                 except ValueError:
#                     print("Opción no válida. Elige una extra o elige \"Salir\".")
#         else:
#             print("Elige S ó N.")
#
#     costeTotal = costePizza + costeExtras
#     print("\n ---------------------------------")
#     if saldoRestante < 0:
#         print("El saldo no es suficiente. Por favor, inténtalo de nuevo.")
#         continue
#     else:
#         print("--- Tu pedido ---")
#         print(f"El total del pedido es {costeTotal:.2f}€.")
#         print(f"Tu cambio de {saldo:.2f}€ es de {saldoRestante:.2f}€.")
#         print("\n")
#         print(f"- {pizzaElegida} {costePizza:.2f}€")
#         for extra_nombre in extrasElegidos:
#             indice_extra = extras.index(extra_nombre)
#             precio_extra = preciosExtra[indice_extra]
#             print(f"- Extra de {extra_nombre} {precio_extra:.2f}€")
#         print("\nGracias por su visita.")
#         break

# #PY0027
# usuarios = {"Marta", "David", "Elvira", "Juan", "Marcos"}
# administradores = {"Juan", "Marta"}
# administradores.discard("Juan")
# administradores.add("Marcos")
# for usuario in usuarios:
#     if usuario in administradores:
#         print(f"{usuario}. Es administrador.")
#     else:
#         print(f"{usuario}. No es administrador.")

# #PY0005
# miembros = {"Mercedes", "Lucía", "Fernando", "Pilar", "Gonzalo"}
# print(f"Miembros: {miembros}")
# while True:
#     nombre = input("Introduce un nuevo miembro o \"Fin\" para terminar: ").strip().capitalize()
#     if nombre == "":
#         print("El nombre no puede estar vacío.")
#         continue
#     elif nombre.lower().capitalize() == "Fin":
#         break
#     else:
#         miembros.add(nombre)
#         print(f"{miembros}\n")
# lote = input("Introduce varios nombres separados por \",\": ").strip().split(",")
# for nombre in lote:
#     nombre = nombre.strip().lower().capitalize()
#     if nombre != "":
#         miembros.add(nombre)
#
# miembrosCopia = miembros.copy()
#
# while True:
#     nombre = input("¿A quién quieres dar de baja? Usa \"Fin\" para terminar: ").strip().capitalize()
#     if nombre.lower().capitalize() == "Fin":
#         break
#     if nombre == "":
#         print("El nombre no puede estar vacío.")
#         continue
#     elif nombre not in miembros:
#         print("El nombre no está en la lista.")
#         continue
#     else:
#         miembros.remove(nombre)
#
# consulta = input("¿A quién quieres buscar para ver si está inscrito? ").strip().capitalize()
# if consulta in miembros:
#     print(f"{consulta} es miembro.")
# else:
#     print(f"{consulta} no es miembro.")
#
# otroGrupo = {"Juan", "Pepe", "Lucía", "Rafa"}
# print(f"Vamos a mirar si alguno de ellos es miembro: {otroGrupo}")
#
# repetidos = miembros.intersection(otroGrupo)
# if repetidos:
#     print(f"Los siguientes miembros están en ambos grupos: {repetidos}")
# else:
#     print("Nadie está en ambos grupos.")
#
# print(f"El número total de miembros inscritos es de {len(miembros)}.")
# mienbrosOrdenados = sorted(miembros)
# print(f"Miembros ordenados alfabéticamente: {mienbrosOrdenados}")

# #PY0023

# #PY0026
# Si el grupo de países pasase a ser un set, habría que declararlo con {} en vez de []:
# paises = {"España", "Argentina", "Perú"}
# Además, algunas operaciones como ordenar con sort no se podrían hacer, porque los set no tienen orden
# interno. Del mismo, modo, no habría que controlar que haya países repetidos porque los set no permiten duplicados.
# Por otro lado, para añadir países, habría que usar paises.add(pais) en vez de paises.append(pais).
# Para eliminar sí es igual, con paises.remove(pais).

# No tendría sentido hacer este ejercicio con tuplas ya que son inmutables una vez creadas.
# Por tanto no podríamos hacerle los cambios que se piden como añadir, eliminar, ordenar, etc.

# #PY0006
# inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}
# ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
# reposiciones = {'CUS002': 10, 'CUS004': 7}
# avisos_ventas = []
#
# print(f"Inventario Inicial: {inventario_inicial}")
# print(f"Ventas a procesar: {ventas}")
# print(f"Reposiciones a aplicar: {reposiciones}")
#
# inventario_copia = inventario_inicial.copy()
#
# for codigo_venta in ventas:
#     if codigo_venta not in inventario_copia:
#         inventario_copia.setdefault(codigo_venta, 0)
#         avisos_ventas.append(f"AVISO: Venta de producto nuevo/no listado: {codigo_venta}")
#
#     inventario_copia[codigo_venta] -= 1
# print(f"\nStock actual: {inventario_copia}")
# print(f"Lista de avisos: {avisos_ventas}")
#
# for codigo, cantidad in reposiciones.items():
#     stock = inventario_copia.get(codigo, 0)
#     inventario_copia[codigo] = stock + cantidad
# print(f"\nStock actual: {inventario_copia}")
#
# print("\n--- INFORME---")
# print(f"Número de referencias: {len(inventario_copia)}")
# print(f"Unidades totales en stock: {sum(inventario_copia.values())}")
#
# claves_a_borrar = []
# for codigo, stock in inventario_copia.items():
#     if stock <= 0:
#         claves_a_borrar.append(codigo)
# if not claves_a_borrar:
#     print("\nNo hay productos que eliminar.")
# else:
#     for codigo in claves_a_borrar:
#         inventario_copia.pop(codigo)
#         print(f"\nProducto {codigo} eliminado.")
# print(f"Stock actual: {inventario_copia}")
#
# consulta = input("\nIntroduce un código de producto a consultar: ")
# stock_actual = inventario_copia.get(consulta)
#
# if stock_actual is not None:
#     print(f"Stock actual de {consulta}: {stock_actual} unidades.")
# else:
#     print(f"No existe el código {consulta} en el inventario.")
#
# del inventario_copia
# print("\nEl diccionario ha sido eliminado.")

# #PY0007
calificaciones = [
    {"alumno": "Ana", "modulo": "Programación", "nota": 7.5},
    {"alumno": "Luis", "modulo": "Sistemas", "nota": 6.0},
    {"alumno": "Ana", "modulo": "Sistemas", "nota": 8.0},
    {"alumno": "Marta", "modulo": "Programación", "nota": 9.0},
    {"alumno": "Marta", "modulo": "Programación", "nota": 10.0},
]

alumnos = {}
for linea in calificaciones:
    alumno = linea["alumno"]
    modulo = linea["modulo"]
    nota = linea["nota"]

    alumnos.setdefault(alumno, {}).setdefault(modulo, []).append(nota)
print(alumnos)

mediasNota = {}
for alumno, modulosNotas in alumnos.items():
    notas_maximas = [max(notas) for notas in modulosNotas.values() if notas]
    media = sum(notas_maximas) / len(notas_maximas)
    mediasNota[alumno] = media
print(mediasNota)

notas_por_modulo = {}
for alumno, modulosNotas in alumnos.items():
    for modulo, notas in modulosNotas.items():
        if notas:
            notaMaxima = max(notas)
            notas_por_modulo[modulo] = {alumno: notaMaxima}
            notas_por_modulo.setdefault(modulo, []).append(alumno)
print(notas_por_modulo)

