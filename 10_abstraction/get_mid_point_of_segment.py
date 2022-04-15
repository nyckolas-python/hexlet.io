def make_decarte_point(x, y):
	return {"x": x, "y": y}

def make_segment(point1:dict, point2:dict):
	return {'x1': point1['x'], 'y1': point1['y'], 'x2': point2['x'], 'y2': point2['y']}

def get_mid_point_of_segment(s:dict):
	return {'x' : (s['x1'] + s['x2'])/2, 'y': (s['y1'] + s['y2'])/2}

# Test Program

segment = make_segment(make_decarte_point(3,2),make_decarte_point(0,0))
mid = get_mid_point_of_segment(segment)
print(mid) # {'x': 1.5, 'y': 1.0}
