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
        self.filhos = []

    def inserirFilho(self, novo_no):
        self.filhos.append(novo_no)

    def getFilhos(self):
        return self.filhos


class Arvore:

    def __init__(self, raiz):
        self.raiz = raiz

    def getValorRaiz(self):
        return self.valor

    def setValorRaiz(self, valor):
        self.valor = valor

    def printPreorder(self, noPai):
        print(noPai.valor)
        for no in noPai.filhos:
            self.printPreorder(no)

    def printPostorder(self, noPai):
        for no in noPai.filhos:
            self.printPostorder(no)
        print(noPai.valor)

    # - função que conte o número total de nós
    def contaNos(self, noPai):
        contador = 1
        for no in noPai.filhos:
            contador += self.contaNos(no)
        return contador

    # - função que calcule a altura da árvore
    def getAltura(self, noPai):
        maiorAlturaFilhos = 0
        for no in noPai.filhos:
            alturaFilho = self.getAltura(no)
            if alturaFilho > maiorAlturaFilhos:
                maiorAlturaFilhos = alturaFilho
        return 1 + maiorAlturaFilhos

    # - função que calcule o número de folhas
    def getFolhas(self, noPai):
        if len(noPai.filhos) == 0:
            return 1
        else:
            nosFolhas = 0
            for no in noPai.filhos:
                nosFolhas += self.getFolhas(no)
            return nosFolhas

    # - função que faça a poda da árvore, removendo todos os nós abaixo de um determinado nível.
    def poda(self, noPai, nivelPoda, nivelAtual):
        if nivelAtual > nivelPoda:
            noPai.filhos = []

        for no in noPai.filhos:
            self.poda(no, nivelPoda, nivelAtual + 1)


noRaiz = No(0)

no1 = No(1)
noRaiz.inserirFilho(no1)

no12 = No(12)
no13 = No(13)
no14 = No(14)
no1.inserirFilho(no12)
no1.inserirFilho(no13)
no1.inserirFilho(no14)

no112 = No(112)
no113 = No(113)
no12.inserirFilho(no112)
no12.inserirFilho(no113)

no1112 = No(1112)
no1113 = No(1113)
no112.inserirFilho(no1112)
no112.inserirFilho(no1112)

no11112 = No(11112)
no11113 = No(11113)
no1112.inserirFilho(no11112)
no1112.inserirFilho(no11113)

no111112 = No(111112)
no11112.inserirFilho(no111112)

no2 = No(2)
noRaiz.inserirFilho(no2)

no22 = No(22)
no23 = No(23)
no24 = No(24)
no2.inserirFilho(no22)
no2.inserirFilho(no23)
no2.inserirFilho(no24)

no212 = No(212)
no213 = No(213)
no22.inserirFilho(no212)
no22.inserirFilho(no213)

no2112 = No(2112)
no2113 = No(2113)
no212.inserirFilho(no2112)
no212.inserirFilho(no2113)

no21112 = No(21112)
no21113 = No(21113)
no2112.inserirFilho(no21112)
no2112.inserirFilho(no21113)

no211112 = No(211112)
no21112.inserirFilho(no211112)

arvore = Arvore(noRaiz)

print(f"Quantidade de nós: {arvore.contaNos(noRaiz)}")

arvore.printPreorder(noRaiz)
print("---")
arvore.printPostorder(noRaiz)

print("---")
print(f"Qunatidade de folhas: {arvore.getFolhas(noRaiz)}")

print("---")
print(f"Altura: {arvore.getAltura(noRaiz)}")

print("---")
arvore.poda(noRaiz, 3, 0)
print(f"Altura: {arvore.getAltura(noRaiz)}")
arvore.printPreorder(noRaiz)
