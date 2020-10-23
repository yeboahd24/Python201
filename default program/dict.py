"""Prefer defaultdict Over setdefault to handle missing items in internal state"""

visits = {
	'Mexico': {'Tulum', 'Puerto', 'Vallarta'},
	'Japan': {'Hakone'},
}

# using setdefault method to add new cities to the sets
# this can be done with wether get or setdefault
# I can use the setdefault method to add new cities to the sets, whether the country name exist or not

visits.setdefault('France', set()).add('Arles') # short

if (japan := visits.get('Japan')) is None: # long
	visits['Japan'] = japan = set()
japan.add('Kyoto')

# print(visits)


"""Dynamically accessing inner state stored in a dictionary"""

class Visits:
	"""This makes all values set to set()"""
	def __init__(self):
		self.data = {}

	def add(self,country, city):
		city_set = self.data.setdefault(country, set())
		city_set.add(city)

visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
# print(visits.data)



# Using collection module to archive the same results
# I advice that you choose defaultdict over setdefault
from collections import defaultdict
class Visits:
	def __init__(self):
		self.data = defaultdict(set)

	def add(self,country, city):
		self.data[country].add(city)

visits = Visits()
visits.add('Russia', 'Yekaterinburg')
visits.add('Tanzania', 'Zanzibar')
print(visits.data)



# Defining your own dictionary

"""This program manage social network profile pictures
	pictures on the filesytem
"""
class Pictures(dict):
	def __missing__(self, key):
		value = open_pictures(key)
		self[key] = value
		return value
pictures = Pictures()
handle = pictures[path]
handle.seek(0)
image_data = handle.read()
