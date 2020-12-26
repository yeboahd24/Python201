# #!usr/bin/env/python3

# The built-in map() function returns an iterator that calls a function on the values in the
# input iterators, and returns the results. It stops when any input iterator is exhausted.
from itertools import *

def times_two(x):
	return 2 * x

def multiply(x, y):
	return (x, y, x * y)

# print('Doubles:')
# for i in map(times_two, range(5)):
# 	print(i)

# print('\nMultiples:')
# r1 = range(5)
# r2 = range(5, 10)
# for i in map(multiply, r1, r2):
# 	print('{:d} * {:d} = {:d}'.format(*i))

# print('\nStopping:')
# r1 = range(5)
# r2 = range(2)
# for i in map(multiply, r1, r2):
# 	print(i)


r1 = range(int(input('range: ')))
print('\nMultiples')
for i in map(lambda x, y: (x, y, x * y), repeat(2), r1):
	print('{:d} * {:d} = {:d}'.format(*i))
