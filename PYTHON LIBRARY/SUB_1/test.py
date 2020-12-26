
import functools

def standalone(self, a, b):
	"Standalone function"
	# print(' called standalone with:', (self, a, b))
	if self is not None:
		# print(' self.attr =', self.name, self.age)
		print(f"These are the attributes =, {self.name} and {self.age}")


class MyClass(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age

	method1 = functools.partialmethod(standalone) # acting like decorator


my = MyClass('linux', 20)
my.method1(my, 20)
print()