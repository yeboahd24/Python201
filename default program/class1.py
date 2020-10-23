#!usr/bin/env/python3

"""Prefer Public Attribute Over Private Ones
	Public Attribute can be accessed by anyone using
	the dot operator on the object
"""

class MyObject(object):
	def __init__(self):
		self.public_field = 5
		self.__private_field = 10

	def get_private_field(self):
		return self.__private_field


foo = MyObject()
assert foo.public_field == 5
assert foo.get_private_field() == 10
# print(foo.__private_field) # accessing this gives you an error
# print(foo.get_private_field()) # this give no errors


class MyOtherObject(object):
	"""class methods also have access to private attributes because they are
		declared within the surrounding class block
	"""
	def __init__(self):
		self.__private_field = 71

	@classmethod
	def get_privat_field_instance(cls, instance):
		return instance.__private_field
bar = MyOtherObject()
# print(bar.get_privat_field_instance(bar)) # Out: 71


class MyParentObject(object):
	def __init__(self):
		self.__private_field = 71

class MyChildObject(MyParentObject):
	def get_private_field(self):
		return self.__private_field

baz = MyChildObject()
# print(baz.get_private_field()) # error because the __private_field is accessible in the MyParentObject
# print(baz.__dict__)  # try:



# Avoiding naming conflict with private attribute

class ApiClass(object):
	def __init__(self):
		# self._value = 5 # this will result in naming conflict
		self.__value = 5
	def get(self):
		return self.__value

class Child(ApiClass):
	def __init__(self):
		super().__init__()
		self._value = 'hello'

a = Child()
print(f' {a.get()} and {a._value} are different')
