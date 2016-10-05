#6-5 rivers

#a dictionary about rivers

glossary = {
	"nile": "egypt",
	"danube": "germany",
	"dee": "scotland"	
	}

for key, value in glossary.items():
	print("\nThe river " + key.title() + 
	" flows though " + value.title() + ". IT'S TRUE!")

print(" ") # make some space

for key in glossary.keys():
	print(key.title())

print(" ") # make some space

for value in glossary.values():
	print(value.title())
