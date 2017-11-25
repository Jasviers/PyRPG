class Criatura(object):
	def __init__(self, HP, ATK, DEF):
		self.MaxHP = HP
		self.HP = HP
		self.ATK = ATK
		self.DEF = DEF

	def atacar(self, target):
		target.atacado(self.ATK);

	def atacado(self, AttackPoints):
		self.HP = self.HP - (AttackPoints - self.DEF)
		if(self.HP <= 0):
			self.morir()
		else:
			self.mostrarVida()

	def mostrarVida(self):
		print("Quedan {} puntos de vida de {} puntos posibles.".format(self.HP, self.MaxHP))

	def morir(self):
		self.HP = 0
		print("Este jugador está muerto.")
