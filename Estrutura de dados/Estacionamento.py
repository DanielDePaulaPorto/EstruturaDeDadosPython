class Veiculo:
    def __init__(self, placa, tamanho):
        self.placa = placa
        self.tamanho = tamanho


class Estacionamento:
    def __init__(self):
        self.slots = [0 for i in range(10)]

    def estacione(self, veiculo):
        tamanho_veiculo = veiculo.tamanho
        contador_vaga = 0
        for i in range(10):
            if self.slots[i] == 0:
                contador_vaga += 1
            else:
                contador_vaga = 0
            if contador_vaga == tamanho_veiculo:
                for j in range(i-tamanho_veiculo+1,i+1):
                    self.slots[j] = veiculo
                return True
        return False

    def print(self):
        for i in range(10):
            print(self.slots[i].placa if self.slots[i] != 0 else 0,end=' ')
        print("---")

est = Estacionamento()

est.print()
print(est.estacione(Veiculo('aaa111',3)))
print(est.estacione(Veiculo('aaa222',2)))
print(est.estacione(Veiculo('aaa333',3)))
print(est.estacione(Veiculo('aaa444',2)))
est.print()




