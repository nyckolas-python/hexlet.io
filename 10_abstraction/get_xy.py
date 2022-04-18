from math import *

def make_descartes_point(x, y):
	# конвертация
	return {
		"angle": atan2(y, x),
		"radius": sqrt(x ** 2 + y ** 2)
		}

def get_x(point):
	print(round(point["radius"] * cos(point["angle"])))
	return round(point["radius"] * cos(point["angle"]))

def get_y(point):
	print(round(point["radius"] * sin(point["angle"])))
	return round(point["radius"] * sin(point["angle"]))

# Test Program

x = 4
y = 8

point = make_descartes_point(x,y)

get_x(point)
get_y(point)