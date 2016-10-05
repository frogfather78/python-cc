#guest list exercise 3-5

guests = ["Buddha", "Lenin", "Scarlett Johansson"]

print("Hey, " + guests[0] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[1] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[2] + ". Fancy dinner, my place, say... 8pm?")

print("\nDang I guess " + guests[1] + " can't make it. :(")

guests[1] = "John Lennon"

print("Hey, " + guests[0] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[1] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[2] + ". Fancy dinner, my place, say... 8pm?")

print("\n\nWhaaaat? There's more space?!")

guests.insert(0, "Gary Lineker")

guests.insert(3, "Gary Glitter")

guests.append("Martin Luther")


print("Hey, " + guests[0] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[1] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[2] + ". Fancy dinner, my place, say... 8pm?")

print("Hey, " + guests[3] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[4] + ". Fancy dinner, my place, say... 8pm?")
print("Hey, " + guests[5] + ". Fancy dinner, my place, say... 8pm?")
