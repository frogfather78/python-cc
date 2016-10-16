#10-6 addition

print("I will add numbers for your lazy brain")
print("Enter q to quit")

while True:
	a = input("Enter a number: ")
	if a == "q":
		break
	else:
		b = input("Enter a second number: ")
		if b == "q":
			break
		else:
			try:
				result = int(a)+int(b)				
			except ValueError:
				print("I'm only adding integers here, bub")
			else:
				print(str(result))
