#10-10 common words

filename = 'moby_dick.txt'

with open(filename) as f_object:
	content = f_object.read()
	
print(len(content))

while True:
	query = input("Which word? ")
	if query.lower() == "q":
		break
	else:
		total = content.lower().count(query)
		print("The word " + query + " appears in " + filename +
			" " + str(total) + " times.")

