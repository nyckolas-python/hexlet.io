def flip(function):
	
	def inner(name, surname):
		return function(name=surname, surname=name)
	return inner

def greet(name, surname):
	res = 'Hello, {name} {surname}!'.format(name=name, surname=surname)
	return print(res)

f = flip(greet)
f('Christian', 'Teotor') # Hello, Teotor Christian!