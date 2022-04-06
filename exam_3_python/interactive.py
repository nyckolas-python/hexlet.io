from functools import wraps


input_dict = {}	# словарь для записи аргументов инпута

def interactive(text:str):	# Декоратор которыйпринимает текст и выводит на печать ф-цию
	def wrapped(func):
		@wraps(func)	# Для того что бы ф-ция сохранила справку и имя используем @wraps(func)
		def inner():
			print(text)			
			print(func())
		return inner
	return wrapped

def asks(key:str, ask_number:str):	# Декоратор запрашивает аргументы ф-ции и записывает в словарь
	def wrapped(func):
		@wraps(func)	# Для того что бы ф-ция сохранила справку и имя используем @wraps(func)
		def inner(*args, **kwargs):
			value = input(ask_number)	# Ввод аргумента
			input_dict[key] = value	 # Запись аргумента в словарь
			return func(*input_dict.values())	# Вовзвращает ф-цию с аргументами
		return inner
	return wrapped


@interactive('Calculator')
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calc(x, y):
	"""
	Ф-ция принимает два аргумента "х" и "у" и возвращает их сумму.
	"""
	return int(x) + int(y)

calc()

#Calculator
#Enter first number: 42
#Enter second number: 57
# 99
print(calc)
# Ф-ция не потеряла имя и справку благодаря декоратору @wraps(func)
#<function calc at 0x7f92aab73160>