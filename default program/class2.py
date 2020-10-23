#!usr/bin/env/python3

"""use plain attribute instead of setter and getter methods"""

class OldResistor(object):
	"""using these setters and getters is simple but not pythonic"""
	def __init__(self, ohms):
		self._ohms = ohms

	def get_ohms(self):
		return self._ohms

	def set_ohms(self, ohms):
		self._ohms = ohms

# r = OldResistor(50e3)
# print('Before: ', r.get_ohms())
# r.set_ohms(10e3)
# print('After: ', r.get_ohms())


class Resistor(object):
	def __init__(self, ohms):
		self.ohms = ohms
		self.voltage = 0
		self.current = 0

r1 = Resistor(50e3)
r1.ohms = 10e3   # simple implementation
# print(r1.ohms)


# Pythonic Implementation

class VoltageResistor(Resistor):
	def __init__(self, ohms):
		super().__init__(ohms)
		self._voltage = 0

	@property
	def voltage(self):
		return self._voltage

	@voltage.setter
	def voltage(self, voltage):
		self._voltage = voltage

		self.current = self._voltage / self.ohms

# r2 = VoltageResistor(1e3)
# print(f'Before: {r2.current:.2f} amps')
# r2.voltage = 10e3
# print(f'After: {r2.current:.2f} amps')




class BoundedResistance(Resistor):
	"""using setter and getter to validate"""
	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if ohms <= 0:
			raise ValueError(f'ohms must be > 0; got {ohms}')
		self._ohms = ohms


# using property method to make attribute from parent class immutable

class FixedResistance(Resistor):
	def __init__(self, ohms):
		super().__init__(ohms)

	@property
	def ohms(self):
		return self._ohms

	@ohms.setter
	def ohms(self, ohms):
		if hasattr(self, '_ohms'):
			raise AttributeError("Ohms is immutable")
		self._ohms = ohms

r4 = FixedResistance(10e3)
r4.ohms = 11e4
print(r4.ohms)

