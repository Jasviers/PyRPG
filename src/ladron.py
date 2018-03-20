from criatura import Criatura

class Ladron(Criatura):

    def __init__(self,hp,hpTotal,atk,defe,fu,experiencia,nivel,nombre):
        Criatura.__init__(self,hp,hpTotal,atk,defe,nombre)
        self.experiencia = experiencia
        self.nivel = nivel
        self.fu = fu

    def ataqueEspecial(self,Criatura_Atacada):
        print("Alumno ha robado a Erviti!!!")
        print("Tu arma mejora en 1 punto al robar")
        print("")
        self.atk += 1
        Criatura_Atacada.atacado(self.atk)

    def ganarFuria(self):
        self.fu += 10

    def ganarExperiencia(self):
        self.experiencia += 3

    def ganarNiveles(self):
        if (self.experiencia == 6):
            self.nivel += 1
