# see the world exercise 3-8

places = ["Egypt", "Belgium", "Cape Town", "Alaska", "Dunkirk"]

print(places)

print("In order")
print(sorted(places) )

print("Original")
print(places)

print("Reverse order")
print(sorted(places, reverse=True) )

places.reverse()
print("Reversed")
print(places)

places.sort()
print("Alphabetical")
print(places)

places.sort(reverse=True)
print("Reverse alphabetical")
print(places)

