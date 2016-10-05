#7-8 deli

#making sarnies

sandwich_orders = ["ham on rye", "cheese and pickle", "crisps"]

finished_orders = []

while sandwich_orders:
	current_sarnie = sandwich_orders.pop()
	finished_orders.append(current_sarnie)
	print("Making a " + current_sarnie + " sammich.")

print(finished_orders)
