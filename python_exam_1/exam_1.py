#!/usr/bin/env python3

import itertools


def is_continuous_sequence(a):
    if len(a) > 1:
        n = a[1] - a[2]
        for i in range(len(a) - 1):
            if (a[i] - a[i + 1]) != n:
                return False
                break
        return True
    else:
        return False


def find_longest_length(str):
    sub_str = ''
    max_length = 0
    for i in str:
        if i not in sub_str:
            sub_str += i
            # print(sub_str) вывод текущей подстроки
        else:
            max_length = max(max_length, len(sub_str))
            # print(max_length) хранение значения максимальной длины подстроки
            sub_str = sub_str[sub_str.index(i) + 1:] + i
    max_length = max(max_length, len(sub_str))
    return max_length


def triangle(n):
    row = []
    rows = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(i + 1):
            if j != 0 and j != i:
                row[j] = rows[i - 1][j - 1] + rows[i - 1][j]
        rows.append(row)
    return rows[n - 1]


def transposed(list):
    new_list = []
    if len(list) > 1:
        for i in range(len(list[0])):
            new_elem = []
            for j in range(len(list)):
                new_elem.append(list[j][i])
            new_list.append(new_elem)
        return new_list
    else:
        return list


def input_list_fn():
    ele = []
    input_list = []
    print('Вводите значения цен, нажимайте enter')
    print(' для окончания ввода просто нажмите enter')
    ele = list(input('-->> '))
    while True:
        try:
            for i in ele:
                #print(ele[i])
                if i.isdigit() == False:
                    ele.remove(i)
            input_list.append(ele)
            print(input_list)
            ele = list(input('-->> '))
        except:
            break


def sum_of_intervals(input_list):
    new_list = []
    result = []

    for i in range(len(input_list)):
        if input_list[i][0] <= input_list[i][1]:
            new_list = range(input_list[i][0], input_list[i][1])
            for j in new_list:
                if j not in result:
                    result.append(j)
        else:
            print(
                'Некорректные данные... Первое значение интервала должно быть меньше второго!'
            )
    print(len(result))


def length_of_last_word(str):
    list_of_word = []
    str = str.replace('/n', ' ')
    list_of_word = str.replace('/t', ' ').split()
    if len(list_of_word) > 0:
        print(len(list_of_word[-1]))
    else:
        print(len(list_of_word))


def get_hm(x):
    print(bin(x).count("1"))


def rpn_calc(alist):
    result = 0
    stek = []
    operator = ['+', '-', '*', '/']
    for i in alist:  # Для каждого елемента в списке
        if isinstance(
                i, int
        ) == True:  # Проверяем если елемент списка - цифра, то записываем на вершину стека
            stek.append(i)
        elif i in operator:  # Проверяем если елемент списка - оператор , то записываем на вершину стека
            a = stek.pop()  # Забираем две последних цифры для операции
            b = stek.pop()
            if i == '+':  # Сравниваем елемент операции, выполняем операцию
                result = b + a
                #print(b,'+',a,'=',result) # промежуточная операция
            elif i == '-':
                result = b - a
                #print(b,'-',a,'=',result) # промежуточная операция
            elif i == '*':
                result = b * a
                #print(b,'*',a,'=',result) # промежуточная операция
            elif i == '/':
                result = b / a
                #print(b,'/',a,'=',result) # промежуточная операция
            stek.append(result)
    print(result)


def show(image):  # Функция вывода на экран пока есть строки
    for line in image:
        print(line)


def compare_version(ver_1, ver_2):
    ver_1 = ver_1.split('.')
    ver_2 = ver_2.split('.')
    if ver_1 > ver_2:
        print(1)
    elif ver_1 < ver_2:
        print(-1)
    elif ver_1 == ver_2:
        print(0)


def is_continuous_sequence(a):
    if len(a) > 1:
        n = a[1] - a[2]
        for i in range(len(a) - 1):
            if (a[i] - a[i + 1]) != n:
                return False
                break
        return True
    else:
        return False


def summary_ranges(alist):
    result = []
    temp = []
    j = 0
    if len(alist) > 1:
        for i in range(1, len(alist)):

            if alist[i] - alist[i - 1] == 1:
                temp = alist[j:i + 1]
                temp = [str(temp[0]), str(temp[-1])]
                temp = '->'.join(temp)
                #print(temp)
            else:
                if temp not in result and temp != []:
                    result.append(temp)
                j = i
                temp = []
        if temp != []:
            result.append(temp)
        print(result)
    else:
        print(result)


