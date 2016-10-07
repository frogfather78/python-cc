#8-12 sammiches

def build_sandwich(*fillings):
	"""it prints what kind of sandwich you like"""
	print("\nI made you a sammich full of:")
	for filling in fillings:
		print(" -" + filling)
	

build_sandwich("crisps")

build_sandwich("ham", "bacon", "prosciutto")

build_sandwich("chicken", "avocado")

