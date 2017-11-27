import criatura


class Monstruo(criatura.Criatura):
    def __init__(self, hp, hpTotal, atk, defe, nombre):
        criatura.Criatura(hp, hpTotal, atk, defe, nombre)
