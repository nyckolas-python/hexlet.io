n = 12 # переменная для всех рекурсивных ф-ций

# Recursion
def rec(x):
	if x < n:
		print(x, end=' ')
		rec(x+1)
		print(x, end=' ')

rec(1) # 1 2 3 3 2 1
print()

# Factorial
def fact(n):
	if n == 1:
		return 1
	return fact(n-1)*n


print(f'Factorial {n} ->',fact(n))

# Fibonacci
def fibo(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	return fibo(n-1) + fibo(n-2)

print(f'Fibonacci {n} ->',fibo(n))

# Polyndrom
def polyndrom(s):
	if len(s) <= 1:
		return True
	if s[0] != s[-1]:
		return False
	return polyndrom(s[1:-1])

print('\"шалаш\" is polyndrom ->',polyndrom('шалаш')) # True
print('\"saippuakivikauppias\" is polyndrom ->',polyndrom('saippuakivikauppias')) # True
print('\"шалаШ\" is polyndrom ->',polyndrom('шалаШ')) # False

def recline(ss):
	if len(ss) == 1 or len(ss) == 2:
		return ss
	return ss[0]+'('+recline(ss[1:-1])+')'+ss[-1]

print('\"malinka\" ->',recline('malinka')) # "malinka" -> m(a(l(i)n)k)a
print('\"malinka\" ->',recline('malina')) # "malinka" -> m(a(li)n)a

a = [1,2,[3,4,[5,[6,[7,[8,[9,[10,[11],12],13],14],15]]]]]
def vlozhenie(spisok, level=1):
	print(*spisok, 'level =',level)
	for i in spisok:		
		if type(i) == list:
			level += 1
			vlozhenie(i, level)

vlozhenie(a)
'''
1 2 [3, 4, [5, [6, [7, [8, [9, [10, [11], 12], 13], 14], 15]]]] level = 1
3 4 [5, [6, [7, [8, [9, [10, [11], 12], 13], 14], 15]]] level = 2
5 [6, [7, [8, [9, [10, [11], 12], 13], 14], 15]] level = 3
6 [7, [8, [9, [10, [11], 12], 13], 14], 15] level = 4
7 [8, [9, [10, [11], 12], 13], 14] 15 level = 5
8 [9, [10, [11], 12], 13] 14 level = 6
9 [10, [11], 12] 13 level = 7
10 [11] 12 level = 8
11 level = 9
'''
def collatz(n):
	if n == 1:
		return True
	if n % 2 == 0:
		return collatz(n // 2)
	return collatz(n * 3 + 1)

print(collatz(10))

def is_even(n):
    if (n < 2):
        return (n % 2 == 0)
    return (is_even(n - 2))
n = int(input("Введите число:"))
if (is_even(n) == True):
		print("Число четное!")
else:
			print("Число нечетное!")