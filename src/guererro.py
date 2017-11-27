import criatura

class Guerrero(criatura.Criatura):

    def __init__(self, hp, hpTotal, atk, defe, fu, experiencia, nivel, nombre):
        criatura.Criatura(hp, hpTotal, atk, defe, nombre)
        self.fu         = fu
        self.experiencia = experiencia
        self.nivel      = nivel

    def ataqueEspecial(self, Criatura_Atacada):
        if self.fu <= 30:
            self.ataqueEspecial = criatura.Criatura.atacar
        else:
            self.ataqueEspecial =  1.5 * criatura.Criatura.atacar
        self.fu = 0

    def ganarFuria(self):
        if self.atk > 0:
            self.fu += 10
        else:
            self.fu = self.fu

    def ganarExperiencia(self, Criatura_Atacada):
        if (Criatura_Atacada.hp == 0):
            self.experiencia += 3

    def ganarNiveles(self):
        if (self.experiencia == 9):
            self.nivel += 1
