#!usr/bin/env/python3

"""Mix-in is a class that defines only a small set of addtional methods for its child
	to provide. It don't define thier own instance attributes nor require their __init__ constructor to bec called
"""

class ToDictMixin(object):

	def to_dict(self):
		return self._traverse_dict(self.__dict__)

	def _traverse_dict(self, instance_dict):
		output = {}
		for key, value in instance_dict.items():
			output[key] = self._traverse_dict(key, value)
		return output

	def _traverse(self, key, value):
		if isinstance(value, ToDictMixin):
			return value.to_dict()

		elif isinstance(value, dict):
			return self._traverse_dict(value)

		elif isinstance(value, list):
			return [self._traverse(key, i) for i in value]

		elif hasattr(value, '__dict__'):
			return self._traverse_dict(value.__dict__)

		else:
			return value




# using mix-in to make a dictionary representation of a binary tree

# class BinaryTree(ToDictMixin):
# 	def __init__(self, value, left=None, right=None):
# 		self.value = value
# 		self.left = left
# 		self.right = right




