
# The dropwhile() function returns an iterator that produces elements of the input iterator
# after a condition becomes false for the first time.


# The opposite of dropwhile() is takewhile(). It returns an iterator that itself returns
# items from the input iterator as long as the test function returns true

# The built-in function filter() returns an iterator that includes only items for which
# the test function returns true.
# filter() differs from dropwhile() and takewhile() in that every item is tested before it is
# returned.


from itertools import *

def should_drop(x):
	print('Testing:', x)
	return x < 1
print('Taking any value greater than 1')
for i in dropwhile(should_drop, [-1, 0, 1, 2, -2]):
	print('Yielding:', i)



def should_take(x):
	print('Testing:', x)
	return x < 2
print('Taking any value less than 2:')
for i in takewhile(should_take, [-1, 0, 1, 2, -2]):
	print('Yielding:', i)


def check_item(x):
	print('Testing:', x)
	return x < 1
print('Filtering')
for i in filter(check_item, [-1, 0, 1, 2, -2]):
	print('Yielding:', i)
