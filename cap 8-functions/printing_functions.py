def print_models(unprinted_designs, completed_models):
	"""simulate printing each design until none left
	move each design to completed after printing"""
	
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#simulate creating a 3d print
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""show all models that were printed"""
	print("\nThe following models were printed:")
	for completed_model in completed_models:
		print(completed_model)

