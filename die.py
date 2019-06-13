from random import randint 

class Die():
	def __init__(self,num_sides = 6):
		self.num_sides = num_sides


	##Note in __init__	we set num_sides = 6, for a regular die
	def roll(self):
		return randint(1, self.num_sides)



