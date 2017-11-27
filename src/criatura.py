from random import randint

class Criatura(object):
    def __init__(self, hp, hpTotal, atk, defe):
        self.hp = hp
        self.hpTotal = hp
        self.atk = atk
        self.defe = defe
        self.nombre = nombre

    def atacar(self, Criatura_Atacada):
        dañoAtacar = (randint(0,self.atk)) - (randint(0,Criatura_Atacada.defe))
        if dañoAtacar >= 0:
            Criatura_Atacada.hp = Criatura_Atacada.hp - dañoAtacar
            print("A la criatura le quedan {}".format(Criatura_Atacada.hp))
        else:
            Criatuta_Atacada.hp = Criatura_Atacada.hp
            print("Has fallado el ataque")

    def atacado(self, ataque_recibido):
        dañoAtacadao = (randint(0,ataque_recibido)) - (randint(0,self.defe))
        if dañoAtacado >= 0:
            self.hp = self.hp - dañoAtacado
            self.mostrarVida()
        else:
            self.hp = self.hp
            print ("Tu enemigo ha fallado el ataque")

    def mostrarVida(self):
        print("Tienes {} de {} totales".format(self.hp, self.hpTotal))
