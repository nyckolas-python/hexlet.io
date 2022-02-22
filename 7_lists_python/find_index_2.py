def find_index_2(item, list):
	count = 0
	for i in range(len(list)):
		if list[i] == item:
			count += 1
			if count == 2:
				return i
	if count == 1:
		return None
	elif item not in list:
		return None