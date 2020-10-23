#!usr/bin/env/python

# using super to initialize the parent class
# Mutliple inheritane
# Note super().__init__(value) is more pythonic than MyBaseClass.__init__
class MyBaseClass(object):
	def __init__(self, value):
		self.value = value

class TimesSevenCorrect(MyBaseClass):
	def __init__(self, value):
		super().__init__(value)
		self.value *= 7

class PlusNineCorrect(MyBaseClass):
	def __init__(self, value):
		super().__init__(value)
		self.value += 9

class GoodWay(TimesSevenCorrect, PlusNineCorrect):
	def __init__(self, value):
		super().__init__(value)
		self.value = value

foo = GoodWay(5)
print("Should be 7 * (5 + 9) = 98 and is", foo.value)

my_str = '\n'.join(repr(cls) for cls in GoodWay.mro())  # checing the MRO
print(my_str)



# class People(object):
# 	def name(self):
# 		print('Naming')

# class Age(People):
# 	def name(self):
# 		print('Aging')
# 		super().name()

# class Talk(Age):
# 	def name(self):
# 		print('Talking')

# class All(Talk, Age):
# 	def name(self):
# 		print('All')
# 		super().name()

# a = All()
# print(a.name())
# print(a.name())
# print()