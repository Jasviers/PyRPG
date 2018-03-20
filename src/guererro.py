from criatura import Criatura


class Guerrero(Criatura):

    def __init__(self, hp, hpTotal, atk, defe, fu, experiencia, nivel, nombre):
        Criatura.__init__(self, hp, hpTotal, atk, defe, nombre)
        self.fu          = fu
        self.experiencia = experiencia
        self.nivel       = nivel

    def ataqueEspecial(self, Criatura_Atacada):
        if self.fu < 30:
            self.atacar(Criatura_Atacada)
        else:
            Criatura_Atacada.atacado(self.atk)
        self.fu = 0

    def ganarFuria(self):
        self.fu += 10

    def ganarExperiencia(self):
        self.experiencia += 3

    def ganarNiveles(self):
        if (self.experiencia == 6):
            self.nivel += 1
