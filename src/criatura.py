class Criatura(object):

        def __init__(self,  HP=100, ATK=30, DEF=10, expGiven=10):
            self.HP = HP
            self.totalHP = HP
            self.ATK = ATK
            self.DEF = DEF
            self.vivo = True
            self.expGiven = expGiven

        def atacar(self, criatura_atacada):
                criatura_atacada.atacado(self.ATK)

        def mostrarHP(self):
                print(self.HP + "/" + self.totalHP)

        def atacado(self, ATK):
                self.HP -= self.ATK - self.DEF
                if(self.HP < 0):
                        self.HP = 0
                        self.vivo = False
                        print("No le pegues más, que ya está muerto!")
