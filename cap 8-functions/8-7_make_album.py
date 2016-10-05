#8-7 i'm a music producer

def make_album(title, artist, track_count=''):
	"""returns dictionary of a music album"""
	album = {"title": title.title(), "artist": artist.title()}
	if track_count:
		album["track_count"] = track_count
	return album

a1 = make_album("man who sold the world", "david bowie", 8)

a2= make_album("Harvest", "neil young")

a3= make_album("different class", "pulp")

albums = [a1, a2, a3]

get_albums = True
print("I'm going to ask you for some album titles. Enter quit to stop.")

while get_albums:
	user_title = input("Album title> ")
	if user_title == "quit":
		break
	else:
		user_artist = input("Album artist> ")
		if user_artist == "quit":
			break
		else:
			albums.append(make_album(user_title, user_artist))


for album in albums:
	print(album)
