"""Note a variable inside a function is considered to be local variable.
	It exist only as long as the function does.
"""
x = 100

def foo():
	x = 200 # local variable
	print(x)
print(x) # this print 100 because this is outside the scope
foo() # this call the foo which print 100
print(x) # global x