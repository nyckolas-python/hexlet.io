def find_where(data: dict, d1: dict):
	for d2 in data:
		if all(k in d2 and d1[k] == d2[k] for k in d1) == True: # сравниваем есть ли все елементы словаря d1 в d2
			print(d2)
			return d2
	print(None)
	return None

def find_where_2(data: dict, search: dict):
	check_keys = False
	check_values = False
	for i in data:
		chek_keys = set(search.keys()).issubset(set(i.keys())) # Проверяем на вхождение ключей, сравниваем множествами
		check_values = set(search.values()).issubset(set(i.values())) # Проверяем на вхождение значения, сравниваем множествами
		if chek_keys == check_values == True: # Должны соблюдаться оба условия одновременно
			print(i)
			return i
	print(None)
	return None

# Test Program
books = [
	{'title': 'Book of Fooos', 'author': 'Foo', 'year': 1111},
	{'title': 'Cymbeline', 'author': 'Shakespeare', 'year': 1611},
	{'title': 'The Tempest', 'author': 'Shakespeare', 'year': 1611},
	{'title': 'Book of Foos Barrrs', 'author': 'FooBar', 'year': 2222},
	{'title': 'Still foooing', 'author': 'FooBar', 'year': 333},
	{'title': 'Happy Foo', 'author': 'FooBar', 'year': 4444},
	]
find_where(books, {'author': 'Shakespeare', 'year': 1611})