class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        for i in range(self.size()):
            print(f"{self.items[self.size()-i-1]}", end=', ')


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def print(self):
        for i in range(self.size()):
            print(f"{self.items[self.size()-i-1]}", end=', ')

class Cafeteria:
    def __init__(self):
        self.alunos = Queue()
        self.lanche = Stack()

    def serve_almoco(self):
        aluno_pegou_saduiche = True
        while aluno_pegou_saduiche:
            aluno_pegou_saduiche = False
            for i in range(self.alunos.size()):
                print("\n---\nAlunos: ")
                self.alunos.print()
                print("\nSanduiches: ")
                self.lanche.print()

                aluno = self.alunos.dequeue()
                lanche = self.lanche.pop()

                if aluno == lanche:
                    print('\n Deu certo')
                    aluno_pegou_saduiche = True
                else:
                    self.alunos.enqueue(aluno)
                    self.lanche.push(lanche)

        return print("\n\n---\n",self.alunos.size(), 'aluno(s) nao vai(ao) comer')


# circular 0
# quadrado 1

fila_alunos = [0,0,0,1,1,1]
pilha_lanche = [0,1,0,1,1,1]


cafeteria = Cafeteria()
for i in range(len(fila_alunos)):
    cafeteria.alunos.enqueue(fila_alunos[i])
for i in range(len(pilha_lanche)):
    cafeteria.lanche.push(pilha_lanche[len(pilha_lanche) - i - 1])

cafeteria.serve_almoco()