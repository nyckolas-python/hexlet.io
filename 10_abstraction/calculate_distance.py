def calcalate_disatence(point1:list = [-1, -1], point2:list = [2, 3]):
	res = ((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)**0.5
	print(res)
	return res

calcalate_disatence()