class Slug(object):
	"""A subclass that break substitutability.

	"""
	def __init__(self, name):
		self.name = name

	def craw(self):
		print('slime trail')

class Snail(Slug):
	"""Snail inherits from Slug
	"""
	def __init__(self, name, shell_size):
		"""Using different instance creation
			is a common way to violate substitutability
		"""
		super().__init__(name)
		self.name =name
		self.shell_size = shell_size

def race(gastropod_one, gastropod_two):
		"""Trying to use Snail without a shell_size
			argument raises an exception
		"""
		gastropod_one.craw()
		gastropod_two.craw()
	
race(Slug('Geoffrey'), Slug('Romona'))
race(Snail('Geoffrey', 25), Snail('Romona', 2))