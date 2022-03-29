cache = {} # словарь с кешем
			
def memoizing(count):
	def memoized(function):	
		def inner(*args, **kwargs):
			if args[0] in cache: # Проверяем присутствие в словаре аргумент ф-ции
				res = cache[args[0]] # В результате присваиваем значение по ключу аргумента
				print(f'We have in cache: {res}') # Выводи результат с помощья ф-строки
				return res
			else: # Если аргумента нет в словаре
				res = function(*args, **kwargs)
				while len(cache) >= count: # Выполняем если количество элем в словаре больше/равно count
					first_key = list(cache.keys())[0] # Берём ключ первого элемента словаря
					cache.pop(first_key) # Удаляем элемент словаря по ключу
				else:
					cache[args[0]] = res # добавляем в словарь наш аргумент и результат
					print(res) # Выводим выполняние ф-ции
					return res
		return inner
	return memoized	

# Test Program
@memoizing(3)
def f(x):
	print('Calculating...')
	return x*10

f(1) # Calculating... 10
f(1) # We have in cache: 10
f(2) # Calculating... 20
f(3) # Calculating... 30
f(4) # Calculating... 40
f(1) # Calculating... 10
f(3) # We have in cache: 30
print(cache) # {3: 30, 4: 40, 1: 10}