class Criatura(object):
        HP = 0
        ATK = 0
        DEF = 0

        def __init__(self,  HP, ATK, DEF):
            self.HP = HP
            self.ATK = ATK
            self.DEF = DEF

        def atacar(self, criatura_atacada):
                criatura_atacada.atacado(self.ATK)

        def mostrarHP(self):
                print(self.HP)

        def atacado(self, ATK):
                self.HP -= self.ATK - self.DEF
