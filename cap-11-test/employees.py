
class Employee():
	"""models employee data"""
	def __init__(self, first, last, salary):
		self.first_name = first
		self.last_name = last
		self.annual_salary = salary
		
	def give_raise(self, increment=5000):
		self.annual_salary += increment
		

