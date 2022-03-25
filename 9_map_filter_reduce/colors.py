g = 'global'

def colors(param='r'):
	y = 'yellow'
	g = 'green'

	def print_red():
		r = 'red'
		nonlocal y
		print(r, y, g)
		y = 'was changed'

	def print_blue():
		b = 'blue'
		print(b, y, g)

	if param == 'r':
		print_red()
	elif param == 'b':
		print_blue()
	else:
		print('i dont know this color')


colors(32)