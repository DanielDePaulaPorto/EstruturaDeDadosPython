from pythonds.basic.stack import Stack


class fila_comPilhas:

    def __init__(self):
        self.pilha1 = Stack() # Pilha que vai receber os dados de entrada da fila
        self.pilha2 = Stack() # Pilha que vai retirar os dados da fila

    def enqueue (self, item):
        if self.pilha1.isEmpty():
            self.transfere_pilha(self.pilha2,self.pilha1)
        self.pilha1.push(item)

    def dequeue(self):
        if self.pilha2.isEmpty():
            self.transfere_pilha(self.pilha1,self.pilha2)
        self.pilha2.pop()

    def transfere_pilha(self, pilha_a, pilha_b):
        while not pilha_a.isEmpty():
            pilha_b.push(pilha_a.pop())

    def print(self):
        if self.pilha2.isEmpty():
            self.transfere_pilha(self.pilha1,self.pilha2)
        print("\nElementos da Fila:")
        while not self.pilha2.isEmpty():
            item = self.pilha2.pop()
            print(item)
            self.pilha1.push(item)

fila = fila_comPilhas()

fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)

fila.print()

fila.dequeue()

fila.print()


fila.enqueue(6)

fila.print()

fila.dequeue()
fila.dequeue()

fila.print()
