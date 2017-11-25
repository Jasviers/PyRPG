from criatura import Criatura


class Guerrero(Criatura):
    def __init__(self, HP, ATK, DEF, Furia, FuriaXAtaque, Nombre):
        Criatura.__init__(self, HP, ATK, DEF)
        self.Furia = Furia
        self.Nombre = Nombre
        self.FuriaXAtaque = FuriaXAtaque
        self.presentarse()

    # Función definida por Paula
    def presentarse(self):
        print("Yo soy un GUERRERO y te voy a MATAAAAAR")

    def ataqueEspecial(self, target):
        if(self.Furia < self.FuriaXAtaque):
            print("No tienes suficiente furia ({}). Así que atacas normal:".format(self.Furia))
            self.atacar(target)
        else:
            target.atacado(self.ATK * 1.5)
