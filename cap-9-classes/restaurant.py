
class Restaurant():
	"""modeling a restaurant, kinda"""
	
	def __init__(self,name,cuisine):
		"""initialise some stuff"""
		self.name = name
		self.cuisine = cuisine
		self.number_served = 0
	
	def describe_restaurant(self):
		print("This place called " + self.name.title() +
			" serves cheap " + self.cuisine + " food.")
			
	def open_restuarant(self):
		print(self.name.title() + " is now open!")
		
	def set_number_served(self, number_served):
		self.number_served = number_served
		
	def increment_number_served(self, increment):
		self.number_served += increment
