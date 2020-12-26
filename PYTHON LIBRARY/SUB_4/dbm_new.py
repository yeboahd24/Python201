# The open() function takes flags to control how the database file is managed. To create a
# new database when necessary, use 'c'. Using 'n' always creates a new database, overwriting
# an existing file.


import dbm
# with dbm.open('/tmp/example.db', 'n') as db:
# 	db['key'] = 'value'
# 	db['today'] = 'Sunday'
# 	db['author'] = 'Doug'
# print(dbm.whichdb('/tmp/example.db'))


with dbm.open('/tmp/example.db', 'r') as db:
	print('keys():', db.keys())
	for k in db.keys():
		print('iterating:', k, db[k])
	print('db["author"] =', db['author'])