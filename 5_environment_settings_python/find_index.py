#!/usr/bin/env python3

def find_index(item, list):
	for (index, _) in enumerate(list):
			if list[index] == item:
				return index
				break

def find_index_2(item, list):
	count = 0
	for i in range(len(list)):
		if list[i] == item:
			count += 1
			if count == 2:
				return i
	if count == 1:
		return None
	elif item not in list:
		return None

def find_index_3(item, list):
	input(item, list)
	cursor = iter(list)
	list(cursor)


def test():
	print(find_index_2('b', 'bob'))
	print(find_index_2(5, [1, 2, 3, 4, 5, 6, 5]))
	print(find_index_2(42, []) is None)
	print(find_index_2('!', 'abc') is None)

if __name__ == '__main__':
	test()
