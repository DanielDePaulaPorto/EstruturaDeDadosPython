lista_original = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]


def busca_binaria(lista, item):
    tamanho = len(lista)
    limite_inferior = 0
    limite_superior = tamanho - 1

    while limite_inferior <= limite_superior:
        indice_teste = (limite_inferior + limite_superior) // 2
        print(f"--{indice_teste}")
        if lista[indice_teste] == item:
            return True
        elif lista[indice_teste] < item:
            limite_inferior = indice_teste + 1
        else:
            limite_superior = indice_teste - 1
    return False


def busca_binaria_recursiva(lista, item, limite_superior, limite_inferior=0):
    if limite_inferior > limite_superior:
        return False

    indice_teste = (limite_inferior + limite_superior) // 2
    print(f"--{indice_teste}")

    if lista[indice_teste] == item:
        return True
    elif lista[indice_teste] < item:
        return busca_binaria_recursiva(lista, item, limite_superior, indice_teste + 1)
    else:
        return busca_binaria_recursiva(lista, item, indice_teste - 1, limite_inferior)


# print(busca_binaria(lista_original,111))
print(busca_binaria_recursiva(lista_original, -135, len(lista_original) - 1))
