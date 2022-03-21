#!/usr/bin/env python3
import roman
from  collections import Counter, defaultdict

def to_rna(dna):
	d = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
	rna = ''
	for v in dna:
		rna += d[v]
	return rna

def build_query_string(param):
	result = ''
	for i in param:
		result =''.join(str(i)+str(param[i])) + result
	return print(result)

def to_roman(num):
	roman = { # Dictionary of roman numbers
		1000: 'M',
		900: 'CM',
		500: 'D',
		400: 'CD',
		100: 'C',
		90: 'XC',
		50: 'L',
		40: 'XL',
		10: 'X',
		9: 'IX',
		5: 'V',
		4: 'IV',
		1: 'I'
		}
	result = ''
	if num < 4000:	
		for i in roman:
			result += num // i * roman[i]
			num %= i
		return result
		print(result)
	else:
		return False
		print(False)

def to_arabic(txt):
	txt = txt.upper()
	try:
		res = roman.fromRoman(txt)
		print(res)
	except roman.InvalidRomanNumeralError:
		print('Вы указали НЕ Римское число!')

def find_where(data, d1):
	for d2 in data:
		if all(k in d2 and d1[k] == d2[k] for k in d1) == True: # сравниваем есть ли все елементы словаря d1 в d2
			print(d2)
			return d2
	print(None)
	return None

def find_where_2(data, search):
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

def scrabble(abc, word):
	d1 = dict(Counter(word.lower()))
	d2 = dict(Counter(abc.lower()))
	#print(d1) # {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}
	#print(d2) # {'r': 1, 'k': 1, 'q': 1, 'o': 1, 'd': 1, 'l': 1, 'w': 1}
	print(all(k in d2 and d1[k] <= d2[k] for k in d1)) # сравниваем все значения <= всех елементов словаря d1 в d2
	return all(k in d2 and d1[k] <= d2[k] for k in d1)

def merged(*alist):
	x = defaultdict(set)
	for i in alist:
		for k, v in i.items():
			x[k].add(v)
			#print(dict(x)) # выводим на экран каждую итерацию
	print(dict(x))
	return dict(x)

def gen_diff(d1, d2):
	res = defaultdict(str)
	for k in d1:
		if k not in d2:
			res[k] = 'deleted'
		elif k in d2 and d1[k]!=d2[k]:
			res[k] = 'changed'
		elif k in d2 and d1[k]==d2[k]:
			res[k] = 'unchanged'
		elif k in d2 and k not in d1:
			res[k] = 'added'
	for k in d2:
		if k not in d1:
			res[k] = 'added'
	print(dict(res))
	return res
			

def test():

	gen_diff(
		{"one": "eon", "two": "two", "four": True},
		{"two": "own", "zero": 4, "four": True},
		) # {"one": "deleted", "two": "changed", "four": "unchanged", "zero": "added"}


if __name__ == '__main__':
	test()