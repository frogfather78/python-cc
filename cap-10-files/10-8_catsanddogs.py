#10-8 cats and dogs

filenames = ['cats.txt', 'dogs.txt']

content = ''

for f_name in filenames:
	try:
		with open(f_name) as f_object:
			lines = f_object.readlines()
			content += str(lines)

	except FileNotFoundError:
		pass
		#print("Can't find " + f_name)

print(content)				
		
