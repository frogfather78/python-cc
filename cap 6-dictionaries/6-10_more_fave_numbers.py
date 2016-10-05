#6-10 fave numbers

#a dictionary about how strange folk can be

fave_numbers = {
	"boris": [10, 17],
	"cheryl": [666],
	"theo": [-9,-8,-6],
	"horanen": [5],
	"bert": [5,800]
	}

for name, numbers in fave_numbers.items():
	print(name.title() + "'s favourite numbers are:\n")
	for number in numbers:
		print(str(number))
	print("\n")
