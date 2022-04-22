def remove_first_level(atree):
	li = [i for i in atree if type(i) == list] # убираем листья
	print(li) # [[5], [3, 4]]
	result = [item for i in li for item in i] # сглаживаем один уровень вложенности
	print(result) # [5, 3, 4]
	return result

# Test Program

tree1 = [[5], 1, [3, 4]]

remove_first_level(tree1)
# [5, 3, 4]

tree2 = [1, 2, [3, 4], [[5, 6], 7]]

remove_first_level(tree2)
# [3, 4, [5, 6], 7]