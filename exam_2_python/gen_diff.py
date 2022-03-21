from collections import defaultdict

def gen_diff(d1, d2):
	res = defaultdict(str)
	for k in d1:
		if k not in d2:
			res[k] = 'deleted'
		elif k in d2 and d1[k]!=d2[k]:
			res[k] = 'changed'
		elif k in d2 and d1[k]==d2[k]:
			res[k] = 'unchanged'
		elif k in d2 and k not in d1:
			res[k] = 'added'
	for k in d2:
		if k not in d1:
			res[k] = 'added'
	print(dict(res))
	return res
			

# Test Program

gen_diff(
		{"one": "eon", "two": "two", "four": True},
		{"two": "own", "zero": 4, "four": True},
		) # {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}