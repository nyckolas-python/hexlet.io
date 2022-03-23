def make_star(x):
	if x > 0:
		return True, '*' * x
	return False, ''

def is_false(x):
	if x != (False, ''):
		return x

def filter_map(function, iter):
	res = map(function, iter)
	d = filter(is_false, res)
	return [x[1] for x in d]

b = filter_map(make_star, [1, 0, 5, -5, 2])
for s in b:
	print('-> '+s)
#-> *
#-> ******
#-> **