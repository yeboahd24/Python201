# Although file objects can be instantiated with a single string argument, that does not
# include the access mode argument. FileType provides a more flexible way of specifying that
# an argument should be a file, including the mode and buffer size.

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('-i', metavar='in-file', type=argparse.FileType('rt'))
parser.add_argument('-o', metavar='out-file',
type=argparse.FileType('wt'))
try:
	results = parser.parse_args()
	print('Input file:', results.i)
	print('Output file:', results.o)
except IOError as msg:
	parser.error(str(msg))
