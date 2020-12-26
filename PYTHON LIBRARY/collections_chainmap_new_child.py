#!usr/bin/env/python3

# ChainMap provides a convenience method for creating a new instance with one extra
# mapping at the front of the maps list to make it easy to avoid modifying the existing
# underlying data structures.



import collections

a = {'a': 'A', 'c': 'C'}
b = {'b': 'B', 'c': 'D'}

m1 = collections.ChainMap(a, b)
m2 = m1.new_child()

print('m1 before:', m1)
print('m2 before:', m2)
m2['c'] = 'E'
print('m1 after:', m1)
print('m2 after:', m2)