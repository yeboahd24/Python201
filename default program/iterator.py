class MyIterator(object):
	"""
	Contstructor
	"""
	def __init__(self, letters):
		self.letters = letters
		self.postion = 0

	def __iter__(self):
		"""
		Returns itself as an iterator
		"""
		return self

	def __next__(self):
		"""
		Returns the next letter in sequence or
		raise StopIteration
		"""
		if self.postion >= len(self.letters):
			raise StopIteration
		letter = self.letters[self.postion]
		self.postion += 1
		return letter

if __name__ == '__main__':
	x = MyIterator('Linux')
	for i in x:
		print(i)