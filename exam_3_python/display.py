def curry(func): 
	"""Truly curry a function of any number of parameters returns a function with exactly one parameter
	When this new function is called, it will usually create and return another function that accepts 
	an additional parameter, unless the original function actually obtained all it needed at which point
	it just calls the function and returns its result """ 
	def curried(*args): 
		""" either calls a function with all its arguments, or returns another functiont 
		that obtains another argument """
		if len(args) == func.__code__.co_argcount:
			ans = func(*args)
			return ans
		else:
			return lambda x: curried(*(args+(x,)))
	return curried


def compose(func_1, func_2):
	def inner(*args, **kwargs):
		res = func_1(func_2(*args, **kwargs))
		print(res)
		return res
	return inner

pair = lambda x: [x, x]

dup = lambda x: x + x

glider = [' * ', '  *', '***']


def enlarge(img):
	img = map(dup,'$'.join(glider)) # задваиваем каждый символ, добавляем разделитель $
	#print(list(img)) # ['  ', '**', '  ', '$$', '  ', '  ', '**', '$$', '**', '**', '**']
	img = "".join(img) # склеиваем все єлементы списка в строку
	print(img) # '   **  $$    **$$******'
	img = img.split('$$') # разделяем строку в список, разделитель $$
	print(img) # ['  **  ', '    **', '******']
	img = map(pair,img) # удваиваем каждый элемент списка
	#print(list(img)) # [['  **  ', '  **  '],['    **', '    **'],['******', '******']]
	img = sum(img,[]) # сглажеваем список, убираем один уровень вложенности!
	print(img) # ['  **  ', '  **  ', '    **', '    **', '******', '******']
	return img

def display(image): # Построчный вывод на экран
    for line in image:
        print(line)

# Test Program

display(glider)
# =>  *
# =>   *
# => ***
display(enlarge(glider))
# =>   **
# =>   **
# =>     **
# =>     **
# => ******
# => ******