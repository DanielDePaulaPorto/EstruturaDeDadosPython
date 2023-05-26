def cria_hash(string):
    hash_table = {}
    lista_string = list(string)
    for i in range(len(string)):
        try:
            hash_table[lista_string[i]] += 1
        except:
            hash_table[lista_string[i]] = 1

    return hash_table


def anagrama_hash(s, t):
    hash_table_s = cria_hash(s)
    hash_table_t = cria_hash(t)

    if hash_table_s == hash_table_t:
        print(f"{s} e {t} são anagramas!")
    else:
        print(f"{s} e {t} NÃO são anagramas!")


anagrama_hash("aaabbb", "ababab")
