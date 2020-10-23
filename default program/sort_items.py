from operator import itemgetter

PEOPLE = [
	{'first': 'Reuven', 'last': 'Lerner', 'email': 'reuven@lerner.co.il'},
	{'first': 'Donald', 'last': 'Trump', 'email': 'president@whitehouse.gov'},
	{'first': 'Akuffo', 'last': 'Addo', 'email': 'president@Ghana.gov'},

]


def sort_people(d):
	"""Sort people base on their first and last name"""
	return d['first'], d['last']
# print(sorted(PEOPLE, key=sort_people))


first = itemgetter('first')  # using itemgetter to get the same thing

print(sorted(PEOPLE, key=first))

