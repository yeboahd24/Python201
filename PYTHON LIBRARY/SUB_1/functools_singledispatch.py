#!usr/bin/env/python


# In a dynamically typed language like Python, there is often a need to perform slightly
# different operations based on the type of an argument, especially when dealing with the
# difference between a list of items and a single item. It is simple enough to check the type
# of an argument directly, but in cases where the behavioral difference can be isolated into
# separate functions, functools provides the singledispatch() decorator to register a set
# of generic functions for automatic switching based on the type of the first argument to a
# function


import functools

@functools.singledispatch
def myfunc(arg):
	print('default myfunc({!r})'.format(arg))

@myfunc.register(int)
def myfunc_int(arg):
	print('myfunc_int({})'.format(arg))

@myfunc.register(list)
def myfunc_list(arg):
	print('myfunc_list()')
	for item in arg:
		print(' {}'.format(item))

myfunc('string argument')
myfunc(1)
myfunc(2.3) # Note because float is not registered this will be treated as default
myfunc(['a', 'b', 'c'])