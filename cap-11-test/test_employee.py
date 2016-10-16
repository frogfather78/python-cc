import unittest

from employees import Employee

class TestEmployee(unittest.TestCase):
	"""tests for Employee"""

	def setUp(self):
		self.an_employee = Employee('bob','cratchett', 5000)
		
	def test_give_raise_default(self):
		"""test give_raise with default value"""
		self.an_employee.give_raise()
		self.assertEqual(self.an_employee.annual_salary, 10000)
		
	def test_give_custom_raise(self):
		"""test give_raise of £1 #tight"""
		self.an_employee.give_raise(1)
		self.assertEqual(self.an_employee.annual_salary, 5001)

unittest.main()
