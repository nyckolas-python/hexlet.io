#!/usr/bin/env python3

def get_range(n):
	list = []
	i = 0
	if n > 0:
		while n > i:
			list.append(i)
			i = i + 1
		return print(list)
	else:
		print(list)

if __name__ == '__main__':
	print('Проверка ТЕСТАМИ ->')
	get_range(14)
	get_range(0)
	get_range(-1)
