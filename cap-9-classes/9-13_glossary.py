#6-3 a glossary
#9-13 rewritten to stay in order 
#a dictionary about things

from collections import OrderedDict



glossary = OrderedDict()

glossary["list []"] = "a collection of variables"
glossary["for"]= "a way to loop through things"
glossary[".sorted()"]= "nothing to do with Es and whizz"
glossary["str()"]= "converts a variable into a string"
glossary[".title()"]= "puts a string into title case"
glossary["in"]= "checks if a thing is contained in a list or like"
glossary["print()"]= "puts something on the screen"
glossary[":"]= "allows you to do a slice of a list"
glossary["range()"]= "start, end, step size"


for key, value in glossary.items():
	print("\n" + key + ": " + value)
