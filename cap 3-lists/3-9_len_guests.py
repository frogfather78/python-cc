#guest list exercise 3-9
#mucking about with len()

guests = ["Buddha", "Lenin", "Scarlett Johansson"]

print("Hey, " + guests[0] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[1] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[2] + ". Fancy dinner, my place, say... 8pm?")

print(len(guests))

print("\nDang I guess " + guests[1] + " can't make it. :(")

guests[1] = "John Lennon"

print("Hey, " + guests[0] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[1] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[2] + ". Fancy dinner, my place, say... 8pm?")

print("\n\nWhaaaat? There's more space?!")
print(len(guests))

guests.insert(0, "Gary Lineker")

guests.insert(3, "Gary Glitter")

guests.append("Martin Luther")


print("Hey, " + guests[0] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[1] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[2] + ". Fancy dinner, my place, say... 8pm?")

print("Hey, " + guests[3] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[4] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[5] + ". Fancy dinner, my place, say... 8pm?")
print(len(guests))

print("\n\nOh, there *isn't* more space. Only two people can come.")

jake1 = guests.pop()
print(jake1 + " you can't come.")

jake2 = guests.pop()
print(jake2 + " you can't come.")

jake3 = guests.pop()
print(jake3 + " you can't come.")

jake4 = guests.pop()
print(jake4 + " you can't come.")

print(guests[0] + " you're still welcome.")
print("And you, " + guests[1] + ", if you want.")
print(len(guests))

del guests[1]
del guests[0]

print(guests)
print(len(guests))
