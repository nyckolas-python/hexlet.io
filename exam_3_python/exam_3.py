#!/usr/bin/env python3

from functools import wraps
from ipaddress import IPv4Address
from operator import itemgetter
from typing import Counter


def compose(func_1, func_2):
	def inner(*args, **kwargs):
		res = func_1(func_2(*args, **kwargs))
		print(res)
		return res
	return inner
def add5(x):
	return x + 5
def mul3(x):
	return x * 3

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

	
	
def test():

	@interactive('Calculator')
	@asks('x', 'Enter first number: ')
	@asks('y', 'Enter second number: ')
	def calc(x, y):
		"""
		Ф-ция принимает два аргумента "х" и "у" и возвращает их сумму.
		"""
		return int(x) + int(y)

	calc()
	print(calc) 
	#Calculator
	#Enter first number: 42
	#Enter second number: 57
	# 99
	#<function test.<locals>.calc at 0x7f4e0e7a5b80>
if __name__ == '__main__':
	test()