def flatten(a:list) -> list:
	"""Ф-ция принимает список с вложенными списками.
	Возвращает сглаженный список, без пустых списков
	[[], [[[a]]]] -> [a]

	Args:
		a (list): [1, [2, 3], 4, [5, 6, [], [None]], False]

	Returns:
		list: [1, 2, 3, 4, 5, 6, None, False]
	"""
	if a == []:
		return a
	if isinstance(a[0], list):
		return flatten(a[0]) + flatten(a[1:])
	return a[:1] + flatten(a[1:])

# Test Program

a = [1, [2, 3], 4, [5, 6, [], [None]], False]
print(flatten(a))
# [1, 2, 3, 4, 5, 6, None, False]