from criatura import Criatura


class MedusaHead(Criatura):

    
    def __init__(self, health, power, defense, speed):
        Criatura.__init__(self, health, power, defense)
        self.speed = speed
