class Senado_Dota2:

    def __init__(self):
        self.lista = []

    def recebe_string_inicial(self,senate):
        for letra in senate:
            self.lista.append(letra)

    def calcula_resultado(self):
        tem_resultado = False
        while not tem_resultado:
            if self.lista[0] == "R":
                if "D" in self.lista:
                    oponente = self.lista.index("D")
                    self.lista.pop(oponente)
                    self.lista.append("R")
                    self.lista.pop(0)
                else:
                    tem_resultado = True
                    print("Radiant")
            elif self.lista[0] == "D":
                if "R" in self.lista:
                    oponente = self.lista.index("R")
                    self.lista.pop(oponente)
                    self.lista.append("D")
                    self.lista.pop(0)
                else:
                    tem_resultado = True
                    print("Dire")


dota2 = Senado_Dota2()

dota2.recebe_string_inicial("RDRDRDD")
dota2.calcula_resultado()

