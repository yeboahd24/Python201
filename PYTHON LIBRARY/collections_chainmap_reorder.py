#!usr/bin/env/python3

import collections

# The ChainMap stores the list of mappings over which it searches in a list in its maps attribute.
# 	This list is mutable, so it is possible to add new mappings directly or to change the order
# 	of the elements to control lookup and update behavior.

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m = collections.ChainMap(a, b)
print(m.maps)
print('c = {}\n'.format(m['c']))

# Reverse the list.
m.maps = list(reversed(m.maps))
print(m.maps)
print('c = {}'.format(m['c']))