#!usr/bin/env/python

# Register Class Existence with __init_subclass__

# Eg: Implementing your own serialized using JSON

import json

class Serializabel(object):
	def __init__(self, *args):
		self.args = args

	def serialize(self):
		return json.dumps({'args': self.args}) # This class makes it easy to serialize simple

class Point2D(Serializabel):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.x = x
		self.y = y

	def __repr__(self):
		return f'Point2D({self.x}, {self.y})'


class Deserrializable(Serializabel):
	@classmethod
	def deserialize(cls, json_data):
		params = json.loads(json_data)
		return cls(*params['args']) # Using Deseriable makes it easy to serialize and deserialize
									# simple, immutable objects in a generic way

class BetterPoint2D(Deserrializable):
	pass


# point = Point2D(5, 3)
# print('Object: ', point)
# print('Serialized: ', point.serialize())

# before = Point2D(5, 3)
# print('Before: ', before)
# data = before.serialize()
# print('Serialized: ', data)
# after = BetterPoint2D.deserialize(data)
# print('After: ', after)





class BetterSerializabel(object):
	def __init__(self, *args):
		self.args = args

	def serialize(self):
		return json.dumps({'class': self.__class__.__name__, 'args': self.args})

	def __repr__(self):
		name = self.__class__.__name__
		args_str = ','.join(str(x) for x in self.args)
		return f'{name}({args_str})'


class BetterRegisteredSerializable(BetterSerializabel):
	def __init_subclass__(cls):
		super().__init_subclass__()
		# register_class(cls)

class Vector1D(BetterRegisteredSerializable):
	def __init__(self, magnitude):
		super().__init__(magnitude)
		self.magnitude = magnitude


before = Vector1D(6)
print('Before: ', before)
data = before.serialize()
print('Serialized: ', data)
