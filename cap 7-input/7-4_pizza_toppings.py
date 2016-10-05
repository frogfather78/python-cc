#7-4 pizza toppings

pizza_toppings=[]

print("Welcome to Pizza Cave. What toppings you want?")

pizza=True

while pizza:
	topping = input("> ")
	
	if topping == "quit":
		break
	else:
		pizza_toppings.append(topping)
		print("Adding " + topping)

print(pizza_toppings)
