# The simplest way to use shelve is via the DbfilenameShelf class. It uses dbm  to
# store the data. The class can be used either directly or by calling shelve.open().


import shelve
with shelve.open('test_shelf.db') as s:
	s['key1'] = {
		'int': 10,
		'float': 9.5,
		'string': 'Sample data',
}