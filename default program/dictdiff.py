def dictdiff(first, second):
	"""Compare if two dictionaries are the same"""
	output = {}
	all_keys = first.keys() | second.keys()

	for key in all_keys:
		if first.get(key)!= second.get(key):
			output[key] = [first.get(key), second.get(key)] # storing the values as list
	return output


d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'a': 1, 'b': 2, 'c': 4}

print(dictdiff(d1, d2))