from criatura import Criatura


class Monstruo(Criatura):
    def __init__(self, hp, hpTotal, atk, defe, nombre):
        Criatura.__init__(self, hp, hpTotal, atk, defe, nombre)
