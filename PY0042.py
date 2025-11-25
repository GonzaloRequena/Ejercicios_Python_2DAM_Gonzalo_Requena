def f_listaComun(l1 : list, l2 : list) -> list:
    listaComun = list(filter(lambda x: x in l1, l2))
    #listaComun = [x for x in lista1 if x in lista2]
    elementos_comunes = list(set(listaComun))#eliminaDuplicados
    return elementos_comunes, "Lista de elementos comunes"


if __name__ == "__main__":
    lista1 = [1, 2, 3, 4, 5, 6]
    lista2 = [4, 5, 6, 7, 8, 9, 6]
    listacomun, comentario = f_listaComun(lista1,lista2)
    print(f"{comentario} - {listacomun}")