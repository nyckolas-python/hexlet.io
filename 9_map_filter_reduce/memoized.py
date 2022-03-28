cache = {} # словарь с кешем

def memoized(function):
	def inner(*args, **kwargs):
		if args[0] in cache: # Проверяем присутствие в словаре аргумент ф-ции
			res = cache[args[0]] # В результате присваиваем значение по ключу аргумента
			print(f'We have in cache: {res}') # Выводи результат с помощья ф-строки
			return res
		else: # Если аргумента нет в словаре
			res = function(*args, **kwargs)
			cache[args[0]] = res # добавляем в словарь наш аргумент и результат
			print(res) # Выводим выполняние ф-ции
			return res
	return inner

# Test Program
@memoized
def f(x):
	print('Calculating...')
	return x*10

f(10) # Calculating... 100
f(42) # Calculating... 420
f(10) # We have in cache: 100
f(42) # We have in cache: 100
print(cache) # {10: 100, 42: 420}