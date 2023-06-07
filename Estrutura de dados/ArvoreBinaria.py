# Definir um nó
# Criar uma classe Arvore para representar uma arvore não binária
# Definir os métodos:
# - Construtor da classe
# - getRootVal
# - setRootVal
# - printPreorder
# - printPostorder
# - função que conte o número total de nós
# - função que calcule a altura da árvore
# - função que calcule o número de folhas
# - função que faça a poda da árvore, removendo todos os nós abaixo de um determinado nível.

class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

    def insereEsquerda(self, valor):
        noEsquerda = No(valor)
        self.esquerda = noEsquerda

    def insereDireita(self, valor):
        noDireita = No(valor)
        self.direita = noDireita


class Arvore:

    def __init__(self, raiz):
        self.raiz = raiz

    def getValorRaiz(self):
        return self.valor

    def setValorRaiz(self, valor):
        self.valor = valor

    def insereNovoNo(self, noPai, valor):
        if valor < noPai.valor:
            if noPai.esquerda is None:
                novoNo = No(valor)
                noPai.esquerda = novoNo
            else:
                self.insereNovoNo(noPai.esquerda, valor)
        else:
            if noPai.direita is None:
                novoNo = No(valor)
                noPai.direita = novoNo
            else:
                self.insereNovoNo(noPai.direita, valor)

    def printPreorder(self, noPai):
        print(noPai.valor)
        if noPai.esquerda != None:
            self.printPreorder(noPai.esquerda)
        if noPai.direita != None:
            self.printPreorder(noPai.direita)

    def printPostorder(self, noPai):
        if noPai.esquerda != None:
            self.printPostorder(noPai.esquerda)
        if noPai.direita != None:
            self.printPostorder(noPai.direita)
        print(noPai.valor)

    def printInorder(self, noPai):
        if noPai.esquerda != None:
            self.printInorder(noPai.esquerda)
        print(noPai.valor)
        if noPai.direita != None:
            self.printInorder(noPai.direita)

    def imprimir_arvore(self, no, prefixo="", is_ultimo=True):
        # Imprime o prefixo
        print(prefixo, end="")

        # Verifica se é o último nó do nível
        if is_ultimo:
            print("`-- ", end="")
            prefixo += "    "
        else:
            print("|-- ", end="")
            prefixo += "|   "

        # Imprime o valor do nó atual
        print(no.valor)

        # Imprime os filhos recursivamente
        if no.direita != None:
            self.imprimir_arvore(no.direita, prefixo, no.direita.direita != None or no.direita.esquerda != None)

        if no.esquerda != None:
            self.imprimir_arvore(no.esquerda, prefixo, no.esquerda.direita != None or no.esquerda.esquerda != None)

    # - função que conte o número total de nós
    def contaNos(self, noPai):
        contador = 1
        if noPai.esquerda != None:
            contador += self.contaNos(noPai.esquerda)

        if noPai.direita != None:
            contador += self.contaNos(noPai.direita)

        return contador

    # - função que calcule a altura da árvore
    def getAltura(self, noPai):
        maiorAlturaFilhos = 0

        if noPai.esquerda != None:
            alturaFilhoEsquerda = self.contaNos(noPai.esquerda)

        if noPai.direita != None:
            alturaFilhoDireita = self.contaNos(noPai.direita)

        if alturaFilhoEsquerda > maiorAlturaFilhos:
            maiorAlturaFilhos = alturaFilhoEsquerda

        if alturaFilhoDireita > maiorAlturaFilhos:
            maiorAlturaFilhos = alturaFilhoDireita

        return 1 + maiorAlturaFilhos

    # - função que calcule o número de folhas
    def getFolhas(self, noPai):

        if noPai.direita == None and noPai.esquerda == None:
            return 1
        else:
            nosFolhas = 0
            if noPai.esquerda != None:
                nosFolhas += self.getFolhas(noPai.esquerda)

            if noPai.direita != None:
                nosFolhas += self.getFolhas(noPai.direita)

            return nosFolhas


noRaiz = No(50)

arvore = Arvore(noRaiz)

arvore.insereNovoNo(noRaiz, 30)
arvore.insereNovoNo(noRaiz, 70)
arvore.insereNovoNo(noRaiz, 20)
arvore.insereNovoNo(noRaiz, 80)
arvore.insereNovoNo(noRaiz, 10)
arvore.insereNovoNo(noRaiz, 40)
arvore.insereNovoNo(noRaiz, 90)

arvore.imprimir_arvore(noRaiz)

print(f"Quantidade de nós: {arvore.contaNos(noRaiz)}")
#
arvore.printPreorder(noRaiz)
print("---")
arvore.printPostorder(noRaiz)
print("---")
arvore.printInorder(noRaiz)
#
print("---")
print(f"Qunatidade de folhas: {arvore.getFolhas(noRaiz)}")

print("---")
print(f"Altura: {arvore.getAltura(noRaiz)}")


# ---------------------

# texto = "String de texto"

def get_String_Binaria(stringTexto):
    stringBinaria = ""
    for caractere in stringTexto:
        valorDecimal = ord(caractere)
        valorBinario = bin(valorDecimal)[2:].zfill(8)
        # print(valorBinario)
        stringBinaria += valorBinario
    return stringBinaria


# strBin = get_String_Binaria(texto)
# print(strBin)

def get_Array_Bytes(stringBinaria):
    return bytearray([int(stringBinaria[i:i + 8], 2) for i in range(0, len(stringBinaria))])

# array = get_Array_Bytes(strBin)
