#6-8 pets

#dictionaries about dogs (and other animals)

rusty = {
	"name": "rusty",	
	"animal": "cat",
	"food": "tuna",
	"owner": "ann",
	"age": 12
	}

monty = {
	"name": "monty",
	"animal": "dog",
	"food": "idiot biscuits",
	"owner": "michael",
	"age": 5
	}

albie = {
	"name": "albie",
	"animal": "dog",
	"food": "gripweed",
	"owner": "poppy",
	"age": 19
	}

pets = [rusty, monty, albie]

for pet in pets:
	print(pet["name"].title() + " is a " + pet["animal"] + ".")
	print("Its favourite food is " + pet["food"] + ".")
	print(pet["name"].title() + " is owned by " +
		pet["owner"].title() + " and is " + str(pet["age"]) +
		" years old.")
	print("\n")
