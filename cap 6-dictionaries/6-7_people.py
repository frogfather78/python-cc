#6-7 people

#a dictionary about more than one person

person_0 = {
	"last_name": "Hughes",
	"first_name": "Ass",
	"city": "Los Angeles",
	"phone_no": "555-7634"
	}
	

person_1 = {
	"last_name": "Fox",
	"first_name": "Cockless",
	"city": "London",
	"phone_no": "0207444555"
	}
	

person_2 = {
	"last_name": "Bum",
	"first_name": "Graeme",
	"city": "Hong Kong",
	"phone_no": "555-1234"
	}

people = [person_0, person_1, person_2]

for new_person in people:

	print("Name: " +
		new_person["first_name"] + " " +
		new_person["last_name"] + ".")

	print("Call: " +
		new_person["city"] + " " +
		new_person["phone_no"] +
		" for a good time, yo.")
		
	print("\n")
