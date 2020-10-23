def longestSubstring(word):
	dict_ = {}
	start = 0
	results = 0

	for index, value in enumerate(word):
		if value in dict_:
			start = max(start, dict_[value] + 1)
		dict_[value] = 1
		results = max(results, index - start + 1)
	return results

