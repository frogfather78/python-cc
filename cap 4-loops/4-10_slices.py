#4-10 slices

#pizzas=["Sloppy Guiseppe", "La Reine", "American Hot"]
#not slices of pizza

#range's third param is "add this to last value"
trips = list(range(3, 31, 3))


for n in trips:
	print(n)
	
print("The first three items in this list are ")
print(trips[:3])

print("Three items from the middle of the list are ")
print(trips[3:6])

print("The last three items of the list are ")
print(trips[-3:len(trips)])


