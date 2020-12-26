#!usr/bin/env/python3
# The islice() function returns an iterator that returns selected items from the input
# iterator, by index.
# islice() takes the same arguments as the slice operator for lists: start, stop, and step.
# The start and step arguments are optional.

from itertools import *
print('Stop at 5:')
for i in islice(range(100), 5):
	print(i, end=' ')
print('\n')

print('Start at 5, Stop at 10:')
for i in islice(range(100), 5, 10):
	print(i, end=' ')
print('\n')

print('By tens to 100:')
for i in islice(range(100), 0, 100, 10):
	print(i, end=' ')
print('\n')