from pprint import pprint # Подключае модуль красивого вывода на экран


def convert(node:list) -> dict:
	"""
	Ф-ция принимает на вход список. Каждый элемент списка кортеж из двух элементов.
	Первый елемент - ключ, второй - значение. Значение может быть таким же списком.
	Любой список внутри исходного списка всегда рассматриваются как данные, которые
	нужжно конвертировать в словарь.

	Args:
		node (list): [(key, [(key, value)],
				(key2, value2)
				]

	Returns:
		dict: {key: {key: value},
			key2: value2
			}
	"""
	output = dict(map(
		# если второй элемент списка имее тип список, то рекурсивно применяем ф-цию
		lambda x: (x[0],convert(x[1])) if type(x[1]) == list else x,
		node
		))
	return output

node = [
	('key', [('anotherKey', [('anotherKeyKey', 'anotherValue')])]),
	('key2', [('anotherKey2', [('anotherKeyKey2', 'anotherValue2')])])
	]

# Test Program
	
pprint(convert(node))

# {'key': {'anotherKey': {'anotherKeyKey': 'anotherValue'}},
#  'key2': {'anotherKey2': {'anotherKeyKey2': 'anotherValue2'}}}
