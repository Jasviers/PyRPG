from criatura import Criatura


class Guerrero(Criatura):
    furia = 0
    nombre = ""

    def __init__(self, HP, ATK, DEF, furia, nombre):
        Criatura.__init__(self, HP, ATK, DEF)
        self.furia = furia
        self.nombre = nombre

    def ataqueEspecial(self, criatura_atacada):
        if self.furia > 0:
            criatura_atacada.atacado(self.ATK*1.5)
        else:
            criatura_atacada.atacado(self.ATK)
