ЗаданиеРеализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:


join_numbers_from_range(1, 1) # '1'
join_numbers_from_range(2, 3) # '23'
join_numbers_from_range(5, 10) # '5678910'

Решение учителя:


def join_numbers_from_range(start, end):
	i = start
    result = ''
    while i <= end:
        result = result + str(i)
        i = i + 1
    return result

Моё решение:


def join_numbers_from_range(start, finish):
	result = ''
    i = start
    while i <= finish:
        result = result + str(i)
        i = i + 1
    return result