def chunked(n, alist):
    print([
        alist[
            i:i +
            n]  # Для всех елементов списка формируем слайсы 0: длина : n - длина слайса
        for i in range(0, len(alist), n)
    ])


def grouper(alist, n):
    args = [iter(alist)] * n
    return zip(*args)


#[(0, 1, 2), (3, 4, 5), (6, 7, 8)]


def test_count():
    c2 = itertools.count(0, 2)
    for i in c2:
        #including terminating condition, else loop will keep on going.(infinite loop)
        if i > 25:
            break
        else:
            print(i, end=" ")


def ichunks(n, alist):
    #new_list = [expression for member in iterable (if conditional)]
    new_list = []
    if type(alist) is list:  # проверяем тип входящиего -> список или итератор
        new_list = map(lambda x: list(itertools.islice(alist, x, x + n)),
                       itertools.count(0, n))
        for i in new_list:  # если список то используем itertools.count(0, n) поток чисел с шагом n
            if len(i) != n:
                return  # проверка хватает ли в чанке всех элементов для заданной длины
            yield i
    elif type(alist) is not list:
        new_list = map(lambda x: list(itertools.islice(alist, x, x + n)),
                       itertools.repeat(0))
        for i in new_list:  # если итератор то используем itertools.repeat(0) поток нулей
            if len(i) != n:
                return  # проверка хватает ли в чанке всех элементов для заданной длины
            yield i
    #for i in itertools.repeat(0):
    #new_list = list(itertools.islice(alist, i, i + n))
    #yield new_list


def enlarge(mas):
    new_mas = []
    for line in mas:  # Для каждой строки в масиве
        new_line = []
        for elem in line:  # Перебираем каждый символ строки
            new_line += elem * 2  # Удваеваем каждый символ
        new_line = ''.join(new_line)  # Склеиваем все символы в единую строку
        new_mas.append(new_line)  # Добавляем строку в новый масив
        new_mas.append(new_line)  # Дублируем строку
    return new_mas


def mirror_matrix(l):
    new_mas = []
    row = []
    print('l == ['
          )  # Вывод на экран первой строки ответа (название матрицы == скобка)
    for row in l:  # цыкл перебора всех рядов матрицы
        new_row = []
        a = len(row) // 2  # делим длину ряда пополам
        even = len(row) % 2  # проверяем чётность
        new_row = row[:a + even] + row[
            a - 1::-1]  # зеркалим ряд с учетом остатка от деления на 2
        print('    ', new_row,
              end=',\n')  # Вывод на экран всех рядов матрицы + формат
        new_mas.append(new_row)  # добавляем зеркальные ряды в новую матрицу
    print(']\n')  # Вывод на экран закрывающей скобки
    return new_mas


def snail_path(m):
	f = lambda m: m and m.pop(0) + f([list(x) for x in zip(*m)][::-1])
	return print(m if not m else m.pop(0) +
				f(list(list(x) for x in zip(*m))[::-1]))

def multiply(m1,m2):
    tmp = []
    m3 = []
    s = 0
    if len(m2) == len(m1[0]):	# количество столбцов m1 матрицы должно быть равно количеству строк m2 матрицы
        #print('ok')
        r1 = len(m1)    # количество строк m1
        c1 = len(m1[0])    # количество столбцов m1
        r2 = c1    #  количество строк m2
        c2=len(m2[0])    # количество столбцов m2
        for z in range(0,r2): # цыкл сколько строк в т2
            for j in range(0, c2): # цыкл сколько столбцов в т2
                for i in range(0, c1): # сколько столбцов в т1
                    s += m1[z][i]*m2[i][j]  # вычисляем каждые элемент
                tmp.append(s) # добавляем элемент в строку
                s = 0   # обнуляем элемент
            m3.append(tmp) # добавляем строку новую матрицу
            tmp = [] # обнуляем строку
        return print(m3)
    else: print('количество столбцов матрицы 1 должно быть равно количеству строк матрицы 2 !!!')

def multiply2(a,b):
    m = len(a)                                            # a: m × n
    n = len(b)                                            # b: n × k
    k = len(b[0])

    c = [[None for __ in range(k)] for __ in range(m)]    # c: m × k

    for i in range(m):
        for j in range(k):       
            c[i][j] = sum(a[i][kk] * b[kk][j] for kk in range(n))
 
    print(c)

def test():

	A = [
		[1, 2],
		[3, 2]]
	B = [
		[3, 2],
		[1, 1]]
	multiply2(A, B)
	C = [
		[2, 5],
		[6, 7],
		[1, 8],
		]
	D = [
		[1, 2, 1],
		[0, 1, 0],
		]
	multiply2(C, D)

if __name__ == '__main__':
    test()
