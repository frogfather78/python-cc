#9-14 dice

from random import randint

class Die():
	"""models a die with a set number of sides"""
	def __init__(self, sides):
		self.sides = sides
	
	def roll_die(self):
		n = randint(1, self.sides)
		print(str(n))

my_die = Die(6)

for n in range(0, 10):
	my_die.roll_die()

my_bigger_die = Die(10)
print("10-sided")

for n in range(0, 10):
	my_bigger_die.roll_die()


my_20_die = Die(20)
print("D20")
for n in range(0, 10):
	my_20_die.roll_die()
