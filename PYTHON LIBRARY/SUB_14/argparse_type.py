# argparse treats all argument values as strings, unless it is told to convert the string to
# another type. The type parameter to add_argument() defines a converter function, which
# the ArgumentParser uses to transform the argument value from a string to some other type.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', type=int)
parser.add_argument('-f', type=float)
parser.add_argument('--file', type=open)
try:
	print(parser.parse_args())
except IOError as msg:
	parser.error(str(msg))