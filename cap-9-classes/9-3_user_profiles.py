#9-3 user profiles
#again

class User():
	"""modeling a user of a something"""
	
	def __init__(self,first,last,uid):
		self.first_name = first
		self.last_name = last
		self.user_id = uid
	
	def describe_user(self):
		print(self.first_name.title() + " " + self.last_name.title() +
			" is a user of this thing.")
		print(str(self.user_id) + " is the user's ID no.")
	
	def greet_user(self):
		print("Hey, " + self.first_name.title() + "! Welcome.")
	
bert = User("bert", "welch", 1)

ernie = User("ernie", "butter", 45)

user_x = User("bottle", "washer", 96)

bert.describe_user()

ernie.greet_user()
ernie.describe_user()
user_x.greet_user()
