#!usr/bin/env/python3

# python program for reversal algorithm of array rotation

def reverseArray(arr, start, end):
	while start < end:
		temp = arr[start]
		arr[start] = arr[end]
		arr[end] = temp
		end = end - 1

# Function to left rotate arr[] fo size n  by d
def leftRotate(arr, d):
	n = len(arr)
	reverseArray(arr, 0, d - 1)
	reverseArray(arr, d, n - 1)
	reverseArray(arr, 0, n - 1)

# Function to print an array
def printArray(arr):
	for i in range(0, len(arr)):
		print(arr[i], end=' ')



# Test case
arr = [1,2,3,4,5,6,7]
leftRotate(arr, 2)
printArray(arr)