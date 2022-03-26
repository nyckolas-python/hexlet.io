def counting_sort():
	a = [1,2,3,4,4,4,3,3,2,2,1,2,4,2,3,4]
	count = [0]*(max(a)+1)
	for i in a:
		count[i]+=1
	#print(count)
	print(a)
	for i in range(max(a)+1):
		if count[i]>0:
			print((str(i)+', ')*count[i], end='')

counting_sort()