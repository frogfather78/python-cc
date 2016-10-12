#9-3 user profiles
#again
#9-5 login attempts
#9-7 admin & 9-8 privileges class

class User():
	"""modeling a user of a something"""
	
	def __init__(self,first,last,uid):
		self.first_name = first
		self.last_name = last
		self.user_id = uid
		self.login_attempts = 0
	
	def describe_user(self):
		print(self.first_name.title() + " " + self.last_name.title() +
			" is a user of this thing.")
		print(str(self.user_id) + " is the user's ID no.")
	
	def greet_user(self):
		print("Hey, " + self.first_name.title() + "! Welcome.")
		print("You have attempted " + str(self.login_attempts) +
			" logins to this thing.")
		
	def increment_login_attempts(self):
		self.login_attempts += 1
	
	def reset_login_attempts(self):
		self.login_attempts = 0 
	
class Admin(User):
	"""has special skills"""
	def __init__(self,first,last,uid,privileges):
		super().__init__(first,last,uid)
		self.privileges = Privileges(privileges)

class Privileges():
	"""what skills"""
	def __init__(self,privileges):
		self.privileges = privileges
	def list_privileges(self):
		
		for privilege in self.privileges:
			print(" - " + privilege)
			

bert = User("bert", "welch", 1)

ernie = User("ernie", "butter", 45)

user_x = Admin("bottle", "washer", 96
	, ['*can ban users*', '*can reset login count*'])


#
#bert.describe_user()

#ernie.greet_user()
#ernie.describe_user()

#ernie.increment_login_attempts()
#ernie.increment_login_attempts()
#ernie.increment_login_attempts() #3

#ernie.greet_user()

#ernie.reset_login_attempts()

#print("Reset Ernie's login attempts")
ernie.greet_user()

user_x.greet_user()
user_x.privileges.list_privileges()
