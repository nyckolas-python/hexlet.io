
from operator import itemgetter


def find_index_of_nearest(n, alist):
	if len(alist) > 0:
		minlist = list(map(lambda x: abs(x-n), alist))
		index = min(enumerate(minlist), key=itemgetter(1))[0]
		#print(minlist)
		print(index)
		return index
	print(None) 
	return None

# Test Program	
find_index_of_nearest(2, []) is None
# True
find_index_of_nearest(0, [15, 10, 3, 4])
# 2
find_index_of_nearest(4, [7, 5, 3, 2])
# 1
find_index_of_nearest(4, [7, 5, 4, 4, 3])
# 2