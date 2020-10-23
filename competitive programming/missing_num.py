def missingNumber(nums):
	max_len = len(nums)

	return int(max_len * (max_len + 1)/2 - sum(nums))

print(missingNumber([0,3,2,4]))
