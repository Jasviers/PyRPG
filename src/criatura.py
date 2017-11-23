class Criatura(object):
    def __init__(self, HP, ATK, DEF):
        self.HP = HP
        self.ATK = ATK
        self.DEF = DEF
        self.HPTotal = HP

    def atacar(self, Criatura_Atacada):
        monstruo.HP = monstruo.HP - self.ATK + monstruo.DEF

    def atacado(self, ataque):
        self.HP = self.HP - monstruo.ATK - self.DEF

    def mostrarVida(self):
        print("Tienes" + self.HP + "puntos de vida de" + self.HPTotal + "totales")
