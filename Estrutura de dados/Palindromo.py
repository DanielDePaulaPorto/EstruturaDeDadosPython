

def eh_palindromo(palavra):
    # print(palavra)
    if len(palavra) < 2:
        return True
    else:
        head = palavra.pop(0)
        tail = palavra.pop()
        if head != tail:
            return False
        else:
            return eh_palindromo(palavra)

entrada = "radar"

print(eh_palindromo(list(entrada)))


