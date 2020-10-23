text = "It was the best of times, it was the blurst of times"
words = "i the it a time times was as best worst take of off point points for that yes no maybe banana error won't"


def spellCheck(text, words):   
	missingValues = set()
	splitWords = words.split()
	for i in splitWords:
		if i not in text:
			missingValues.add(i)
	return missingValues
			 

print(spellCheck(text, words))


