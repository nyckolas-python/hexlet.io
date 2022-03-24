from operator import add
from functools import reduce


def abs_sum(alist):
	#print(alist)
	#print(list(map(abs, alist)))
	return reduce(add, map(abs, alist), 0) # Возвращает сумму абсолютных значений списка или 0 если пуст

print(abs_sum([-3, 7])) # [3, 7]
print(abs_sum([])) # 0
print(abs_sum([-42])) # 42