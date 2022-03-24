from operator import getitem


def walk(alist, keylist):
	for i in keylist:
		alist = getitem(alist, i)
	print(alist)

walk({'a': {7: {'b': 42}}}, ['a', 7, 'b']) # 42
walk({'a': {7: {'b': 42}}}, ['a', 7]) # {'b': 42}