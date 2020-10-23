from functools import singledispatch
from decimal import Decimal

"""This decorator will transform your regular function
	into single dispatch generic function.
	
"""

@singledispatch
def add(x, y):
	raise NotImplentedError('Unsupported type')

@add.register(float)
@add.register(Decimal)   # overloading the function
def _(a, b):
	print('First argument of type', type(a))
	print(a + b)

if __name__ == '__main__':
	add(1.23, 5.5)
	add(Decimal(2.78), Decimal(3.97))

