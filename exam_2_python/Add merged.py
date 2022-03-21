from collections import defaultdict

def merged(*alist): # *args ф-ция может принимать множество аргументов
	x = defaultdict(set) # если елемента нет в словаре добавляем его, значения в виде множества
	for i in alist:
		for k, v in i.items():
			x[k].add(v)
			#print(dict(x)) # выводим на экран каждую итерацию
	print(dict(x))
	return dict(x)
			

# Test Program

print(merged({}, {}) == {}) # True
print(merged(
		{'a': 1, 'b': 2},
		{'b': 10, 'c': 100}
	) == {'a': {1}, 'b': {2, 10}, 'c': {100}}) # True