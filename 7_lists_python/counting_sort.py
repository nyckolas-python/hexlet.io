def counting_sort():
	a = [1,2,3,4,4,4,3,3,2,2,1,2,4,2,3,4]
	count = [0]*(max(a)+1)
	for i in a:
		count[i]+=1
		print(i, end=' ') # вывод неотсортированного списка чисел
	print()


	for i in range(max(a)+1):
		if count[i]>0: # выводить только если количество 1 и больше
			print((str(i)+' ')*count[i], end='') # вывод ОТСОРТИРОВАННОГО списка чисел

def text_counting_sort():
	a = 'abcdmvkefnvknenmrvjlkKLJKLJ"KJklmlrkeljeklmkl'
	count = [0]*26 # количество букв в анг. алфивите
	
	for i in a.lower():
		if i>='a' and i<='z':
			nomer = ord(i)-97
			count[nomer] += 1
			print(i, end=' ') # вывод неотсортированной строки
	print()
	for i in range(26):
		if count[i]>0: # выводить только если количество 1 и больше
			
			print((chr(i+97)+' ')*count[i], end='') # вывод ОТСОРТИРОВАННОЙ строки
			#print(chr(i+97), count[i], end=' \n') # вывод БУКВА КОЛТЧЕСТВО
		
counting_sort() # 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4
print('')
text_counting_sort()