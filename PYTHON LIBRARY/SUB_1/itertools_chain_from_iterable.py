#!usr/bin/env/python3


# If the iterables to be combined are not all known in advance, or if they need to be
# evaluated lazily, chain.from_iterable() can be used to construct the chain instead.


from itertools import *

def make_iterables_to_chain():
	yield [1, 2, 3]
	yield ['a', 'b', 'c']
for i in chain.from_iterable(make_iterables_to_chain()):
	print(i, end=' ')
print()


# for i in zip([1, 2, 3], ['a', 'b', 'c']):
# 	print(i)


