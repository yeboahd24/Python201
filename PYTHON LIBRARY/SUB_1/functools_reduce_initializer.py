#!usr/bin/env/python3

# The optional initializer argument is placed at the front of the sequence and processed
# along with the other items. This can be used to update a previously computed value with
# new inputs.


import functools

def do_reduce(a, b):
	print('do_reduce({}, {})'.format(a, b))
	return a + b
	
data = range(1, 5)
print(data)
result = functools.reduce(do_reduce, data, 99)
print('result: {}'.format(result))
