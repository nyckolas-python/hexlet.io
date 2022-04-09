from collections import Counter


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
	
# Test Program

print(histo([1, 1, 3, 4, 5, 5, 1]))
	# => 1/### 3
	# => 2/
	# => 3/# 1
	# => 4/# 1
	# => 5/## 2
print(histo([1, 1, 3, 4, 5], bar_char = '*'))
	# => 1|** 2
	# => 2|
	# => 3|* 1
	# => 4|* 1
	# => 5|* 1
print(histo([1, 1, 3, 4, 5], min_value = 3, max_value = 4))
	# => 3|# 1
	# => 4|# 1
print(histo([], min_value = 1, max_value = 5))
	# => 1|
	# => 2|
	# => 3|
	# => 4|
	# => 5|