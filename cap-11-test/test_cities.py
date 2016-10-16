
import unittest

from city_functions import full_city_name

class CityNameTest(unittest.TestCase):
	"""tests for city_functions"""
	
	def test_full_city_name(self):
		"""output of full_city_name with city, country"""
		formatted_name = full_city_name('santiago', 'chile')
		self.assertEqual(formatted_name, 'Santiago, Chile')	

	def test_full_city_name_pop(self):
		"""output of full_city_name with
		city, country, population"""
		formatted_name = full_city_name('paris', 'France', 9000000)
		self.assertEqual(formatted_name, 'Paris, France - Pop: 9000000')
		
unittest.main()
