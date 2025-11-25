def muestra_personas(dni: str, /, **kwargs) -> None:
    print("--- DATOS ---")
    print(f"DNI: {dni}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
    print("------------------")

muestra_personas("0000000R", Nombre="Ana", Edad=18)
muestra_personas("1111111L", Nombre="Juan", Edad=20, Poblacion="Sevilla")