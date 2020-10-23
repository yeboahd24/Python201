def foo(x):
	def bar(y):
		return x * y
	return bar # the bar is a local variable inside foo
f = foo(10)
print(f(20))