def comprueba_argumentos( filas : int, columnas : int) -> None:
    if not (1 <= filas <= 9 and 1 <= columnas <= 9):
        print("Error: Ambos argumentos deben ser números enteros positivos del 1 al 9.")
        parser.print_help()
        exit(1)

def dibuja_tabla(filas : int, columnas : int) -> None:
    # Dibujar la tabla
    for i in range(filas):
        print(" * " * columnas, end='\n')


if __name__ == "__main__":
    import argparse

    # Crear el objeto ArgumentParser
    parser = argparse.ArgumentParser(description="Dibuja una tabla con filas y columnas especificadas")

    # Añadir argumentos para las filas y columnas. Obliga a que sean enteros o da error al ejecutar
    parser.add_argument('filas', type=int, help="Número de filas (entero positivo del 1 al 9)", )
    parser.add_argument('columnas', type=int, help="Número de columnas (entero positivo del 1 al 9)")

    # Parsear los argumentos
    args = parser.parse_args()

    comprueba_argumentos(args.filas, args.columnas)
    dibuja_tabla(args.filas, args.columnas)