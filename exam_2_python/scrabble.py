from collections import Counter


def scrabble(abc, word):
	d1 = dict(Counter(word.lower()))
	d2 = dict(Counter(abc.lower()))
	#print(d1) # {'w': 1, 'o': 1, 'r': 1, 'l': 1, 'd': 1}
	#print(d2) # {'r': 1, 'k': 1, 'q': 1, 'o': 1, 'd': 1, 'l': 1, 'w': 1}
	print(all(k in d2 and d1[k] <= d2[k] for k in d1)) # сравниваем все значения <= всех елементов словаря d1 в d2
	return all(k in d2 and d1[k] <= d2[k] for k in d1)

# Test Program

scrabble('rkqodlw', 'world') # True
scrabble('avj', 'java') # False
scrabble('avjafff', 'java') # True
scrabble('', 'hexlet') # False
scrabble('scriptingjava', 'JavaScript') # True