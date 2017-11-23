class Criatura(object):
    
    
    def __init__(self, health, power, defense):
        self.health = health
        self.power = power
        self.defense = defense

    # def attack(self, target):

    def wounded(self, power):
        if (power > self.defense):
            self.health -= (power - self.defense)

    def show_health(self):
        print(self.health)
