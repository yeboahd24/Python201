#!usr/bin/env/python3

# Function to print element and NGE pair for all elements of list

def printNGE(arr):  # NGE - Next Greater Element
	for i in range(0, len(arr)):
		_next = - 1
		for j in range(i + 1, len(arr), 1):
			if arr[i] < arr[j]:
				_next = arr[j]
				break
		print(str(arr) + '-- ' + str(_next))


# Test Case
arr = [11, 13, 21, 3]  # [13, 21, -1, - 1]
print(printNGE(arr))