
def call_twice(function, abc):
	a = function(abc)
	b = function(abc)
	return print((a, b))

call_twice(input, 'Enter Value: ') # Два раза ввод, вывод кортеж
# 'Enter Value: ' 'foo'
# 'Enter Value: ' 'bar'
# ('foo', 'bar')