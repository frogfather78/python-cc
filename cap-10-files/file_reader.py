filename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

pi_string = ''

for line in lines:		
	pi_string += line.strip()

#print(pi_string[:52] + '...')

birthday = input("Enter birthday as ddmmyy: ")

if birthday in pi_string:
	print("Your birthday is in the first million digits of pi")
else:
	print("your birthday does not appear in the first million digits of pi")


