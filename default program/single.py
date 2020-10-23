from functools import singledispatch

"""This decorator will transform your regular function
	into single dispatch generic function
	>>>add(1, 2)
	First argument of type <class int>
	3
"""

@singledispatch
def add(x, y):
	raise NotImplentedError('Unsupported type')

@add.register(int)
def _(a, b):
	print('First argument of type', type(a))
	print(a + b)


@add.register(str)
def _(a, b):
	print('First argument of type', type(a))
	print(a + b)

@add.register(list)
def _(a, b):
	print('First argument of type', type(a))
	print(a + b)

if __name__ == '__main__':
	add(1, 2)
	add('Python', 'Programming')
	add([1,2,3], [4, 5, 6])




