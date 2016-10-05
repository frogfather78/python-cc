#6-3 a glossary

#a dictionary about things

glossary = {
	"list []": "a collection of variables",
	"for": "a way to loop through things",
	".sorted()": "nothing to do with Es and whizz",
	"str()": "converts a variable into a string",
	".title()": "puts a string into title case",
	"in": "checks if a thing is contained in a list or like",
	"print()": "puts something on the screen",
	":" : "allows you to do a slice of a list",
	"range()": "start, end, step size"
	}

for key, value in glossary.items():
	print("\n" + key + ": " + value)
