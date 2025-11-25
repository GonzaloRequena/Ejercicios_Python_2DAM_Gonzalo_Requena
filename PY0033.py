from typing import Any

lista = [6, 1, 8, 7, 3, 2, 4, 9, 5]

def separar_lista(lista: list[int]) -> tuple[list[Any], list[Any]]:
    listaPar = []
    listaImpar = []

    for elemento in lista:
        if elemento % 2 == 0:
            listaPar.append(elemento)
        else :
            listaImpar.append(elemento)
    return listaPar, listaImpar

if __name__ == '__main__':
    listaPar, listaImpar = separar_lista(lista)
    print(separar_lista(lista))