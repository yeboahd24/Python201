
class Scoop(object):
	def __init__(self, flavor):
		self.flavor = flavor



class Bowl(object):

	max_scoop = 3 # class variable

	def __init__(self):
		"""Initialize self.scoops with an empty list"""
		self.scoops = []
	

	def add_scoop(self, *new_scoops):
		"""*new_scoops is just liks *args.
			You can use whatever name you want

		"""
		for one_scoop in new_scoops:
			if len(self.scoops) < Bowl.max_scoop:
				self.scoops.append(one_scoop)

	def __repr__(self):
		"""Creates a string via str.join and
			a generator expression
		"""
		return '\n'.join(s.flavor for s in self.scoops)

s1 = Scoop('chocolate')
s2 = Scoop('vanillas')
s3 = Scoop('vanilla')
s4 = Scoop('vanill')


b = Bowl()
b.add_scoop(s1, s2)
b.add_scoop(s4, s3)

print(b)



"""Reducing redundancy with dataclass"""


from typing import List
from dataclasses import dataclass, field

@dataclass
class Scoops(object):
	flavor: str

@dataclass
class Bowls(object):
	max_length = 3  # maximizing the number of scoops
	scoops: List[Scoops] = field(default_factory=list)

	def add_scoops(self, *new_scoops):
		for one_scoop in new_scoops:
			self.scoops.append(one_scoop)

	def __repr__(self):
		return '\n'.join(s.flavor for s in self.scoops)



s1 = Scoops('chocolate')
s2 = Scoops('vanilla')

b = Bowls()
b.add_scoops(s1, s2)

# print(b)