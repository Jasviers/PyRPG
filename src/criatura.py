import random as rd

class Criatura(object):
    def __init__(self, hp, hpTotal, atk, defe, nombre):
        self.hp = hp
        self.hpTotal = hp
        self.atk = atk
        self.defe = defe
        self.nombre = nombre

    def atacar(self, Criatura_Atacada):
        Criatura_Atacada.atacado(self.atk)

    def atacado(self, ataque_recibido):
        dañoAtacado = (rd.randint(0,ataque_recibido)) - (rd.randint(0,self.defe))
        if dañoAtacado > 0:
            self.hp = self.hp - dañoAtacado
            print("{} recibe daño".format(self.nombre))
        else:
            self.hp = self.hp
            print("{} esquiva el ataque".format(self.nombre))

    def mostrarVida(self):
        print("{} tiene {} puntos de vida de {} totales".format(self.nombre, self.hp, self.hpTotal))
