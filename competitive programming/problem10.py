#!usr/bin/env/python3

# Python program to find maximum sum path

def maxPathSum(arr1, arr2, m, n):

	# initialize indexes for arr1[] and arr2[]
	i, j = 0, 0

	# Initialize result and current sum through arr[] and arr2[]
	result, sum1, sum2 = 0, 0, 0

	# Below 3 loops are similar to merge in merge sort
	while (i < m and j < n):
		# Add elements of arr1[] to sum1
		if arr1[i] < arr2[j]:
			sum1 += arr1[i]
			i += 1

		# Add elements of arr2[] to sum1
		elif arr1[i] > arr2[j]:
			sum2 += arr2[j]
			j += 1

		else:
			# we reached a common point
			result += max(sum1, sum2)

			sum1, sum2 = 0, 0  # update sum1 and sum2

			# keep updating result while there are more common elements
			while (i < m and j < n and arr1[i] == arr2[j]):
				result += arr1[i]
				i += 1
				j += 1

	while i < m:  # Add remaining elements of arr1[]
		sum1 += arr1[i]
		i += 1

	while  j < n:
		sum2 += arr2[j]
		j += 1

	result += max(sum1, sum2)
	return result

	
# Test Case
arr1 = [2,3,7,10,12,15,30,34]
arr2 = [1,5,7,8,10,15,16,19]
n = len(arr1)
m = len(arr2)
print('Maximum sum path is: ', maxPathSum(arr1, arr2, m, n))
