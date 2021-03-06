#9-1 restaurant
#9-4 number served
#9-6 ice cream

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

class IceCreamStand(Restaurant):
	"""modelling a specific type of restaurant"""
	def __init__(self,name,cuisine,flavours):
		super().__init__(name,cuisine)
		self.flavours = flavours
	
	def list_flavours(self):
		for flavour in self.flavours:
			print(" -" + flavour.title())

restaurant_0 = Restaurant('morleys', 'chicken')

restaurant_1 = Restaurant('golden grill', 'kebab')

restaurant_2 = Restaurant('fat duck', 'fancy schmancy')

restaurant_0.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_1.describe_restaurant()

restaurant_1.set_number_served(5)

print(restaurant_1.number_served)


restaurant_1.set_number_served(19)

print(restaurant_1.number_served)

restaurant_1.increment_number_served(4)

print(restaurant_1.name.title() + " has served " + 
	str(restaurant_1.number_served) + " peeps today")
#restaurant.open_restuarant()


icecreamstand_1 = IceCreamStand('jen & bennys', 'ice cream',
		['mint choc', 'vanilla', 'straw'])
		
icecreamstand_1.describe_restaurant()
icecreamstand_1.list_flavours()
