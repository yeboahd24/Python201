#!usr/bin/env/python

# Validating metaclass using base class of my Polygon class hierarchy

class ValidatePolygon(type):
	def __new__(meta, name, bases, class_dict):
		# Only validate subclasses of the Polygon class
		if bases:
			if class_dict['sides'] < 3:
				raise ValueError("Polygon need 3+ sides")
			return type.__new__(meta, name, bases, class_dict)

class Polygon(metaclass=ValidatePolygon):
	sides = None # Must be specified by subclasses

# 	@classmethod
# 	def interior_angles(cls):
# 		return (cls.sides - 2) * 180

# class Triangle(Polygon):
# 	sides = 3

# class Rectangle(Polygon):
# 	sides = 4

# class Nonagon(Polygon):
# 	sides = 9

# assert Triangle.interior_angles() == 180
# assert Rectangle.interior_angles() == 360
# assert Nonagon.interior_angles() == 1260



class BetterPolygon(object):
	sides = None

	def __init_subclass__(cls):
		super().__init_subclass__()
		if cls.sides < 3:
			raise ValueError('Polygon need 3+ sides')  # Validator

	@classmethod
	def interior_angle(cls):
		return (cls.sides - 2) * 180

class Hexagon(BetterPolygon):
	sides = 3

assert Hexagon.interior_angles() == 720