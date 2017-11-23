from criatura import Criatura


class Monstruo(Criatura):
    nombre = ""

    def __init__(self, HP, ATK, DEF, nombre):
        Criatura.__init__(self, HP, ATK, DEF)
        self.nombre = nombre
