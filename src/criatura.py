from random import randint

class Criatura(object):
    def __init__(self, HP, HPTotal, ATK, DEF):
        self.HP = HP
        self.HPTotal = HP
        self.ATK = ATK
        self.DEF = DEF

    def atacar(self, Criatura_Atacada):
        dañoAtacar = (randint(0,self.ATK)) - (randint(0,Criatura_Atacada.DEF))
        if daño >= 0:
            Criatura_Atacada.HP = Criatura_Atacada.HP - dañoAtacar
            print("A la criatura le quedan {}".format(Criatura_Atacada.HP))
        else:
            Criatuta_Atacada.HP = Criatura_Atacada.HP
            print("Has fallado el ataque")

    def atacado(self, ataque_recibido):
        dañoAtacadao = (randint(0,ataque_recibido)) - (randint(0,self.DEF))
        if dañoAtacado >= 0:
            self.HP = self.HP - dañoAtacado
            self.mostrarVida()
        else:
            self.HP = self.HP
            print ("Tu enemigo ha fallado el ataque")

    def mostrarVida(self):
        print("Tienes {} de {} totales".format(self.HP, self.HPTotal))
