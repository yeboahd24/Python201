def detectCapitals(word):
	return word == word.upper() or word == word.lower() or word == word.capitalize()

print(detectCapitals('FlaG'))