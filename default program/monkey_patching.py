#!usr/bin/env/python3
"""Monkey patching means adding new variable or method to a class after it is been defined"""

class A(object):
	def __init__(self, num):
		self.num = num

	def __add__(self, other):
		return A(self.num + other.num)

def get_num(self):
	return self.num

# adding get_num() function to A class

A.get_num = get_num # the monkey patch

foo = A(42)
bar = A(6)

print(foo.get_num())
print(bar.get_num())

