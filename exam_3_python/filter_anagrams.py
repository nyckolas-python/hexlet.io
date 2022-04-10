from collections import Counter


def filter_anagrams(word:str, alist:list):
	res = [i for i in alist if Counter(word) == Counter(i)]
	print(res)
	return res

# Test Program
	
list(filter_anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
	# ['aabb', 'bbaa']
list(filter_anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
	# ['carer', 'racer']
list(filter_anagrams('laser', ['lazing', 'lazy',  'lacer']))
	# []
list(filter_anagrams([1, 2], [[2, 1], [2, 2], [1, 2]]))
	# [[2, 1], [1, 2]]