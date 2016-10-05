#5-11 listing ordinal numbers

#create a list from 1 to 9
numbers = list(range(1, 10))


for number in numbers:
	if number == 1:
		ordinal = "st"
	elif number == 2:
		ordinal = "nd"
	elif number == 3:
		ordinal = "rd"
	else:
		ordinal = "th"
	print(str(number) + ordinal)


	
