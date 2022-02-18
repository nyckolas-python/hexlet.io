#!/usr/bin/env python3

from math import sqrt

def get_square_roots(num):
	if num > 0:
		num = sqrt(num)
		result = [-num, num]
	elif num < 0:
		result = []
	else: 	result = [0]

	return print(result)

if __name__ == '__main__':
	print('Проверка ТЕСТАМИ ->')
	get_square_roots(25)
	get_square_roots(0)
	get_square_roots(-25)
