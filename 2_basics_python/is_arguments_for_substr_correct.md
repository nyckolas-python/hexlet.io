ЗаданиеРеализуйте функцию-предикат is_arguments_for_substr_correct(), которая принимает три аргумента:
	1. 
строку;
	2. 
индекс, с которого начинать извлечение;
	3. 
длину извлекаемой подстроки.


Функция возвращает False, если хотя бы одно из условий истинно:
	* 
Отрицательная длина извлекаемой подстроки.
	* 
Отрицательный заданный индекс.
	* 
Заданный индекс выходит за границу всей строки.
	* 
Длина подстроки в сумме с заданным индексом выходит за границу всей строки.


В ином случае функция возвращает True.
Не забывайте, что индексы начинаются с 0, поэтому индекс последнего элемента — это «длина строки минус 1».

Решение учителя:


def is_arguments_for_substr_correct(string, index, length):
	if index < 0:
        return False
    elif length < 0:
        return False
    elif index > len(string) - 1:
        return False
    elif index + length > len(string):
        return False
    return True

Моё решение:


def is_arguments_for_substr_correct(string, start, length):
	if length < 0 or start < 0 or start > (len(string) - 1) or (start + length) > len(string):
        return False
    else: return True