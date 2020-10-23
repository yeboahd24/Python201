from itertools import compress
from itertools import dropwhile
from itertools import starmap
from itertools import tee
"""Grouping items base on bools
	>>>list(compress(letters, bools))
	['A', 'C', 'D']
"""

letters = 'ABCDEFG'
bools = [True, False, True, True, False]
data = list(compress(letters, bools))
# print(data)

data = list(dropwhile(lambda x: x < 5, [4, 3, 5, 8, 9, 7])) # ignoring any digit less than 5
# print(data)

data = list(starmap(lambda x, y: x + y, [(2, 3), (3, 3)]))
# print(data)

data = 'ABCDEFG'
"""This create many iterable
	item1, item2 becomes separate
	object
"""

item1, item2 = tee(data)
for i in item1:
	print(i)

for x in item2:
	print(x)




