import criatura

class Guerrero(criatura.Criatura):

    def __init__(self, HP, ATK, DEF, FU, Nombre):
        criatura.Criatura(self, HP, ATK, DEF)
        self.FU     = FU
        self.Nombre = Nombre

    def ataqueEspecial(self, Criatura_Atacada):
        if self.FU <= 50:
            self.ataqueEspecial = self.ATK
        else:
            self.ataqueEspecial = 1.5 * self.ATK

        self.FU = 0

    def ganarFuria(self):
        if self.ATK >= 3:
            self.FU += 2
        else:
            self.FU = self.FU
