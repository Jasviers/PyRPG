from criatura import Criatura


class Monstruo(Criatura):
    def __init__(self, HP, ATK, DEF, Nombre):
        Criatura.__init__(self, HP, ATK, DEF)
        self.Nombre = Nombre
        self.presentarse()

    # Función definida por Paula
    def presentarse(self):
        print("Soy un MONSTRUOOOOOOO, AAAAAAAH")
