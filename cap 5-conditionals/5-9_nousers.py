#5-9 hello admin redux

#users = ["Phil", "Thomas", "Amy", "Admin", "Corrine"]

users=[]

if users:
	for user in users:
		if user.lower() != "admin":
			print("Hello " + user + ", thanks for coming back")
		else:
			print("Hello Admin, would you like a status report?")
else:
	print("We need to find some users, ya plum")
	
