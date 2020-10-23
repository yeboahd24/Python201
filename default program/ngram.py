
"""Creating ngram from iterable."""
from itertools import islice
def n_grams(a, n):
    z = (islice(a, i, None) for i in range(n))
    return zip(*z)

a = [1, 2, 3, 4, 5, 6]
print(list(n_grams(a, 3)))
#>>> [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
print(list(n_grams(a, 2)))
#>>> [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6)]
print(list(n_grams(a, 4)))
#>>> [(1, 2, 3, 4), (2, 3, 4, 5), (3, 4, 5, 6)]

