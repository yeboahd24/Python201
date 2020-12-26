# The JSON format expects the keys to a dictionary to be strings. Trying to encode a dictionary with non-string types as keys produces a TypeError. One way to work around that
# limitation is to tell the encoder to skip over non-string keys using the skipkeys argument.

import json

data = [{'a': 'A', 'b': (2, 4), 'c': 3.0, ('d',): 'D tuple'}]
print('First attempt')
try:
	print(json.dumps(data))
except TypeError as err:
	print('ERROR:', err)
print()
print('Second attempt')
print(json.dumps(data, skipkeys=True))