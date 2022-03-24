from operator import truth


def keep_truthful(alist):
	return filter(truth, alist) # operator.truth(x) return False -> (0, "", False, None)

print(list(keep_truthful([True, False, "", "foo", None]))) # [True, 'foo']
	