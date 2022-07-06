# Дана ф-ция rgb(). Использую её, реализуем класс Color, с атрибутами: red, green, blue

def rgb(color):
	if color == 'red':
		return 'rgb(255, 0, 0)'
	elif color == 'green':
		return 'rgb(0, 255, 0)'
	elif color == 'blue':
		return 'rgb(0, 0, 255)'

class Color:
	red = rgb('red')
	green = rgb('green')
	blue = rgb('blue')
	
print(Color.red) # rgb(255, 0, 0)
print(Color.green == 'rgb(0, 255, 0)') # True