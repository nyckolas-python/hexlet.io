def make_decarte_point(x, y):
	return {"x": x, "y": y}

def make_rectangle(top_left_point, width, height):
	return {
		'top_left_point': top_left_point,
		'top_right_point': {'x': top_left_point['x'] + width, 'y': top_left_point['y']},
		'bottom_right_point': {'x': top_left_point['x'] + width, 'y': top_left_point['y'] - height},
		'bottom_left_point': {'x': top_left_point['x'], 'y': top_left_point['y'] - height}		
		}

def get_quadrant(point):
	if point['x'] > 0 and point['y'] > 0:
		res = 'I квадрант'
	if point['x'] < 0 and point['y'] > 0:
		res = 'II квадрант'
	if point['x'] < 0 and point['y'] < 0:
		res = 'III квадрант'
	if point['x'] > 0 and point['y'] < 0:
		res = 'IV квадрант'
	if point['x'] == 0 and point['y'] != 0:
		res = 'на оси X'
	if point['x'] != 0 and point['y'] == 0:
		res = 'на оси Y'
	if point['x'] == 0 and point['y'] == 0:
		res = point
	#print(res)
	return res

def contains_origin(rectangle):
	quadrant_list = ['I квадрант', 'II квадрант', 'III квадрант', 'IV квадрант']
	#print(rectangle.values()) # [{'x': -4, 'y': 3}, {'x': 1, 'y': 3}, {'x': 1, 'y': -1}, {'x': -4, 'y': -1}]
	check = [get_quadrant(i) for i in rectangle.values()]
	print(set(check) == set(quadrant_list))
	return set(check) == set(quadrant_list) # True

# Test Program
p = make_decarte_point(0, 1)
rectangle = make_rectangle(p, 4, 5)
contains_origin(rectangle)

p = make_decarte_point(-4, 3)
rectangle = make_rectangle(p, 5, 4)
contains_origin(rectangle)