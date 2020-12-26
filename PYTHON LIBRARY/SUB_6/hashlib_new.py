# Sometimes it is more convenient to refer to the algorithm by giving its name in a string
# rather than by using the constructor function directly. It is useful, for example, to be able
# to store the hash type in a configuration file. In those cases, use new() to create a hash
# calculator.


import argparse
import hashlib
import sys
from hashlib_data import lorem
parser = argparse.ArgumentParser('hashlib demo')
parser.add_argument(
	'hash_name',
	choices=hashlib.algorithms_available,
	help='the name of the hash algorithm to use',
)


parser.add_argument(
	'data',
	nargs='?',
	default=lorem,
	help='the input data to hash, defaults to lorem ipsum',
)


args = parser.parse_args()
h = hashlib.new(args.hash_name)
h.update(args.data.encode('utf-8'))
print(h.hexdigest())