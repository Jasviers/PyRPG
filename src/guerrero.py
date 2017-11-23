from criatura import Criatura

class Guerrero(Criatura):

    def __init__(self, atk, defen, hp, nombre):
        Criatura.__init__(self,atk,defen,hp, nombre)
        self.furia = 0

    def atacar(self, criatura):
        print("{} ataco a {}".format(self.nombre, criatura.nombre))
        criatura.atacado(self.atk)
        if self.furia <= 100:
            self.furia += 20 if self.furia+20 <= 100 else 100-self.furia

    def ataque_especial(self, criatura):
        if self.furia>=40:
            self.furia-=40
            criatura.atacado(self.atk*1.5)
        print("No tiene suficiente furia, ataco de forma normal.")
        self.atacar(criatura)
