#!usr/bin/env/python3

# The tee() function returns several independent iterators (defaults to 2) based on a single
# original input.


from itertools import *

r = islice(count(), 5)
i1, i2 = tee(r)
print('i1:', list(i1))
print('i2:', list(i2))