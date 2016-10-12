#9-10 imported restaurant

import restaurant as rs


restaurant_0 = rs.Restaurant('morleys', 'chicken')

restaurant_1 = rs.Restaurant('golden grill', 'kebab')

restaurant_2 = rs.Restaurant('fat duck', 'fancy schmancy')

restaurant_0.describe_restaurant()
restaurant_2.describe_restaurant()


restaurant_1.set_number_served(19)

print(restaurant_1.number_served)

restaurant_1.increment_number_served(4)

print(restaurant_1.name.title() + " has served " + 
	str(restaurant_1.number_served) + " peeps today")
