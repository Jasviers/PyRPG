import criatura


class Monstruo(criatura.Criatura):
    def __init__(self, HP, HPTotal, ATK, DEF, Nombre):
        criatura.Criatura(HP, HPTotal, ATK, DEF)
        self.Nombre = Nombre
