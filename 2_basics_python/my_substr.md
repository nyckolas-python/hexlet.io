ЗаданиеРеализуйте функцию my_substr(), которая извлекает из строки подстроку указанной длины. Она принимает на вход два аргумента: строку и длину, и возвращает подстроку, начиная с первого символа:

Решение учителя:


def my_substr(string, length):
	result_string = ''
    index = 0
    while index < length:
        result_string = result_string + string[index]
        index = index + 1

    return result_string

Моё решение:


def my_substr(string, value):
	new_string = ''
    lenth = len(string) - 1
    i = 0
    if value <= lenth:
        while i < value:
            new_string = new_string + string[i]
            i = i + 1
        return new_string
    return string