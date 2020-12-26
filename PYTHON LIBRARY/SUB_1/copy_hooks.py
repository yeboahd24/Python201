
import copy
import functools

@functools.total_ordering
class MyClass:
	def __init__(self, name):
		self.name = name

	def __eq__(self, other):
		return self.name == other.name

	def __gt__(self, other):
		return self.name > other.name

	def __copy__(self):
		print('__copy__()')
		return MyClass(self.name)

	def __deepcopy__(self, memo):
		print('__deepcopy__({})'.format(memo))
		return MyClass(copy.deepcopy(self.name, memo))

a = MyClass('a')
sc = copy.copy(a)
dc = copy.deepcopy(a)
print(sc)
print(dc)

#The memo dictionary is used to keep track of the values that have been copied already,
#so as to avoid infinite recursion.
