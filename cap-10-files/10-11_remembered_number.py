#10-11 i got your number

import json

f_name = "fave_number.json"

with open(f_name) as f_obj:
	number = json.load(f_obj)
	
	if number:
		print("Your favourite number is " + str(number))
	else:
		print("You need to tell me what your favourite number is")
