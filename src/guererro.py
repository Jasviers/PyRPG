import criatura

class Guerrero(criatura.Criatura):

    def __init__(self, HP, HPTotal, ATK, DEF, FU, experiencia, nivel, Nombre):
        criatura.Criatura(HP, HPTotal, ATK, DEF)
        self.FU         = FU
        self.expriencia = experiencia
        self.nivel      = nivel
        self.Nombre     = Nombre

    def ataqueEspecial(self, Criatura_Atacada):
        if self.FU <= 50:
            self.ataqueEspecial = criatura.Criatura.atacar
        else:
            self.ataqueEspecial =  1.5 * criatura.Criatura.atacar
        self.FU = 0

    def ganarFuria(self):
        if self.ATK > 0:
            self.FU += 10
        else:
            self.FU = self.FU

    def ganarExperiencia(self, Criatura_Atacada):
        if (Criatura_Atacada.HP == 0):
            self.experiencia += 3

    def ganarNiveles(self):
        if (self.experiencia == 9):
            self.nivel += 1
