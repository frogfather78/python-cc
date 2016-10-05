#6-6 polling

favourite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil':'python',
	}
	
pollees = ['phil', 'horace', 'gavin', 'edward']

for pollee in pollees:
	if pollee in favourite_languages:
		print("Thanks for taking the survey, " + pollee.title())
	else:
		print(pollee.title() + " you should tell me your fave language.")
		
