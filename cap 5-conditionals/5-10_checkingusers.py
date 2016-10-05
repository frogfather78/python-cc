#5-10 checking usernames

current_users = ["phil", "thomas", "amy", "barnes", "corrine"]

new_users = ["Amy", "Barnes", "Terence", "Spud Gun", "PHIL"]

for new_user in new_users:
	if new_user.lower() in current_users:
		print("Sorry, " + new_user + " already exists. Pick summat else")
	else:
		print("Hey! " + new_user + " is a fine username, bud.")
	
