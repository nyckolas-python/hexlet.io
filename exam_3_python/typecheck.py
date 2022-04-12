from functools import wraps


def typecheck(func): # Декоратор проверяет на соответствие типам в аннотации ДО выброса ошибки
	@wraps(func)
	def inner(*args, **kwargs):
		a = func.__annotations__ # Словарь с аннотацией переменных
		#print(a) # {'x': <class 'int'>, 'y': <class 'str'>, 'z': <class 'float'>, 'foo': <class 'dict'>}
		#print(a['x']) # <class 'int'>
		#print(kwargs) # {'x': '4.0', 'y': [0]} - словарь с указанными переменными
		for k in kwargs:
			#print(k) # x - переменная
			#print(kwargs[k]) # 4.0 - значение
			if type(kwargs[k]) != a[k]: # проверяем тип переменной указанной и в аннотации
				#print(f'Ошибка типа в переменной: {k} \nОжидается -> {a[k]} имеется -> {type(kwargs[k])}')
				raise ValueError(f'Ошибка типа в переменной: {k} \nОжидается -> {a[k]} имеется -> {type(kwargs[k])}')
			else:
				return func(*args, **kwargs)
	return inner


def typecheck_all(func):	# Декоратор который ВСЕ аргументы ф-ции на соответствие типам в аннотации
	@wraps(func)	# Для того что бы ф-ция сохранила справку и имя, аннотацию используем @wraps(func)
	def inner(*args, **kwargs):
		a = func.__annotations__
		try:
			func(*args, **kwargs)
		except ValueError as e:
			print('Error: есть ошибки!')
			for k in kwargs:
				if type(kwargs[k]) != a[k]:
					print(f'Ошибка типа в переменной: {k} \nОжидается -> {a[k]} имеется -> {type(kwargs[k])}')
			print('Исправьте ошибки в переменных:')
			print([k for k in kwargs if type(kwargs[k]) != a[k]])
			return 
	return inner

# Test Program

@typecheck_all
@typecheck
def f(
x: int = 3,
y: str = "Hello!",
z: float = 3.0,
foo: dict = {'a': 42, 'b': 'bar'}
):
	print(f'Ура в переменных нет ошибок!\nx = {x}, y = {y}, z = {z}, foo = {foo}')
	print([k for k,v in locals().items()]) # ['x', 'y', 'z', 'foo'] - список всех локальных переменных
	pass
	
f(x=1, y = 'Привет, мир!')