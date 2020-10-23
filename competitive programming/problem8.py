#!usr/bin/env/python3

# Python script to implement two stacks in a list

class twoStack(object):

	def __init__(self, n):
		self.size = n
		self.arr = [None] * n
		self.top1 = - 1
		self.top2 = self.size

	# method to push an element x to stack1
	def push1(self, x):

		# There is at least one empty space for new element
		if self.top1 < self.top2 - 1:
			self.top1 = self.top1 + 1
			self.arr[self.top1] = x

		else:
			print('Stack Overflow')
			exit(1)


	# method to push an element x to stack2
	def push2(self, x):

		# There is at least one empty space from second stack
		if self.top1 < self.top2 - 1:
			self.top2 = self.top2 - 1
			self.arr[self.top2] = x

		else:
			print('Stack Overflow')
			exit(1)

	def pop1(self):
		if self.top1 >= 0:
			x = self.arr[self.top1]
			self.top1 = self.top1 - 1
			return x

		else:
			print('Stack Underflow')
			exit(1)

	def pop2(self):
		if self.top2 < self.size:
			x = self.arr[self.top2]
			self.top2 = self.top2 - 1
			return x

		else:
			print('Stack Underflow')
			exit()


# Test Case
ts = twoStack(5)
ts.push2(15)
ts.push2(7)
ts.push1(10)
ts.push2(11)

print('Popped element from stack1 is ' + str(ts.pop1()))
ts.push2(40)
print('Popped element from stack2 is ' + str(ts.pop2()))

			
