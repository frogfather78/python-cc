#all of the list functions

buildings = ["Shard", "St. Paul's", "Gherkin", "Cheesegrater", "Eye"]

print(len(buildings))

print(sorted(buildings))

buildings.sort(reverse=True)

#demolish one building
demolish = buildings.pop()
print("Kaboom")
print(demolish)

print(buildings)

#destroy another building
print("BOOM again")
del(buildings[2])

print(buildings)

#build something new
print("Building a new building")
buildings.append("Tower Bridge")


buildings.sort()

print("Second building is " + buildings[1])
print(buildings)

#build something else new
print("Inserting something")
buildings.insert(2, "Tower 42")

print(buildings)
