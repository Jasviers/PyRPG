from criatura import Criatura

class PrincipeMutante(Criatura):

    def __init__(self, atk, defen, hp, nombre):
        Criatura.__init__(self,atk,defen,hp,nombre)
