from collections import defaultdict


def rgb(color):
	if color == 'red':
		return 'rgb(255, 0, 0)'
	elif color == 'green':
		return 'rgb(0, 255, 0)'
	elif color == 'blue':
		return 'rgb(0, 0, 255)'

def get_colors():
	c = defaultdict(set)
	c['red'].add(rgb('red'))
	c['green'].add(rgb('green'))
	c['blue'].add(rgb('blue'))
	
	return dict(c)

# Test Program
colors = get_colors() # {'red': {'rgb(255, 0, 0)'}, 'green': {'rgb(0, 255, 0)'}, 'blue': {'rgb(0, 0, 255)'}}
print(colors.keys() == {'red', 'green', 'blue'}) # True