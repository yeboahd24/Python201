# sorting array by parity

def sortParity(nums):
	even = [a for a in nums if a % 2 == 0]
	odd = [a for a in nums if a % 2]
	results = []

	for i in range(len(nums)//2):
		results.append(even[i])
		results.append(odd[i])
	return results

print(sortParity([2,4,5,3])) # so in here the results shoulb be even, odd even, odd in that order 
