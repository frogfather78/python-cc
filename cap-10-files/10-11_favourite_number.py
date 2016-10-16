#10-11 favourite number

import json

f_name = "fave_number.json"

def ask_for_number():
	"""asks user for their favourite number
	stores it in f_name file"""
	
	fave_number = input("What's your favourite number? ")
	with open(f_name, 'w') as f_obj:
		json.dump(fave_number, f_obj)

def remember_number():
	try:
		with open(f_name) as f_obj:
			number = json.load(f_obj)
		
	except FileNotFoundError:
		return None
	else:
		return number

a = remember_number()
if a:
	print("Your favourite number was: " + str(a))
else:
	ask_for_number()

