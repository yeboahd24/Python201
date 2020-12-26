#!usr/bin/env/python3


# The lru_cache() decorator wraps a function in a “least recently used” cache. Arguments to
# the function are used to build a hash key, which is then mapped to the result. Subsequent
# calls with the same arguments will fetch the value from the cache instead of calling the
# function. The decorator also adds methods to the function to examine the state of the
# cache (cache_info()) and empty the cache (cache_clear()).


import functools

@functools.lru_cache()
def expensive(a, b):
	print('expensive({}, {})'.format(a, b))
	return a * b

MAX = 2

# print('First set of calls:')
# for i in range(MAX):
# 	for j in range(MAX):
# 		expensive(i, j)
# print(expensive.cache_info())

# print('\nSecond set of calls:')
# for i in range(MAX + 1):
# 	for j in range(MAX + 1):
# 		expensive(i, j)
# print(expensive.cache_info())

# print('\nClearing cache:')
# expensive.cache_clear()
# print(expensive.cache_info())

# print('\nThird set of calls:')
# for i in range(MAX):
# 	for j in range(MAX):
# 	expensive(i, j)
# print(expensive.cache_info())

call1 = expensive(2, 2)
call2 = expensive(1, 2)
print(call1)
print(call2)
print(call1)