
# Impressão de uma lista aninhada
#
lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]]]

def imprime_lista(lista):
    while lista:
        elemento = lista.pop(0)
        if type(elemento) == type([]):
            lista = elemento + lista
        else:
            print(elemento)

def imprime_lista_recursivo(lista):
    for elemento in lista:
        if type(elemento) != type([]):
            print(elemento)
        else:
            imprime_lista_recursivo(elemento)



# imprime_lista(lst)

print("---")

imprime_lista_recursivo(lst)
