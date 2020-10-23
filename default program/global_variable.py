x = 100 # global variable

def foo():
	global x
	x = 200
	print(x)  # this change the initial value x=100 to x=200 through the use of the global

print(x) #x=100
foo() #x=200
print(x) #x=200 because it was updated in the scope