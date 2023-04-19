from pythonds.basic.queue import Queue

# Implemente uma fila de prioridade para pessoas considerando que.
# A ordem de chegada define a ordem de atendimento.
# Idosos (60+), deficientes, grávidas e pessoas com crianças de colo têm prioridade.
# Idosos (80+) têm maior prioridade.

class Pessoa:

    def __init__(self, chegada, idade):
        self.chegada = chegada
        self.idade = idade

    def __repr__(self):
        return f"Pessoa (inicialmente na posicao {self.chegada}) com {self.idade} anos."

class Fila_Com_Prioridade:

    def __init__(self):
        self.fila_normal = Queue()
        self.fila_idosos60 = Queue()
        self.fila_idosos80 = Queue()

    def enqueue(self, Pessoa):
        if Pessoa.idade >= 80:
            self.fila_idosos80.enqueue(Pessoa)
        elif Pessoa.idade >= 60:
            self.fila_idosos60.enqueue(Pessoa)
        else:
            self.fila_normal.enqueue(Pessoa)

    def dequeue(self):
        if not self.fila_idosos80.isEmpty():
            return self.fila_idosos80.dequeue()
        elif not self.fila_idosos60.isEmpty():
            return self.fila_idosos60.dequeue()
        elif not self.fila_normal.isEmpty():
            return self.fila_normal.dequeue()
        else:
            return "LISTA VAZIA!!!"

minha_Fila = Fila_Com_Prioridade()

for i in range(7):
    idade = int(input("Informe a idade da pessoa que entrou na fila: "))
    pessoa = Pessoa(i, idade)
    minha_Fila.enqueue(pessoa)


for i in range(7):
    print(minha_Fila.dequeue())

