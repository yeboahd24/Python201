
# The starmap() function is similar to map(), but instead of constructing a tuple from
# multiple iterators, it splits up the items in a single iterator as arguments to the mapping
# function using the * syntax


from itertools import *

values = [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9)]
for i in starmap(lambda x, y: (x, y, x * y), values):
	print('{} * {} = {}'.format(*i))


# The cycle() function returns an iterator that repeats the contents of the arguments it
# is given indefinitely. Because it has to remember the entire contents of the input iterator,
# it may consume quite a bit of memory if the iterator is long.


for i in zip(range(7), cycle(['a', 'b', 'c'])):
	print(i)


# The repeat() function returns an iterator that produces the same value each time it is
# accessed.

for i in repeat('over-and-over', 5):
	print(i)

for i in map(lambda x, y: (x, y, x * y), repeat(2), range(5)):
	print('{:d} * {:d} = {:d}'.format(*i))
