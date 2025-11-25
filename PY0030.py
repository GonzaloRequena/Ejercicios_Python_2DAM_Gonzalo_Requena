inventario_inicial = {'CUS001': 12, 'CUS002': 5, 'CUS003': 0}
ventas = ['CUS001', 'CUS002', 'CUS001', 'CUS004']
reposiciones = {'CUS002': 10, 'CUS004': 7}
avisos_ventas = []

print(f"Inventario Inicial: {inventario_inicial}")
print(f"Ventas a procesar: {ventas}")
print(f"Reposiciones a aplicar: {reposiciones}")

inventario_copia = inventario_inicial.copy()

for codigo_venta in ventas:
    if codigo_venta not in inventario_copia:
        inventario_copia.setdefault(codigo_venta, 0)
        avisos_ventas.append(f"AVISO: Venta de producto nuevo/no listado: {codigo_venta}")

    inventario_copia[codigo_venta] -= 1
print(f"\nStock actual: {inventario_copia}")
print(f"Lista de avisos: {avisos_ventas}")

for codigo, cantidad in reposiciones.items():
    stock = inventario_copia.get(codigo, 0)
    inventario_copia[codigo] = stock + cantidad
print(f"\nStock actual: {inventario_copia}")

print("\n--- INFORME---")
print(f"Número de referencias: {len(inventario_copia)}")
print(f"Unidades totales en stock: {sum(inventario_copia.values())}")

# añade al informe el código necesario para que muestre los dos elementos con más stock. (usa sorted-lambda)
masStock = sorted(
    inventario_copia.items(),
    key=lambda x: -x[1],
) [:2]

print(f"Mas stock: {masStock}")

claves_a_borrar = []
for codigo, stock in inventario_copia.items():
    if stock <= 0:
        claves_a_borrar.append(codigo)
if not claves_a_borrar:
    print("\nNo hay productos que eliminar.")
else:
    for codigo in claves_a_borrar:
        inventario_copia.pop(codigo)
        print(f"\nProducto {codigo} eliminado.")
print(f"Stock actual: {inventario_copia}")

consulta = input("\nIntroduce un código de producto a consultar: ")
stock_actual = inventario_copia.get(consulta)

if stock_actual is not None:
    print(f"Stock actual de {consulta}: {stock_actual} unidades.")
else:
    print(f"No existe el código {consulta} en el inventario.")

del inventario_copia
print("\nEl diccionario ha sido eliminado.")

