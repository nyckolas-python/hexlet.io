def same_parity_filter(alist):
	res = []
	if len(alist) > 0:
		res = [i for i in alist if abs(alist[0] % 2) == abs(i % 2)]
	print(res)
	return res

# Test Program
	
same_parity_filter([])
	# []
same_parity_filter([2, 0, 1, -3, 10, -2])
	# [2, 0, 10, -2]
same_parity_filter([-1, 0, 1, -3, 10, -2])
	# [-1, 1, -3]