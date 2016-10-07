#8-13 user_profile

def build_profile(first, last, **user_info):
	"""Build a dictionary about a user"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for k, v in user_info.items():
		profile[k] = v
		
	return profile
	

user_profile = build_profile('Phil', 'Oakes',
				occupation = 'publisher',
				hobby = 'drinking',
				age = 37)
				
profile2 = build_profile('Dave', 'Lister',
				occupation = 'bum',
				age = 25,
				favourite_food = 'curry')

print(user_profile)
print(profile2)

print(profile2['age'])
