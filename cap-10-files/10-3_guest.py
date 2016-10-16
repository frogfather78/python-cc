#10-3 guest
#10-4 guestbook

get_names=True
guest_book =''

while get_names:
	guest_name = input("Please tell me who you are: ")
	if guest_name.lower() == 'quit':
		break
	else:
		guest_book += guest_name + "\n"

with open('guest_book.txt', 'w') as file_object:
	file_object.write(guest_book)
