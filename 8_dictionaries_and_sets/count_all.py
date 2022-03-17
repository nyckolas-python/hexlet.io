from collections import Counter

def count_all(alist):
	result = dict(Counter(alist))
	return print(result)

# Test programm
count_all(['cat', 'dog', 'cat'])
count_all('hello')
count_all('*' * 20)