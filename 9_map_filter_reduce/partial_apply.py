def partial_apply(function, name):
	
	def inner(surname):
		return function(name, surname)
	return inner

def greet(name, surname):
	res = 'Hello, {name} {surname}!'.format(name=name, surname=surname)
	return print(res)

f = partial_apply(greet, 'Dorian')
f('Gray') # Hello, Dorian Gray!
