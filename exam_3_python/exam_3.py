#!/usr/bin/env python3

from functools import reduce, wraps
from ipaddress import IPv4Address
from operator import add, itemgetter
from typing import Counter


def compose(func_1, func_2):
	def inner(*args, **kwargs):
		res = func_1(func_2(*args, **kwargs))
		print(res)
		return res
	return inner


def get_men_counted_by_year(users):
	man = [i['birthday'][:4] for i in users if i['gender'] == 'male']
	print(dict(Counter(man)))
	return dict(Counter(man))
	
users = [
	{'name': 'Bronn', 'gender': 'male', 'birthday': '1973-03-23'},
	{'name': 'Reigar', 'gender': 'male', 'birthday': '1973-11-03'},
	{'name': 'Eiegon', 'gender': 'male', 'birthday': '1963-11-03'},
	{'name': 'Sansa', 'gender': 'female', 'birthday': '2012-11-03'},
	{'name': 'Jon', 'gender': 'male', 'birthday': '1980-11-03'},
	{'name': 'Robb', 'gender': 'male', 'birthday': '1980-05-14'},
	{'name': 'Tisha', 'gender': 'female', 'birthday': '2012-11-03'},
	{'name': 'Rick', 'gender': 'male', 'birthday': '2012-11-03'},
	{'name': 'Joffrey', 'gender': 'male', 'birthday': '1999-11-03'},
	{'name': 'Edd', 'gender': 'male', 'birthday': '1973-11-03'},
	]

def decode(physical_signal):
	# List physical signals
	high_signal = '¯'
	low_signal = '_'
	pipe_signal = '|'

	bits = ''  # if no matter start with
#	bits = '0' # start with bit 0
	def check_health() -> None:
		# Check validators on physical signal

		if not physical_signal:
			raise Exception('Physical signal is empty')

		for token in physical_signal:
			if token not in [low_signal, high_signal, pipe_signal]:
				raise Exception(
					'Token {} is invalid int physical signal segment'.
					format(token))
#			if physical_signal[0] not in [low_signal, high_signal]:
#			# Validate high and low signal
#			raise Exception(
#				'Physical signal {} does not start with high or low signal'.
#				format(physical_signal[0]))
	check_health()

	# Get a bool bit
	def give_bit(λ): return str((0, 1)[λ])
	change_signal = False

	# Skip first element, if first bit always is 0
#	for token in physical_signal[1:]:
	for token in physical_signal:

		# If changed singal return bit 1
		current_bit = give_bit(change_signal)

		if token == pipe_signal:
			# When change signal is identified the next bit should be 1
			change_signal = True
			continue
		else:
			# Bit should be 0
			change_signal = False

		bits += current_bit
	print(bits)
	return bits


def find_index_of_nearest(n, alist):
	if len(alist) > 0:
		minlist = list(map(lambda x: abs(x-n), alist))
		index = min(enumerate(minlist), key=itemgetter(1))[0]
		#print(minlist)
		print(index)
		return index
	print(None) 
	return None	

def conv(n,ri=10,ro=16):
	digs="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	acc=0
	res=""
	if n in {0, '00', '0'}:
		res='00'		
	for a in str(n).upper():
		k=digs.find(a)
		acc=acc*ri+k		
	while(acc>0):
		k=acc%ro
		res=digs[k]+res
		acc=acc//ro
	return res

def rgb2hex(r,g,b):
	hex = conv(r) + conv(g) + conv(b)
	print(hex)
	return hex

def hex2rgb(line):
	rgb = {}
	rgb['r'] = conv(line[1:3],16,10)
	rgb['g'] = conv(line[3:5],16,10)
	rgb['b'] = conv(line[5:],16,10)
	print(rgb)
	return rgb


def ip2int(line):
	# First Method
	adr = IPv4Address(line)
	print(int(adr))

	# Second Method
	a,b,c,d = line.split('.')
	x = int(a) * 256**3 + int(b) * 256**2 + int(c) * 256 + int(d)	
	if x == int(adr):
		print(x)
		return x

def int2ip(ipnum):
	# First Method
	line = str(IPv4Address(ipnum))
	print(line)

	#Second Method
	a = ipnum//256**3
	b = (ipnum - (a*256**3))//256**2
	c = (ipnum - a*256**3 - b*256**2)//256
	d = (ipnum - a*256**3 - b*256**2 - c*256)
	res_line = f'{a}.{b}.{c}.{d}'
	if res_line == line:
		print(res_line)
		return line

input_dict = {}

def interactive(text:str):
	def wrapped(func):
		@wraps(func)
		def inner():
			print(text)			
			print(func())
		return inner
	return wrapped

def asks(key:str, ask_number:str):
	def wrapped(func):
		@wraps(func)
		def inner(*args, **kwargs):
			value = input(ask_number)
			input_dict[key] = value	
			return func(*input_dict.values())
		return inner
	return wrapped


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

glider = [' * ', '  *', '***']
def display(image):
    for line in image:
        print(line)
pair = lambda x: [x, x]
dup = lambda x: x + x
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


def histo(alist:list, min_value=None, max_value=None, bar_char='#'):
	res = []
	if max_value == None: max_value = max(alist) # если аргумент не задян, то присваиваем макс элемент
	if min_value == None: min_value = min(alist) # если аргумент не задян, то присваиваем мин элемент
	hist = [i for i in alist if max_value >= i >= min_value] # оставляем только max_value >= i >= min_value
	c = Counter(hist) # подсчитываем повторяющиеся элементы с списке
	#print(c) # Counter({1: 3, 5: 2, 3: 1, 4: 1})
	for i in range(min_value, max_value+1):
		if c[i] != 0: # По ключу находим в словаре количество, формируем строку результата
			line = ('# => '+str(i)+'/'+bar_char*c[i]+' '+str(c[i]))
		else: # Если ключ возвращает 0 значит такого єлемента нет, формируем строку резултата
			line = ('# => '+str(i)+'/')
		res.append(line) # дополняем список результатами
	return '\n'.join(res) # форматируем результат для вывода на экран
	
def filter_anagrams(word:str, alist:list):
	res = [i for i in alist if Counter(word) == Counter(i)]
	print(res)
	return res

def same_parity_filter(alist):
	res = []
	if len(alist) > 0:
		res = [i for i in alist if abs(alist[0] % 2) == abs(i % 2)]
	print(res)
	return res

def test():
	
	same_parity_filter([])
	# []
	same_parity_filter([2, 0, 1, -3, 10, -2])
	# [2, 0, 10, -2]
	same_parity_filter([-1, 0, 1, -3, 10, -2])
	# [-1, 1, -3]

if __name__ == '__main__':
	test()