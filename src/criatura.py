class Criatura(object):

    def __init__(self, atk, defen, hp, nombre):
        self.atk = atk
        self.defen = defen
        self.hp = hp
        self.__hpTotal = hp
        self.nombre = nombre

    def atacar(self, criatura):
        print("{} ataco a {}".format(self.nombre, criatura.nombre))
        criatura.atacado(self.atk)

    def atacado(self, atk):
        self.hp -= (atk - self.defen)
        print("{} ahora tiene {}HP de {}HP".format(self.nombre, self.hp, self.__hpTotal))

    def mostrarVida(self):
        print("Vida de {} = {}".format(self.nombre, self.hp))
