class Vertice:

    def __init__(self, id):
        self.id = id
        self.adjacentes = {}

    def getId(self):
        return self.id

    def getVizinhos(self):
        return self.adjacentes.keys()

    def imprimeVizinhos(self):
        for key in self.adjacentes.keys():
            print(f"{self.id} -- {self.adjacentes[key]} --> {key}")

    def adicionaVizinho(self, chave, peso):
        self.adjacentes[chave] = peso

    def getPeso(self, vizinho):
        return self.adjacentes[vizinho]


class Grafo:

    def __init__(self):
        self.vertices = []

    def criaVertice(self, id):
        vertice = Vertice(id)
        self.vertices.append(vertice)
        return vertice

    def adicionaAresta(self, verticeOrigem, verticeDestino, peso):
        verticeOrigem.adicionaVizinho(verticeDestino.getId(), peso)


grafo = Grafo()

vA1 = grafo.criaVertice("A1")
vA2 = grafo.criaVertice("A2")
vA3 = grafo.criaVertice("A3")
vA4 = grafo.criaVertice("A4")

grafo.adicionaAresta(vA1, vA2, 5)
grafo.adicionaAresta(vA1, vA3, 7)
grafo.adicionaAresta(vA2, vA3, 2)
grafo.adicionaAresta(vA2, vA4, 1)

vA1.imprimeVizinhos()
vA2.imprimeVizinhos()
vA3.imprimeVizinhos()
vA4.imprimeVizinhos()
