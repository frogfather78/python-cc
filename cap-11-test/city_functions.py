#11-1 citycountry

def full_city_name(city, country, population=''):
	if population:
		full_name = city + ", " + country + " - pop: " + str(population)
	else:
		full_name = city + ", " + country
	return full_name.title()
	
