#9-1 restaurant

class Restaurant():
	"""modeling a restaurant, kinda"""
	
	def __init__(self,name,cuisine):
		"""initialise some stuff"""
		self.name = name
		self.cuisine = cuisine
	
	def describe_restaurant(self):
		print("This place called " + self.name.title() +
			" serves cheap " + self.cuisine + " food.")
			
	def open_restuarant(self):
		print(self.name.title() + " is now open!")

restaurant_0 = Restaurant('morleys', 'chicken')

restaurant_1 = Restaurant('golden grill', 'kebab')

restaurant_2 = Restaurant('fat duck', 'fancy schmancy')

restaurant_0.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_1.describe_restaurant()


#restaurant.open_restuarant()

		
