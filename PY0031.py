# Datos iniciales de calificaciones
calificaciones = [
    {'alumno': 'Ana', 'modulo': 'Programación', 'nota': 7.5},
    {'alumno': 'Luis', 'modulo': 'Sistemas', 'nota': 6.0},
    {'alumno': 'Luis', 'modulo': 'Programación', 'nota': 4.0},
    {'alumno': 'Ana', 'modulo': 'Sistemas', 'nota': 8.0},
    {'alumno': 'Marta', 'modulo': 'Programación', 'nota': 9.0},
    {'alumno': 'Marta', 'modulo': 'Programación', 'nota': 10.0},
    {'alumno': 'Marta', 'modulo': 'Sistemas', 'nota': 8.0}
]

# Construir estructura anidada alumnos: {alumno: {modulo: [notas]}}
alumnos = {}
for m in calificaciones:  # se recorre la lista de calificaciones donde cada posicion es un dic con alumno, modulo, nota.
    a = m['alumno']  # casi equivalente a get.
    mod = m['modulo']
    nota = m['nota']
    alumnos.setdefault(a, {}).setdefault(mod, []).append(nota)
    """  alumnos.setdefault(a, {}).setdefault(mod, []).append(nota) es equivalente al bloque de abajo

        modulos_alumno_concreto = alumnos.setdefault(a, {}) #devuelve el diccionario de a, si no existe lo crea vacio y lo devuelve
        notas_modulo_concreto = modulos_alumno_concreto.setdefault(mod, []) #devuelve la lista de notas de mod, si no existe lo crea vacio y lo devuelve
        notas_modulo_concreto.append(nota) # añade la nota al final de la lista.
    """

print("== Estructura alumnos ==")
print(alumnos)

# Media de las notas de un aluno
"""
Calculo de la media aritmetica de todos los módulos de un alumno. Para calcular la media, se 
cogera la nota máxima de cada modulo, en caso de no tener nota no se tendrá en cuenta ese modulo

alumnos {'Ana': {'Programación': [7.5], 'Sistemas': [8.0]}, 
        'Luis': {'Sistemas': [6.0]}, 
        'Marta': {'Programación': [9.0, 10.0], 'Sistemas': [8.0] } #su media seria (10+8)/2 = 9
        }
"""

medias_x_alu = {}
for a, modulos_y_notas in alumnos.items():
    nota_max_mod = [max(notas) for notas in modulos_y_notas.values() if notas]
    print("a ", a)
    print("modulos_y_notas ", modulos_y_notas)
    print("nota_max_mod ", nota_max_mod)

    medias_x_alu[a] = sum(nota_max_mod) / len(nota_max_mod)

print("== Media por alumno ==")
print(medias_x_alu)

# Diccionario de notas de alumnado en un módulo -> {modulo, {alumno: media_en_módulo}}
invertido = {}
for a, mod_notas in alumnos.items():
    for mod, notas in mod_notas.items():
        if notas:
            maxima = max(notas)
            invertido.setdefault(mod, {})[a] = maxima

print("== Diccionario modulo y alumnos con nota max -> {alumno: nota_modulo} ==")
print(invertido)

# Aprobados por módulo (media >= 5)
corte = 5.0
aprobados = {
    mod: {al: maxima for al, maxima in d.items() if maxima >= corte}
    for mod, d in invertido.items()
}
print("== Aprobados por módulo (media >= 5) ==")
print(aprobados)

# CORRECCIONES DE NOTAS Simular correcciones sobre la ÚLTIMA nota de cada módulo afectado
correcciones = {'Ana': {'Programación': +0.75}}  # ejemplo
# alumnos_corregidos = deepcopy(alumnos)  # para no tocar el original
for alumno, mods in correcciones.items():
    sub = alumnos.get(alumno)  # alumnos_corregidos.get(alumno) #linea para deepcopy
    if not sub:
        continue
    for modulo, cambio in mods.items():
        notas = sub.get(modulo)
        if not notas:
            continue
        notas[-1] = notas[-1] + cambio

# print("== Estructura tras correcciones ==")
print("")
print(alumnos)  # print(alumnos_corregidos) #linea para deepcopy

# Eliminar una matrícula concreta (alumno, módulo, índice de intento)
alumno_obj = 'Ana'
modulo_obj = 'Programación'
indice_intento = 0  # indica que nota ha de eliminar de todas las que tiene en la lista de notas de un modulo

try:
    if alumno_obj not in alumnos or modulo_obj not in alumnos[alumno_obj]:
        raise KeyError(f"No existe la combinación alumno={alumno_obj}, modulo={modulo_obj}")
        # print(f"No existe la combinación alumno={alumno_obj}, modulo={modulo_obj}")
    notas = alumnos[alumno_obj][modulo_obj]
    if not (0 <= indice_intento < len(notas)):
        raise IndexError(f"Índice de intento fuera de rango: {indice_intento}")
        # print(f"Índice de intento fuera de rango: {indice_intento}")
    valor_eliminado = notas.pop(indice_intento)
    if not notas:
        alumnos[alumno_obj].pop(modulo_obj)
    if not alumnos[alumno_obj]:
        alumnos.pop(alumno_obj)

    print("== Nota eliminada ==")
    print(valor_eliminado)
    print("== Estructura tras eliminación ==")
    print(alumnos)
except (KeyError, IndexError) as e:
    print("Error al eliminar matrícula:", e)

# Añadir el Ranking de alumnos por nota media ordenador (descendente), en caso de empate se ordena nombre. (sorted-lambda)
ranking = sorted(
    medias_x_alu.items(),
    key=lambda x: (-x[1], x[0])
)
print("== Ranking ==")
for alumno, media in ranking:
    print(f"Alumno: {alumno}, media: {media:.2f}")