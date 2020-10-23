#!usr/bin/env/python3

# Python program to find the smallest and second smallest elements

import sys

def print2Smallest(arr):

	# There should be atleast two elements
	arr_size = len(arr)
	if arr_size < 2:
		print('Invalid Input')
		return

	first = second = sys.maxsize
	for i in range(0, arr_size):
		# If current element is smaller than first then
		# Update both first and second
		if arr[i] < first:
			second = first
			first = arr[i]

		# If arr[i] is in between first and second then update second
		elif (arr[i] < second and arr[i] != first):
			second = arr[i]

	if (second == sys.maxsize):
			print('No second smallest element')
	else:
		print(f'The smallest element is: {first} and the second smallest element is: {second}')

# Test Case
arr = [12, 13, 1, 10, 34, 1]
print(print2Smallest(arr))