#!usr/bin/env/python3

# Python implementation of maximum sum increasing subsequence problem(MSIS)
# Eg: [1, 101, 2, 3, 100, 4, 5] = 106(1 + 2 + 3+ 100)

def maxSumIs(arr, n):
	_max = 0
	msis = [0 for x in range(n)]

	# Initialize msis values for all indexes
	for i in range(n):
		msis[i] = arr[i]

	# Compute maximum sum values in bottom up manner
	for i in range(n):
		for j in range(i):
			if arr[i] > arr[j] and msis[i] < msis[j] + arr[i]:
				msis[i] = msis[j] + arr[i]

	# Pick maximum of all msis values
	for i in range(n):
		if _max < msis[i]:
			_max = msis[i]
	return _max


# Test Case
arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print('Sum of maximum sum increasing subsequence is: ' +str(maxSumIs(arr, n)))
