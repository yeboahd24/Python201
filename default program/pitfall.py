#!usr/bin/env/python3

# Changing the sequence you are iterating over

alist = [0, 1, 2]
for index, value in enumerate(alist):
	alist.pop(index)
# print(alist) # [1]

# optimizing it
# iterating this time does not affect the index

alist = [1,2,3,4,5,6,7]
for index, value in reversed(list(enumerate(alist))):
	# delete all even items
	if value % 2 == 0:
		alist.pop(index)

# print(alist) #Out: [1,3,5,7]

'''modifying a list elements with the placeholder is not possible
	it does not change anything in the original list
'''
alist = [1,2,3,4]
for item in alist:
	if item % 2 == 0:
		item = 'even'
# print(alist) # Out: [1,2,3,4]

# this is the better way to do

alist = [1,2,3,4]
for index, item in enumerate(alist):
	if item % 2 == 0:
		alist[index] ='even'
# print(alist)

'''Do not check agains type checking'''
# Don't do this

def foo(name):
	if isinstance(name, str):
		print(name.lower())

def bar(listing):
	if isinstance(listing, list):
		listing.append((1,2,3))
		return ", ".join(listing)


# Do this

def foo(name):
	print(str(name).lower())

def bar(listing):
	l = list(listing)
	l.extend(1,2,3)
	return ", ".join(l)

	

