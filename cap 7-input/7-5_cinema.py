#7-5 cinema tickets

still_here=True

while still_here:
	age = input("How old are you? ")
	if age == "quit":
		break
	else:
		age = int(age)
		if age < 3:
			print("You're a bit young to be buying a cinema ticket. " +
			"It's on the house.")
		elif age < 12:
			print("$10 for you, and no naughty films.")
		else:
			print("Full price: $15. Yes, for one film.")
			
