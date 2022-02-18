ЗаданиеРеализуйте функцию multiply_number_from_range(), которая перемножает числа в указанном диапазоне включая границы диапазона. Пример вызова:

multiply_number_from_range(1, 5) # 1 * 2 * 3 * 4 * 5 = 120
multiply_number_from_range(2, 3) # 2 * 3 = 6
multiply_number_from_range(6, 6) # 6

Решение учителя:


def multiply_number_from_range(start, finish):
	i = start
    result = 1
    while i <= finish:
        result = result * i
        i = i + 1
    return result

Моё решение:


def multiply_number_from_range(start, finish):
	multi_sum = 1
    i = start
    while i <= finish:
        multi_sum = multi_sum * i
        i = i + 1
    return multi_sum