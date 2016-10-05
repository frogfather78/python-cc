#4-11 pizza party time

pizzas=["Sloppy Guiseppe", "La Reine", "American Hot"]

friend_pizzas=pizzas[:]

pizzas.append("Anchovy")

friend_pizzas.append("Spinach and Ricotta")

print("I like these:")
for pizza in pizzas:
	print(pizza)
	
print("\nMy friend likes:")
for pizza in friend_pizzas:
	print(pizza)
		
print("Y'all know I loves you all, pizzas")
