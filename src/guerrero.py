from criatura import Criatura


class Guerrero(Criatura):
    def __init__(self, HP, ATK, DEF, furia, nombre):
        Criatura.__init__(self, HP, ATK, DEF)
        self.furia = furia
        if(furia < 0 || furia > 100):
            raise Error("La furia debe de ser menor de 100!")
        self.nombre = nombre
        self.nivel = 1
        self.siguienteNivel

    def ataqueEspecial(self, criatura_atacada):
        if self.furia > 0:
            criatura_atacada.atacado(self.ATK*1.5)
        else:
            criatura_atacada.atacado(self.ATK)
        if !criatura_atacada.vivo:
            print("Enhorabuena, has matado a " + criatura_atacada.nombre)

    def ganarFuria(self):
        # Cada turno la furia aumenta según la que tengas
        self.furia = self.furia*1.5

    def atacar(self, criatura_atacada):
        Criatura.atacar(self, criatura_atacada.vivo)
        if(!criatura_atacada.vivo):
            self.siguienteNivel -= criatura_atacada.expGiven
        if(self.siguienteNivel <= 0):
            self.nivel++
            print("Enhorabuena! Has subido al nivel " + nivel)
            self.siguienteNivel = nivel * 100 + self.siguienteNivel
