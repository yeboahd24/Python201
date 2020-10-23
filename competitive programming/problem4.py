#!usr/bin/env/python3

# Python function to print leaders in array

"""an element is leader if it is greater than all the elements to its right side.
	and the rightmost element is always a leader.
	Eg: {16,17,4,3,5,2}, leaders are 17, 5 and 2
"""

def printLeader(arr, size):
	for i in range(0, size):
		for j in range(i+1, size):
			if arr[i] <= arr[j]:
				break
		if j == size - 1: # if loop didn't break
			print(arr[i])

# Drive function
arr = [16, 17, 4, 3, 5, 2]
# print(printLeader(arr, len(arr)))




# method 2 (scan from right)
def printLeader(arr, size):
	max_from_right = arr[size - 1]
	print(max_from_right)
	for i in range(size - 2, 0, - 1):
		if max_from_right < arr[i]:
			print(arr[i])
			max_from_right = arr[i]

arr = [16, 17, 4, 3, 5, 2]
print(printLeader(arr, len(arr)))
