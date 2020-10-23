def sort_priority(numbers, group):
	found = False 
	def helper(x):
		nonlocal found  # is used to assigned out closure into another scope
		if x in group:	# note avoid using nonlocal statements for anything beyound simple function
			found =True
			return (0, x)
		return (1, x)
	numbers.sort(key=helper)
	return found

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
found = sort_priority(numbers, group)
# print('Found:', found)
# print(numbers)


class Sorter:
	def __init__(self, group):
		self.group = group
		self.found = False

	def __call__(self, x):
		if x in self.group:
			self.found = True
			return (0, x)
		return (1, x)
sorter = Sorter(group)
numbers.sort(key=sorter)
print(numbers)