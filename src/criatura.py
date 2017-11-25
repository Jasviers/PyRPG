from random import randint

class Criatura(object):
    def __init__(self, HP, HPTotal, ATK, DEF):
        self.HP = HP
        self.HPTotal = HP
        self.ATK = ATK
        self.DEF = DEF

    def atacar(self, Criatura_Atacada):
        Criatura_Atacada.HP = Criatura_Atacada.HP + (randint(0,Criatura_Atacada.DEF)) - (randint(0,self.ATK))

    def atacado(self, ataque_recibido):
        self.HP = self.HP + randint(0,self.DEF) - randint(0,ataque_recibido)

    def mostrarVida(self):
        print("Tienes {} de {} totales".format(self.HP, self.HPTotal))
