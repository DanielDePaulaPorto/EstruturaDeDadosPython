lista_inicial = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7]


# Tetativa 1 - Sem HashTable
def conta_ocorrencias(lista):
    ocorrencias = [lista.count(item) for item in lista]

    maior = max(ocorrencias)
    indice_maior = lista.index(maior)

    return lista[indice_maior]


# Tetativa 2 - Com HashTable
def conta_ocorrencias_hash(lista):
    hash_table = {}
    maior = lista[0]

    for i in range(len(lista)):
        try:
            hash_table[lista[i]] += 1
        except:
            hash_table[lista[i]] = 1

        if hash_table[lista[i]] > hash_table[maior]:
            maior = lista[i]

    return maior


maior_ocorrencia = conta_ocorrencias_hash(lista_inicial)

print(f"O valor de maior ocorrência é {maior_ocorrencia}")
