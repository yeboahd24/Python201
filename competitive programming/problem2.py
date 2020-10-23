#!usr/bin/env/python3

"""Python program to find the element occurring odd number of times"""

def getOddOccurrence(arr):

	# initialize result
	res = 0

	# Traverse the array
	for element in arr:
		# XOR with the result
		res = res ^ element
	return res

# Test array
arr = [2,3,5,4,5,2,4,3,5,2,4,4,2]
print(f'{arr}: ', getOddOccurrence(arr))
	



