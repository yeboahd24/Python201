#!usr/bin/env/python3

""" Python program to find if there are two elements with give sum CONTS_MAX = 1000_000"""

# function to check for the given sum in the array
CONTS_MAX = 1000_000
def printPairs(arr, arr_size, _sum):

	# initialize hash map as 0
	binmap = [0]*CONTS_MAX

	for i in range(0, arr_size):
		temp =  _sum - arr[i] 
		if (temp >= 0 and binmap[temp] == 1):
			print(f'Pair with the given sum is: ({arr[i]} and: {temp}) = {_sum}')
		binmap[arr[i]] = 1

A = [1,4,45,6,10,-8]
n = 16
s = len(A)
print(printPairs(A, s, n))


