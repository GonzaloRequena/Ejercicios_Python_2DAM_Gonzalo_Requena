from _datetime import datetime
from time import strftime


def agregar_tarea(desctarea: str, registro:list=None, usuario: str="sistema") -> list:
    tarea = {}
    if registro is None:
        registro = []
    tarea["desctarea"] = desctarea
    tarea["fecha"] = datetime.now().strftime("%Y/%m/%d - %H:%M:%S")
    tarea["usuario"] = usuario
    registro.append(tarea)
    return registro

registro_jorge = agregar_tarea("enviar sms", usuario="jorge")
registro_jorge = agregar_tarea("corregir sms", registro_jorge, "jorge")

registro_ana = agregar_tarea("corregir bug", usuario="ana")
registro_ana = agregar_tarea("corregir bug2", registro_ana, "ana")

print(registro_jorge)
print(registro_ana)
