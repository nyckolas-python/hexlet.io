def greet(name, *args):
	next = ''
	if len(args) >= 1:
		next = ' and ' + ' and '.join(args)
	return print('Hello, ' + name + next + '!')

# Test Program
greet('Bob') # Hello, Bob!
greet('Bob', 'Mary') # Hello, Bob and Mary!
greet('Bob', 'Mary', 'Mykola') # Hello, Bob and Mary and Mykola!