def foo():
	call_counter = 0
	def bar(y):
		nonlocal call_counter  # note we normally use nonlocal when using variable of a function in another function
		call_counter +=1
		return f'y = {y}, call_counter = {call_counter}'
	return bar

b = foo()

for i in range(10, 100, 10):
	print(b(i))

