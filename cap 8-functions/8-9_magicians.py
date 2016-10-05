#8-9 magicians

magicians = ["marvelloso", "harry potter", "bob", 'lemmy']

def show_magicians(magicians):
	for magician in magicians:
		print(magician.title())

def make_great(magicians):
	numbers = list(range(0, len(magicians)))
	for i in numbers:
		magicians[i] = "The Great " + magicians[i].title()
	return magicians



the_greats = make_great(magicians[:])

show_magicians(magicians)

print("The Great Ones")

show_magicians(the_greats)
