# función que crea el diccionario de pizzas y lo devuelve
def crear_pizzas() -> dict[str, float]:
    pizzas = {"Margarita": 8, "Cuatro quesos": 12.5, "Austriaca": 8, "Pepperoni": 10}
    return pizzas


# función que muestra el menú, ordenándolo y recorriéndolo para mostrar cada pizza y su precio
def mostrar_menu(pizzas: dict[str, float]) -> None:
    print("== MENÚ DE PIZZAS ==")
    pizzas_ordenadas = sorted(pizzas.items(), key=lambda x: (-x[1], x[0]))
    for i in range(len(pizzas_ordenadas)):
        print(f"{i + 1}. {pizzas_ordenadas[i][0]} - {pizzas_ordenadas[i][1]:.2f}")
    print("--------------------")


# función que pide nueva pizza y precio a insertar
# Si la pizza ya existe, actualiza el precio, si no existe, la añade al diccionario
def modificar_pizzas(pizzas: dict[str, float]) -> dict[str, float]:
    nueva_pizza = input("Escribe el nombre de la pizza: ").strip()
    try:
        nuevo_precio = float(input("Escribe el precio de la pizza: "))
        nuevo_precio = nuevo_precio

        if nuevo_precio <= 0:
            print("El precio debe ser mayor que 0.")
            return pizzas
    except ValueError:
        print("Formato incorrecto. El precio debe ser un número.")
        return pizzas

    for nombre in pizzas.keys():
        if nombre.lower() == nueva_pizza.lower():
            pizzas[nombre] = nuevo_precio
            break
        else:
            pizzas[nueva_pizza.capitalize()] = nuevo_precio
            break
    return pizzas


pizzas = crear_pizzas()
while True:
    mostrar_menu(pizzas)
    respuesta = input("¿Quieres añadir una pizza nueva en el menú? S/N ").strip().upper()
    if respuesta == "N":
        break
    if respuesta == "S":
        pizzas = modificar_pizzas(pizzas)
    else:
        print("Responde sí o no: S/N ")

# Si se quiere delegar ciertos aspectos del código como mostrar el menú o modificar pizzas
# a funciones, éstas necesitan recibir el diccionario pizzas como parámetro para poder operar
