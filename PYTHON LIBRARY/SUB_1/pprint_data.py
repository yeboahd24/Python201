#!usr/bin/env/python3
from pprint import pprint
import logging
from pprint import pformat

#To format a data structure without writing it directly to a stream (for example, for logging),
#use pformat() to build a string representation

data = [
	(1, {'a': 'A', 'b': 'B', 'c': 'C', 'd': 'D'}),
	(2, {'e': 'E', 'f': 'F', 'g': 'G', 'h': 'H',
	'i': 'I', 'j': 'J', 'k': 'K', 'l': 'L'}),
	(3, ['m', 'n']),
	(4, ['o', 'p', 'q']),
	(5, ['r', 's', 't''u', 'v', 'x', 'y', 'z']),
]

# pprint(data)



logging.basicConfig(
		level=logging.DEBUG,
		format='%(levelname)-8s %(message)s',
)

logging.debug('Logging pformatted data')
formatted = pformat(data)
for line in formatted.splitlines():
	logging.debug(line.rstrip())
