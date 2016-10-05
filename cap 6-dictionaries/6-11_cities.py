#6-11 cities

#a dictionary about a place or three

london = {
	"country": "united kingdom",
	"population": 7000000,
	"fact": "It sits on the river Thames"
	}

paris = {
	"country": "france",
	"population": 9000000,
	"fact": "It smells of wee"
	}
	
berlin = {
	"country": "germany",
	"population": 5000000,
	"fact": "David Bowie's 'Heroes' was recorded here"
	}
	
cities = {
	"london": london,
	"paris": paris, 
	"berlin": berlin
	}

for city, data in cities.items():
	print(city.title() +" is in " + data["country"].title() + ".")
	print("It's home to " + str(data["population"]) + " souls.")
	print(data["fact"])
		
		
