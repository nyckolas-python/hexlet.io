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

a = compose(mul3, add5)(1) # 18
b = compose(add5, mul3)(1) # 8
c = compose(mul3, str)(1) # '111'
d = compose(str, mul3)(1) # '3'