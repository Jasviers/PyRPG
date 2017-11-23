from criatura import Criatura


class Guerrero(Criatura):


    def __init__(self, health, power, defense, wrath, name):
        if (wrath <= 0 and wrath >= 100):
            raise TooAngryError("The wrath must be a value between 0 and 100 (included), but instead it received <%>", wrath)
        Criatura.__init__(self, health, power, defense)
        self.wrath = wrath
        self.name = name

    
class TooAngryError(Exception):
    

    def __init__(self, value, message):
        self.value = value
        self.message = message

